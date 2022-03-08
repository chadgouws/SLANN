import numpy as np
import pandas as pd

from analysis import metrics as mtx


def prepare_trades(df):
    df = df.copy()

    # Remove trades that nothing is bought or sold
    df['TRADE_NET_VALUE'] = np.where(df['TRADE'] == 'SELL', df['Close']*0.999*df['TRADE_AMT'], df['TRADE_AMT'])

    # Calculate portfolio's value ($)
    df['PORTFOLIO_VALUE'] = df['CASH'] + df['ASSET_VALUE']

    # Give each trade a number (Trade must must have been opened)
    df['ind'] = np.where((df['TRADE'] == 'BUY') & (df['ASSET_VALUE'].shift(1) == 0.0), 1, 0)
    df['TRADE_NR'] = df['ind'].cumsum()

    df['CHECK'] = df.groupby(['TRADE_NR'])['TRADE_NET_VALUE'].transform('mean')
    df = df[df['CHECK'] != 0.0]

    df = df.drop(columns=['ind', 'CHECK'], axis=1)
    return df


def analyse_strategy(df, roi=0.3, win_ratio=0.2, winner_roi_avg=0.1, loser_roi_avg=0.1, winner_roi_max=0.05,
                     loser_roi_max=0.25):
    super_metric_ = roi + win_ratio + winner_roi_avg + loser_roi_avg + winner_roi_max + loser_roi_max
    if super_metric_ == 1.0:
        df = prepare_trades(df)

        roi_ = mtx.roi(df['PORTFOLIO_VALUE'])
        win_ratio_ = mtx.win_ratio(df['TRADE_NR'], df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        winner_roi_avg_ = mtx.winner_roi_average(df['TRADE_NR'], df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        loser_roi_avg_ = mtx.loser_roi_average(df['TRADE_NR'], df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        winner_roi_max_ = mtx.winner_roi_max(df['TRADE_NR'], df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        loser_roi_max_ = mtx.loser_roi_max(df['TRADE_NR'], df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])

        super_metric = roi*roi_ + win_ratio*win_ratio_ + winner_roi_avg*winner_roi_avg_ + \
                       loser_roi_avg*loser_roi_avg_ + winner_roi_max*winner_roi_max_ + loser_roi_max*loser_roi_max_
        return {'SUPER_METRIC': super_metric, 'ROI': roi_, 'WIN_RATIO': win_ratio_, 'WINNER_ROI_AVG': winner_roi_avg_,
                'LOSER_ROI_AVG': loser_roi_avg_, 'WINNER_ROI_MAX': winner_roi_max_, 'LOSER_ROI_MAX': loser_roi_max_}

    else:
        print('SUM OF SUPER METRIC WEIGHTS EQUALS %f (MUST EQUAL 1.0)' % super_metric_)
