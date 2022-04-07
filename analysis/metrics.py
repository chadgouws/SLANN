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


def loser_roi_average(trade_number, trade_seq, trade_net_value, asset_value):
    """
    Calculate the average loss taken on a single losing trade
    :param trade_number:
    :param trade_seq:
    :param trade_net_value:
    :param asset_value:
    :return:
    """
    data = {'TRADE_NR': trade_number, 'TRADE': trade_seq, 'TRADE_NET_VALUE': trade_net_value, 'ASSET_VALUE': asset_value}
    df = pd.DataFrame(data)
    trades = set(df['TRADE_NR'])

    roi = []
    for i in trades:
        df_calc = df[df['TRADE_NR'] == i]
        value, cost = trade_value_cost(df_calc['TRADE'], df_calc['TRADE_NET_VALUE'], df_calc['ASSET_VALUE'])
        if value - cost <= 0:
            roi.append((value - cost) / cost)

    if len(roi) > 0:
        return np.mean(roi)
    else:
        return 0


def loser_roi_max(trade_number, trade_seq, trade_net_value, asset_value):
    """
    Calculate the maximum loss taken on a single losing trade
    :param trade_number:
    :param trade_seq:
    :param trade_net_value:
    :param asset_value:
    :return:
    """
    data = {'TRADE_NR': trade_number, 'TRADE': trade_seq, 'TRADE_NET_VALUE': trade_net_value, 'ASSET_VALUE': asset_value}
    df = pd.DataFrame(data)
    trades = set(df['TRADE_NR'])

    roi = []
    for i in trades:
        df_calc = df[df['TRADE_NR'] == i]
        value, cost = trade_value_cost(df_calc['TRADE'], df_calc['TRADE_NET_VALUE'], df_calc['ASSET_VALUE'])
        if value - cost <= 0:
            roi.append((value - cost) / cost)

    if len(roi) > 0:
        return min(roi)
    else:
        return 0


def max_drawdown(portfolio_value):
    """
    Maximum drawdown is the greatest distance, or loss, from a previous equity peak.
    :param df:
    :return:
    """
    portfolio_value = pd.Series(portfolio_value)
    peak = max(portfolio_value)
    peak_index = portfolio_value.idxmax()
    portfolio_value = portfolio_value[portfolio_value.index >= peak_index]
    trough = min(portfolio_value)

    return (trough - peak) / peak


def no_of_trades(trade_nr):
    """
    Allocates points based on the number of trades made
    :param trade_nr:
    :return:
    """
    trade_nr = set(trade_nr)
    return len(trade_nr)


def profit_factor(trade_number, trade_seq, trade_net_value, asset_value):
    """
    Calculates as the gross profit divided by the gross loss for the trading period, inclusive of fees.
    This metric relates the amount of profit per unit of risk, with values greater than one indicating
    a profitable system.
    :param df:
    :return:
    """
    data = {'TRADE_NR': trade_number, 'TRADE': trade_seq, 'TRADE_NET_VALUE': trade_net_value,
            'ASSET_VALUE': asset_value}
    df = pd.DataFrame(data)
    trades = set(df['TRADE_NR'])

    gross_profit = 0
    gross_loss = 0
    for i in trades:
        df_calc = df[df['TRADE_NR'] == i]
        value, cost = trade_value_cost(df_calc['TRADE'], df_calc['TRADE_NET_VALUE'], df_calc['ASSET_VALUE'])
        trade_return = value - cost
        if trade_return > 0:
            gross_profit += trade_return
        else:
            gross_loss -= trade_return

    return gross_profit / gross_loss


def roi(seq):
    """
    Calculates Return on Investment: final capital subtracted from initial capital divided by initial capital
    :param seq:
    :return:
    """
    if isinstance(seq, pd.Series):
        seq = list(seq.to_numpy())

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


