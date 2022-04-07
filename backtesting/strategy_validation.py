import os
import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pipeline.prepare_indicators import prepare_indicators, build_period
from analysis.strategy import prepare_trades, analyse_strategy
from backtesting.backtest import back_test

from algorithm.NN import NeuralNetwork5


def performance_curve(date, portfolio, asset, title='Title', asset_name=None):
    # Prepare data
    portfolio = 100 * portfolio / portfolio.loc[0]
    asset = 100 * asset / asset.loc[0]

    # Plot curve
    plt.plot(date, portfolio, c='r')
    plt.plot(date, asset, c='b')

    # Label plot
    plt.title(title)
    plt.ylabel('Performance [%]')
    plt.xlabel('Date')

    if asset_name:
        plt.legend(['Portfolio Strategy', asset_name], loc='upper left')
    else:
        plt.legend(['Portfolio Strategy', 'Asset'], loc='upper left')

    plt.show()


def compare_metrics(portfolio_metric, asset_metric, title='Title', asset_name=None):

    # Plot curve
    labels = ['Portfolio Strategy', asset_name]
    data = [100*portfolio_metric, 100*asset_metric]
    plt.bar(labels, data)

    # Label plot
    plt.title(title)
    plt.ylabel('Performance [%]')

    plt.show()


if __name__ == '__main__':

    pd.set_option('display.max_columns', 100)

    # Periods and iterations
    current_date = datetime.datetime.now()

    # Neural Network Structure
    input_size = '6'
    layer_1_size = '10'
    layer_2_size = 'None'
    output_size = '3'
    middle_layer_activation_func = 'relu'
    output_activation_func = 'softmax'

    # Select data for back testing
    price_files = os.listdir('C:/Users/chadg/GARD/Projects/slann/data/price')

    file_index = np.random.randint(0, len(price_files))
    df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price/' + price_files[file_index], header=0)

    df = df[~df['date'].str.contains('PM')]
    df = df[~df['date'].str.contains('AM')]
    df['date'] = pd.to_datetime(df['date'])
    df = df[df['date'] >= datetime.datetime(2021, 1, 1, 0, 0, 0)]

    df = df.sort_values(by=['date'])
    df = build_period(df)

    # Initialize trading strategy (Neural Network ML model)
    strategy = NeuralNetwork5(init=False)

    # prepare data and calculate indicators
    df = prepare_indicators(df)
    df = df.dropna()
    df = df[['date', 'symbol', 'close', 'bb_ratio', 'rsi_14', 'rsi_sma_diff',
             'aroon_up', 'aroon_dn', 'stoch_d']]
    df = df.reset_index(drop=True)

    drop_columns = ['bb_ratio', 'rsi_14', 'rsi_sma_diff', 'aroon_up', 'aroon_dn', 'stoch_d']

    # Back test parent strategy
    df = back_test(df, strategy, cash_initial=100000)

    df = df.drop(labels=drop_columns, axis=1)
    df = prepare_trades(df)                               # Prepare strategy trades

    performance_curve(df['date'], df['PORTFOLIO_VALUE'], df['close'], title='Portfolio Strategy vs '+df['symbol'][0],
                      asset_name=df['symbol'][0])
    metric = analyse_strategy(df)                         # Analyse strategy
    print(metric)
