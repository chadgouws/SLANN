import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from analysis import metrics as mtx
from indicators import indicators as ict


def indicate_trades(df):
    df['different'] = np.where(df['Trade'] == df['Trade'].shift(1), 1, 0)
    return df


def analyse_strategy(df, roi=0.3, win_ratio=0.2, winner_roi_avg=0.05, loser_roi_avg=0.1, winner_roi_max=0.1,
                     loser_roi_max=0.25):
    super_metric_ = roi + win_ratio + winner_roi_avg + loser_roi_avg + winner_roi_max + loser_roi_max
    if super_metric_ == 1.0:
        roi_ = mtx.roi(df)

        df = indicate_trades(df)
        df = df[df['different'] == 0]
        df['roi'] = df['Portfolio Value'] / df['Portfolio Value'].shift(1)

        win_ratio_ = mtx.win_ratio(df)
        winner_roi_avg_ = mtx.winner_roi_average(df)
        loser_roi_avg_ = mtx.loser_roi_average(df)
        winner_roi_max_ = mtx.winner_roi_max(df)
        loser_roi_max_ = mtx.loser_roi_max(df)

        super_metric = roi*roi_ + win_ratio*win_ratio_ + winner_roi_avg*winner_roi_avg_ + \
                       loser_roi_avg*loser_roi_avg_ + winner_roi_max*winner_roi_max_ + loser_roi_max*loser_roi_max_
        return super_metric

    else:
        print('SUM OF SUPER METRIC WEIGHTS EQUALS %f (MUST EQUAL 1.0)' % super_metric_)