def trade_value_cost(trade_seq, trade_net_value, asset_value):
    """
    Calculates the current value of a trade and the cost of the trade
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

    trades = list(df['TRADE'])
    if trades[0] == 'BUY':
        existing_cost = df['ASSET_VALUE'].iloc[0] - 0.999 * df['TRADE_NET_VALUE'].iloc[0]
    elif trades[0] == 'SELL':
        existing_cost = df['ASSET_VALUE'].iloc[0] + df['TRADE_NET_VALUE'].iloc[0] / 0.999
    elif trades[0] == 'HOLD':
        existing_cost = df['ASSET_VALUE'].iloc[0]
    else:
        existing_cost = 0.0

    trade_net_value_total = df.groupby(['TRADE']).sum()

    if 'BUY' in trades:
        buy_cost = trade_net_value_total.loc['BUY', 'TRADE_NET_VALUE']
    else:
        buy_cost = 0

    if 'SELL' in trades:
        cash = trade_net_value_total.loc['SELL', 'TRADE_NET_VALUE']
    else:
        cash = 0

    cost = buy_cost + existing_cost / 0.999
    # print(cost)
    if cost == 0.0:
        return None

    current_value = df['ASSET_VALUE'].iloc[-1] + cash
    return current_value, cost


def winner_roi_average(trade_number, trade_seq, trade_net_value, asset_value):
    """
    Calculate the average win taken on a single winning trade
    :param trade_number:
    :param trade_seq:
    :param trade_net_value:
    :param asset_value:
    :return:
    """
    data = {'TRADE_NR': trade_number, 'TRADE': trade_seq, 'TRADE_NET_VALUE': trade_net_value, 'ASSET_VALUE': asset_value}
    df = pd.DataFrame(data)
    trades = set(df['TRADE_NR'])

    roi = []
    for i in trades:
        df_calc = df[df['TRADE_NR'] == i]
        value, cost = trade_value_cost(df_calc['TRADE'], df_calc['TRADE_NET_VALUE'], df_calc['ASSET_VALUE'])
        if value - cost > 0:
            roi.append((value - cost) / cost)

    if len(roi) > 0:
        return np.mean(roi)
    else:
        return 0


def winner_roi_max(trade_number, trade_seq, trade_net_value, asset_value):
    """
    Calculate the max win taken on a single winning trade
    :param trade_number:
    :param trade_seq:
    :param trade_net_value:
    :param asset_value:
    :return:
    """
    data = {'TRADE_NR': trade_number, 'TRADE': trade_seq, 'TRADE_NET_VALUE': trade_net_value, 'ASSET_VALUE': asset_value}
    df = pd.DataFrame(data)
    trades = set(df['TRADE_NR'])

    roi = []
    for i in trades:
        df_calc = df[df['TRADE_NR'] == i]
        value, cost = trade_value_cost(df_calc['TRADE'], df_calc['TRADE_NET_VALUE'], df_calc['ASSET_VALUE'])
        if value - cost > 0:
            roi.append((value - cost) / cost)

    if len(roi) > 0:
        return max(roi)
    else:
        return 0


def win_ratio(trade_number, trade_seq, trade_net_value, asset_value):
    """
    Calculate the win ratio of all trades in a given timeframe
    :param trade_number:
    :param trade_seq:
    :param trade_net_value:
    :param asset_value:
    :return:
    """
    data = {'TRADE_NR': trade_number, 'TRADE': trade_seq, 'TRADE_NET_VALUE': trade_net_value, 'ASSET_VALUE': asset_value}
    df = pd.DataFrame(data)
    trades = set(df['TRADE_NR'])

    winner = []
    for i in trades:
        df_calc = df[df['TRADE_NR'] == i]
        value, cost = trade_value_cost(df_calc['TRADE'], df_calc['TRADE_NET_VALUE'], df_calc['ASSET_VALUE'])
        if value - cost > 0:
            winner.append((value - cost) / cost)

    if len(winner) > 0:
        return len(winner) / len(trades)
    else:
        return 0.0


if __name__ == '__main__':
    a = 1

    df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/other/indicator_testing.csv', header=0)
    df['action'] = np.random.randint(0, 2, df.shape[0])
    cash = [1000] + [0] * 60
    df.to_csv('C:/Users/chadg/GARD/Projects/slann/data/other/indicator_testing_buy_sell.csv', index=False)
    print(df)

