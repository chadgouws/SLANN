import numpy as np
import pandas as pd

from analysis import metrics as mtx


def prepare_trades(df):
    df = df.copy()

    # Remove trades that nothing is bought or sold
    df['TRADE_NET_VALUE'] = np.where(df['TRADE'] == 'SELL', df['close']*0.999*df['TRADE_AMT'], df['TRADE_AMT'])

    # Calculate portfolio's value ($)
    df['PORTFOLIO_VALUE'] = df['CASH'] + df['ASSET_VALUE']

    # Give each trade a number (Trade must must have been opened)
    df['ind'] = np.where((df['TRADE'] == 'BUY') & (df['ASSET_VALUE'].shift(1) == 0.0), 1, 0)
    df['TRADE_NR'] = df['ind'].cumsum()

    df['CHECK'] = df.groupby(['TRADE_NR'])['TRADE_NET_VALUE'].transform('mean')
    df = df[df['CHECK'] != 0.0]

    df = df.reset_index()
    df = df.drop(columns=['ind', 'CHECK'], axis=1)
    return df


def weight_metric(metric, weight, ref=0.0, less_than=True):
    if less_than:
        if metric < ref:
            weight = 0
        else:
            weight = weight
    return weight


def analyse_strategy(df, roi=0.2, win_ratio=0.2, drawdown=0.2, winner_roi_avg=0.05, loser_roi_avg=0.1,
                     winner_roi_max=0.05, loser_roi_max=0.2):
    # Need to consider an improvement: 0.25, 0.15, 0.075, 0.075, 0.05, 0.3 & profit factor = 0.1

    super_metric_ = roi + win_ratio + drawdown + winner_roi_avg + loser_roi_avg + winner_roi_max + loser_roi_max
    if round(super_metric_, 4) == 1.0:
        df = prepare_trades(df)

        roi_ = mtx.roi(df['PORTFOLIO_VALUE'])
        win_ratio_ = mtx.win_ratio(df['TRADE_NR'], df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        winner_roi_avg_ = mtx.winner_roi_average(df['TRADE_NR'], df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        loser_roi_avg_ = mtx.loser_roi_average(df['TRADE_NR'], df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        winner_roi_max_ = mtx.winner_roi_max(df['TRADE_NR'], df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        loser_roi_max_ = mtx.loser_roi_max(df['TRADE_NR'], df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        drawdown_ = mtx.max_drawdown(df['PORTFOLIO_VALUE'])
        no_of_trades = mtx.no_of_trades(df['TRADE_NR'])

        # Set weighting parameters
        if no_of_trades <= 1:
            trades_value = 0.0
        elif no_of_trades == 2:
            trades_value = no_of_trades
        elif no_of_trades == 3:
            trades_value = no_of_trades
        elif no_of_trades == 4:
            trades_value = no_of_trades
        else:
            trades_value = 5

        # win_ratio = weight_metric(win_ratio_, win_ratio, ref=0.6)

        # Std dev of portfolio & asset
        close_normalized = 100 * df['close'] / df['close'].iloc[0]
        portfolio_normalized = 100 * df['PORTFOLIO_VALUE'] / df['PORTFOLIO_VALUE'].iloc[0]

        std_dev_asset = close_normalized.std()
        std_dev_portfolio = portfolio_normalized.std()

        range_asset = close_normalized.max() - close_normalized.min()
        range_portfolio = portfolio_normalized.max() - portfolio_normalized.min()

        roi_asset = mtx.roi(df['close'])

        # Portfolio correlation with asset
        roi_hr_asset = df['close'] / df['close'].shift(1) - 1
        roi_hr_portfolio = df['PORTFOLIO_VALUE'] / df['PORTFOLIO_VALUE'].shift(1) - 1
        df_corr = pd.DataFrame({'ASSET': roi_hr_asset, 'PORTFOLIO': roi_hr_portfolio})
        df_corr = df_corr.corr()
        corr = df_corr.loc['ASSET', 'PORTFOLIO']

        super_metric = trades_value + roi*roi_ + win_ratio*win_ratio_ + drawdown*drawdown_ + \
                       winner_roi_avg*winner_roi_avg_ + loser_roi_avg*loser_roi_avg_ + \
                       winner_roi_max*winner_roi_max_ + loser_roi_max*loser_roi_max_
        return {'SUPER_METRIC': super_metric, 'ROI': roi_, 'WIN_RATIO': win_ratio_, 'MAX_DRAWDOWN': drawdown_,
                'WINNER_ROI_AVG': winner_roi_avg_, 'LOSER_ROI_AVG': loser_roi_avg_, 'WINNER_ROI_MAX': winner_roi_max_,
                'LOSER_ROI_MAX': loser_roi_max_, 'ROI_ASSET': roi_asset, 'STD_DEV_ASSET': std_dev_asset,
                'STD_DEV_PORTFOLIO': std_dev_portfolio, 'RANGE_ASSET': range_asset, 'RANGE_PORTFOLIO': range_portfolio,
                'CORR': corr, 'NO_OF_TRADES': no_of_trades}

    else:
        print('SUM OF SUPER METRIC WEIGHTS EQUALS %f (MUST EQUAL 1.0)' % super_metric_)
