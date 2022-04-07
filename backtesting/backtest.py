import os
import copy
import random
import datetime

import pandas as pd
import numpy as np

from portfolio.portfolio import Portfolio
from pipeline.prepare_indicators import prepare_indicators, build_period
from pipeline.prepare_data import write_nn_to_file

from algorithm.model import TestModel
from analysis.strategy import prepare_trades, analyse_strategy

from algorithm.NN import NeuralNetwork5


def back_test(df, model, cash_initial=None, buy_weight=None, sell_weight=None):
    """
    Back tests your trading strategies, and builds a timeline of the Portfolio
    """
    if cash_initial:
        if buy_weight and sell_weight:
            portfolio = Portfolio(cash_initial=cash_initial, buy_weight=buy_weight, sell_weight=sell_weight)
        else:
            portfolio = Portfolio(cash_initial=cash_initial)
    else:
        portfolio = Portfolio()

    # This needs to be checked BIG TIME
    portfolio.asset_amt['BTCUSD'] = 0.0

    trades = []
    for index, row in df.iterrows():
        tensor = row[['bb_ratio', 'rsi_14', 'rsi_sma_diff', 'aroon_up', 'aroon_dn', 'stoch_d']]
        output = model.feedforward(tensor.values)                             # Model calc and output
        price = {row['symbol']: row['close']}
        portfolio.update_prices(price=price)
        portfolio.update_portfolio()
        portfolio.get_order_type(output, token=row['symbol'])
        portfolio.trade_pair(row['symbol'])
        portfolio.update_portfolio()

        trades.append([portfolio.order_type, portfolio.trade_amt, portfolio.asset_amt['cash'],
                       portfolio.asset_amt[row['symbol']], portfolio.asset_values[row['symbol']]])

    df_trades = pd.DataFrame(trades, columns=['TRADE', 'TRADE_AMT', 'CASH', 'ASSET_AMT', 'ASSET_VALUE'])
    df_all = df.copy()
    df_all = pd.merge(df_all, df_trades, left_index=True, right_index=True)
    # df_all['TRADE_AMT'] = 0.999 * df_all['TRADE_AMT']
    return df_all


