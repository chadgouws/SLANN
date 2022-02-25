import collections

import pandas as pd
import numpy as np

from utils.utils import check_seq_greater_than, check_seq_equal_to


def portfolio_correlation(df):
    """

    :param df:
    :return:
    """


def count_drawdowns(df, period=5, floor=-0.03):
    """

    :param df:
    :param period:
    :param floor:
    :return:
    """


def loser_roi_average(df):
    """

    :param df:
    :return:
    """
    df = df[df['Trade'] == 'SELL']
    df = df.dropna()
    return df[df['roi'] <= 1.0]['roi'].mean() - 1


def loser_roi_max(df):
    """

    :param df:
    :return:
    """
    df = df[df['Trade'] == 'SELL']
    df = df.dropna()
    return df[df['roi'] <= 1.0]['roi'].min() - 1


def max_drawdown(df):
    """

    :param df:
    :return:
    """


def profit_factor(df):
    """

    :param df:
    :return:
    """


def roi(seq):
    """
    Calculates Return on Investment: final capital subtracted from initial capital divided by initial capital
    :param df:
    :return:
    """
    if isinstance(seq, pd.DataFrame):
        sequence = seq.to_numpy()

    try:
        if len(seq) == 0:
            return None
        elif seq[0] == 0:
            return None
        else:
            return (seq[-1] - seq[0]) / seq[0]

    except TypeError:
        print(seq, 'is not iterable')


def trade_open_time():
    pass


def trade_profit_loss(trade_seq, trade_net_value, asset_value):
    """
    Number of winning trades divided by number of winning trades add number of losing trades
    :param trade_seq:
    :param trade_net_value:
    :param asset_value:
    :return:
    """
    if len(list(trade_seq)) > 0:
        pass
    else:
        return None

    if check_seq_greater_than(trade_net_value):
        pass
    else:
        return None

    if check_seq_greater_than(asset_value):
        pass
    else:
        return None

    data = {'TRADE': trade_seq, 'TRADE_NET_VALUE': trade_net_value, 'ASSET_VALUE': asset_value}
    df = pd.DataFrame(data)

    if check_seq_equal_to(df[df['TRADE'] == 'HOLD']['TRADE_NET_VALUE']):
        pass
    else:
        return None

    trade_net_value_total = df.groupby(by=['TRADE']).sum()
    trades = list(df['TRADE'])
    if 'BUY' in trades:
        cost = df['ASSET_VALUE'].iloc[0] - 0.999 * df['TRADE_NET_VALUE'].iloc[0] + \
               trade_net_value_total.loc['BUY', 'TRADE_NET_VALUE']
    else:
        cost = df['ASSET_VALUE'].iloc[0]

    if cost == 0.0:
        return None

    if 'SELL' in trades:
        cash = trade_net_value_total.loc['SELL', 'TRADE_NET_VALUE']
    else:
        cash = 0

    current_value = df['ASSET_VALUE'].iloc[-1] + cash
    return round(current_value - cost, 8)


def winner_roi_average(df):
    """

    :param df:
    :return:
    """
    df = df[df['Trade'] == 'SELL']
    df = df.dropna()
    return df[df['roi'] > 1.0]['roi'].mean() - 1


def winner_roi_max(df):
    """

    :param df:
    :return:
    """
    df = df[df['Trade'] == 'SELL']
    df = df.dropna()
    return df[df['roi'] > 1.0]['roi'].max() - 1


def win_ratio(initial):
    pass


if __name__ == '__main__':
    a = 1

    df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/other/indicator_testing.csv', header=0)
    df['action'] = np.random.randint(0, 2, df.shape[0])
    cash = [1000] + [0] * 60
    df.to_csv('C:/Users/chadg/GARD/Projects/slann/data/other/indicator_testing_buy_sell.csv', index=False)
    print(df)

