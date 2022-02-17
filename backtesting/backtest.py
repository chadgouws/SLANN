import copy

import pandas as pd
import numpy as np

from portfolio.portfolio import Portfolio


def back_test(df, cash_initial=None, buy_weight=None, sell_weight=None):
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

    trades = []
    asset_values = []
    for index, row in df.iterrows():
        # print(row.values)
        output = test_model()  # Model calc and output
        price = {'XBT': row['Close']}
        portfolio.update_prices(price=price)
        portfolio.get_order_type(output)
        portfolio.trade_pair()
        portfolio.update_portfolio()
        trades.append(portfolio.order_type)
        asset_values.append(portfolio.asset_values)

    df = df.copy()
    df['Trade'] = trades
    df_assets = pd.DataFrame(asset_values)
    df = pd.merge(df, df_assets, how='inner', left_index=True, right_index=True)
    # self.df = self.df.drop(labels=['Open', 'High', 'Low', 'Volume'], axis=1)
    df['Portfolio Value'] = df['cash'] + df['XBT'] + df['ETH'] + df['XRP'] + df['LTC'] + df['BCH']
    return df


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

        child = copy.deepcopy(parent)
        child.mutate()

        rows = len(df['Close'].to_list())
        start = random.randint(0, rows - periods)

        df = df[start:start + periods]
        df = df.sort_values(by=['Date'])

        # prepare data and calculate indicators
        df = pi.prepare_indicators(df)

        df = df.dropna()
        print(df)
        df = df.drop(['Unix Timestamp', 'Open', 'High', 'Low', 'Volume', 'bb_sma', 'bolu', 'bold', 'sma_350',
                      'sma_400', 'sma_750', 'macd', 'signal', 'cd', 'return'], axis=1)
        df = df.reset_index(drop=True)
        print(df)

        # prepare ML models 1 & 2

        pft = PortfolioTimeline(df)                                             # Set parent portfolio
        df_parent = pft.backtest(model=parent)                                  # Back test parent strategy
        super_metric_parent = stg.analyse_strategy(df_parent)                   # Analyze parent strategy

        # pft = PortfolioTimeline(df_test)                                        # Set child portfolio
        df_child = pft.backtest(model=child)                                    # Back test child strategy
        super_metric_child = stg.analyse_strategy(df_parent)                    # Analyze child strategy

        if super_metric_child >= super_metric_parent:
            parent = copy.deepcopy(child)

        print('Super metric: ', super_metric_parent)

    # df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/other/indicator_testing.csv', header=0)