if __name__ == '__main__':
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    # Periods and iterations
    current_date = datetime.datetime.now()
    periods = 1000
    iterations = 2000
    sample_size = 10

    # Neural Network Structure
    input_size = '6'
    layer_1_size = '10'
    layer_2_size = 'None'
    output_size = '3'
    middle_layer_activation_func = 'relu'
    output_activation_func = 'softmax'

    metric_names = ['ITERATION', 'SUPER_METRIC', 'ROI', 'WIN_RATIO', 'MAX_DRAWDOWN', 'WINNER_ROI_AVG', 'LOSER_ROI_AVG',
                    'WINNER_ROI_MAX', 'LOSER_ROI_MAX', 'ROI_ASSET', 'STD_DEV_ASSET', 'STD_DEV_PORTFOLIO', 'RANGE_ASSET',
                    'RANGE_PORTFOLIO', 'CORR', 'NO_OF_TRADES']

    # Price data files
    price_files = os.listdir('C:/Users/chadg/GARD/Projects/slann/data/price')

    # Create data file
    df_metrics = pd.DataFrame(columns=metric_names)
    file_name = 'C:/Users/chadg/GARD/Projects/slann/backtesting/backtesting_data/metrics/nn_architecture_' + \
                'relu-softmax-6-10-None-3_850-10_2022-04-07T10-55-14.csv'
    # df_metrics.to_csv(file_name, index=False)

    # Initialize trading strategy (Neural Network ML model)
    parent = NeuralNetwork5(init=False)

    # Iterate through learning process
    for i in range(iterations):

        # Prepare models for back testing
        child = copy.deepcopy(parent)
        child.mutate(alpha=0.3)

        # Create dataframes for child vs parent metric comparison
        parent_sample_metrics = pd.DataFrame(columns=metric_names)
        child_sample_metrics = pd.DataFrame(columns=metric_names)

        for s in range(sample_size):

            # select data for back testing
            file_index = np.random.randint(0, len(price_files))
            df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price/' + price_files[file_index], header=0)

            df = df[~df['date'].str.contains('PM')]
            df = df[~df['date'].str.contains('AM')]
            df['date'] = pd.to_datetime(df['date'])
            df = df[df['date'] < datetime.datetime(2021, 1, 1, 0, 0, 0)]

            rows = len(df['close'].to_list())
            start = random.randint(0, rows - periods)

            df = df[start:start + periods]
            df = df.sort_values(by=['date'])
            df = build_period(df)

            # prepare data and calculate indicators
            df = prepare_indicators(df)
            df = df.dropna()
            df = df[['date', 'symbol', 'close', 'bb_ratio', 'rsi_14', 'rsi_sma_diff',
                     'aroon_up', 'aroon_dn', 'stoch_d']]
            df = df.reset_index(drop=True)

            drop_columns = ['bb_ratio', 'rsi_14', 'rsi_sma_diff', 'aroon_up', 'aroon_dn', 'stoch_d']

            # Back test parent strategy
            df_parent = back_test(df, parent, cash_initial=100000)
            df_parent = df_parent.drop(labels=drop_columns, axis=1)
            df_parent = prepare_trades(df_parent)                               # Prepare parent strategy trades
            if len(list(df_parent['TRADE'])) == 0:
                continue
            metric_parent = analyse_strategy(df_parent)                         # Analyse parent strategy
            metric_parent['ITERATION'] = i
            parent_sample_metrics = parent_sample_metrics.append(metric_parent, ignore_index=True)

            # Back test child strategy
            df_child = back_test(df, child, cash_initial=100000)
            df_child = df_child.drop(labels=drop_columns, axis=1)
            df_child = prepare_trades(df_child)                                 # Prepare child strategy trades
            if len(list(df_child['TRADE'])) == 0:
                continue
            metric_child = analyse_strategy(df_child)                           # Analyse child strategy
            metric_child['ITERATION'] = i
            child_sample_metrics = child_sample_metrics.append(metric_child, ignore_index=True)

        # Check metrics to determine which strategy was better - set new parent
        metrics_parent = dict(parent_sample_metrics.mean())
        metrics_child = dict(child_sample_metrics.mean())

        if metrics_child['SUPER_METRIC'] >= metrics_parent['SUPER_METRIC']:
            parent = child
            df_metrics = pd.DataFrame(metrics_child, index=[0])
        else:
            parent = parent
            df_metrics = pd.DataFrame(metrics_parent, index=[0])

        # Write back testing data to file
        df_metrics.to_csv(file_name, mode='a', index=False, header=False)

        # Print Super Metric Information
        print('%d) Super metric: ' % i, round(metrics_parent['SUPER_METRIC'], 4))

        # Check Super Metric for NaN - reset NN if necessary
        if np.isnan(metrics_parent['SUPER_METRIC']):
            parent = NeuralNetwork5()

    # Write NN architecture to file
    np.savetxt('C:/Users/chadg/GARD/Projects/slann/backtesting/backtesting_data/neural_networks/SMGANN' +
               '_' + current_date.strftime('%Y-%m-%dT%H-%M-%S') + '_W1_' + middle_layer_activation_func +
               '-' + output_activation_func + '-' + input_size + '-' + layer_1_size + '-' + layer_2_size +
               '-' + output_size + '_' + str(periods) + '-' + str(iterations) + '.csv', parent.weights1, delimiter=",")
    np.savetxt('C:/Users/chadg/GARD/Projects/slann/backtesting/backtesting_data/neural_networks/SMGANN' +
               '_' + current_date.strftime('%Y-%m-%dT%H-%M-%S') + '_W2_' + middle_layer_activation_func +
               '-' + output_activation_func + '-' + input_size + '-' + layer_1_size + '-' + layer_2_size +
               '-' + output_size + '_' + str(periods) + '-' + str(iterations) + '.csv', parent.weights2, delimiter=",")
