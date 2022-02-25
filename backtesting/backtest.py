import copy
import random

import pandas as pd
import numpy as np

from portfolio.portfolio import Portfolio
from pipeline.prepare_indicators import prepare_indicators
from algorithm.model import TestModel
from analysis.strategy import prepare_trades


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

    portfolio.asset_amt['BTCUSD'] = 0.0

    trades = []
    for index, row in df.iterrows():
        # print(row.values)
        output = model.feedforward()                                              # Model calc and output
        price = {row['Symbol']: row['Close']}
        portfolio.update_prices(price=price)
        portfolio.update_portfolio()
        portfolio.get_order_type(output, token=row['Symbol'])
        portfolio.trade_pair(row['Symbol'])
        portfolio.update_portfolio()

        trades.append([portfolio.order_type, portfolio.trade_amt, portfolio.asset_amt['cash'],
                       portfolio.asset_amt[row['Symbol']], portfolio.asset_values[row['Symbol']]])

    df_trades = pd.DataFrame(trades, columns=['TRADE', 'TRADE_AMT', 'CASH', 'ASSET_AMT', 'ASSET_VALUE'])
    df_all = df.copy()
    df_all = pd.merge(df_all, df_trades, left_index=True, right_index=True)
    # df_all['TRADE_AMT'] = 0.999 * df_all['TRADE_AMT']
    return df_all


if __name__ == '__main__':

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    periods = 2000
    iterations = 1

    # Iterate through learning process
    for i in range(iterations):
        # select data for back testing
        df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/gemini_BTCUSD_1hr.csv', header=0)

        rows = len(df['Close'].to_list())
        start = random.randint(0, rows - periods)

        df = df[start:start + periods]
        df = df.sort_values(by=['Date'])

        # prepare data and calculate indicators
        df = prepare_indicators(df)

        df = df.dropna()
        df = df.drop(['Unix Timestamp', 'Open', 'High', 'Low', 'Volume'], axis=1)
        df = df.reset_index(drop=True)

        # Prepare models for backtesting
        parent = TestModel()
        child = TestModel()

        # Back test each and compare performance
        df_parent = back_test(df, parent, cash_initial=100000)                    # Back test parent strategy
        df_parent = df_parent.drop(labels=['bb_ratio', 'rsi_500', 'aroon_up', 'aroon_dn', 'macd_signal', 'stoch_d'],
                                   axis=1)
        print(df_parent)

        # Label trades for analysis
        df_parent = prepare_trades(df_parent)
        print(df_parent.head(50))


        # super_metric_parent = stg.analyse_strategy(df_parent)                   # Analyze parent strategy
        #
        # df_child = back_test(df, child)                                         # Back test child strategy
        # super_metric_child = stg.analyse_strategy(df_parent)                    # Analyze child strategy
        #
        # # Check metrics to determine which strategy was better - set new parent
        # if super_metric_child >= super_metric_parent:
        #     parent = copy.deepcopy(child)
        #
        # print('Super metric: ', super_metric_parent)
