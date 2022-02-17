import pandas as pd
import numpy as np


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


def roi(df):
    """
    Calculates Return on Investment: final capital subtracted from initial capital divided by initial capital
    :param df:
    :return:
    """
    portfolio_value = df['Portfolio Value'].to_list()
    return (portfolio_value[-1] - portfolio_value[0]) / portfolio_value[0]


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


def win_ratio(df):
    """
    Number of winning trades divided by number of winning trades add number of losing trades
    :param df:
    :return:
    """
    df = df[df['Trade'] == 'SELL']
    df = df.dropna()
    wins = df[df['roi'] > 1.0]['roi'].count()
    losses = df[df['roi'] <= 1.0]['roi'].count()
    return wins / (wins + losses)


if __name__ == '__main__':
    a = 1

    df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/other/indicator_testing.csv', header=0)
    df['action'] = np.random.randint(0, 2, df.shape[0])
    cash = [1000] + [0] * 60
    df.to_csv('C:/Users/chadg/GARD/Projects/slann/data/other/indicator_testing_buy_sell.csv', index=False)
    print(df)

