import pandas as pd
import numpy as np

from utils.utils import recent_maximum_index, recent_minimum_index

# Need to investigate whether it is faster to drop unnecessary columns or leave them and carry on with more data


def a_d_line(df, period=9):
    pass


def adx(close, high, low, period=14):
    """
    :param close:
    :param high:
    :param low:
    :param period:
    :return:
    """
    dx = dmi(close, high, low, period=period)
    return ema(dx, com=period)


def aroon(high, low, period=25, scalar=100.0):
    """
    :param high:
    :param low:
    :param period:
    :param scalar:
    :return:
    """
    periods_since_h = high.rolling(period+1).apply(recent_maximum_index)
    periods_since_l = low.rolling(period+1).apply(recent_minimum_index)

    up = scalar * (1 - periods_since_h / period)
    dn = scalar * (1 - periods_since_l / period)
    return up, dn


def atr(close, high, low, period=14):
    """
    Returns the rolling average of True Range (TR) for the given period
    :param df:
    :param period:
    :return:
    """
    tr = true_range(close, high, low)
    return sma(tr, period=period)


def bollinger_bands(close, period=20):
    """
    Returns the 3 lines responsible for Bollinger Bands (BB) for the specified period
    :param df:
    :param period:
    :return:
    """
    sma_ = sma(close, period=period)
    std_ = std(close, period=period)
    return sma_, sma_ + 2 * std_, sma_ - 2 * std_           # sma, bolu, bold


def dmi(close, high, low, period=14):
    """
    Returns the Directional Movement Index (DMI) for the specified period
    :param close:
    :param high:
    :param low:
    :param period:
    :return:
    """
    dip = di_positive(close, high, low, period=period)
    din = di_negative(close, high, low, period=period)
    return abs(dip - din) / abs(dip + din)


def dm_negative(low):
    """
    Returns the Directional Movement (-DM)
    :param df:
    :return:
    """
    return low.shift(1) - low


def dm_positive(high):
    """
    Returns the Directional Movement (+DM)
    :param df:
    :return:
    """
    return high - high.shift(1)


def dm_smooth(dm, period=14):
    dmp_sma = sma(dm, period=period)
    return dmp_sma - dmp_sma / 14 + dm


def di_negative(close, high, low, period=14):
    dmn = dm_negative(low)
    dmn_smooth = dm_smooth(dmn)
    avg_tr = atr(close, high, low, period=period)
    return dmn_smooth / avg_tr


def di_positive(close, high, low, period=14):
    dmp = dm_positive(high)
    dmp_smooth = dm_smooth(dmp)
    avg_tr = atr(close, high, low, period=period)
    return dmp_smooth / avg_tr


def ema(close, span=None, com=None):
    """
    Returns the Exponential Moving Average (EMA) for the given period, which is a weighted moving average that
    gives a higher weighting to more recent prices.
    :param close:
    :param period:
    :param com:
    :param span:
    :return:
    """
    if span:
        # Returns a standard EMA [2 / (n + 1)]
        return close.ewm(span=span, min_periods=span).mean()

    if com:
        # Returns Wilder's EMA [1 / (n + 1)]
        return close.ewm(com=com, min_periods=com).mean()


def macd(close, fast=12, slow=26):
    """
    Returns the Moving Average Convergence Divergence (MACD) for the specified periods
    :param df:
    :param period_1:
    :param period_2:
    :return:
    """
    ema_fast = ema(close, span=fast)
    ema_slow = ema(close, span=slow)
    macd = ema_fast - ema_slow
    signal = ema(macd, span=9)
    cd = macd - signal
    return macd, signal, cd


def obv(df):
    """
    Returns the On Balance Volume (OBV)
    :param df:
    :return:
    """
    df['obv_ind'] = np.where(df['Close'] > df['Close'].shift(1), 1, 0)
    df['obv_ind'] = np.where(df['Close'] < df['Close'].shift(1), -1, df['obv_ind'])
    df['Volume'] = df['Volume'] * df['obv_ind']
    df['obv'] = df['Volume'].cumsum()
    return df.drop(['obv_ind'], axis=1)


def rsi(close, period=14, scalar=100.0):
    """
    :param close:
    :param period:
    :param scalar:
    :return:
    """
    gain = close.diff(1)
    loss = gain.copy()

    gain[gain < 0] = 0
    loss[loss > 0] = 0

    gain_avg = ema(gain, com=period)
    loss_avg = ema(loss, com=period)

    return scalar * gain_avg / (gain_avg + loss_avg.abs())


def sma(close, period=9):
    """
    Returns the Simple Moving Average (MA) for the given period
    :param df:
    :param period:
    :return:
    """
    return close.rolling(period).mean()


def std(close, period=50):
    """
    Returns the Standard Deviation for the given period
    :param df:
    :param period:
    :return:
    """
    return close.rolling(period).std()


def stochastic(close, high, low, period=14, scalar=100.0):
    """
    Returns the Stochastic Oscillator for the given period
    :param df:
    :param period:
    :return:
    """
    low_ = low.rolling(period).min()
    high_ = high.rolling(period).max()
    k = (close - low_) / (high_ - low_)
    d = sma(k, period=3)
    return k, d


def true_range(close, high, low):
    """
    Returns the True Range (TR) for the current period
    :param df:
    :return:
    """
    hl = high - low
    hc = abs(high - close.shift(1))
    lc = abs(low - close.shift(1))
    df = pd.DataFrame({'hl': hl.values,
                       'hc': hc.values,
                       'lc': lc.values,
                       })
    return df.max(axis=1)


if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/other/indicator_testing.csv', header=0)
    #print(df)

    # df = ma(df)
    # df = std(df)
    # df = stochastic(df)
    # df = rsi(df, gradient=True)
    # df = bollinger_bands(df)
    # df = aroon(df)
    # df = macd(df)
    # # df = obv(df)
    #
    # df['k_d'] = df['k_14'] / df['d_14'] - 1
    # df['k_ind'] = np.where(df['k_14'] < 0.2, 1, 0)
    # df['k_ind'] = np.where(df['k_14'] > 0.8, -1, df['k_ind'])
    # df['macd_sig_ratio'] = df['macd_12_26'] / df['macd_sig_12_26'] - 1
    # df['macd_12_26'] = np.where(df['macd_12_26'] > 0, 1, -1)
    # df['macd_sig_12_26'] = np.where(df['macd_sig_12_26'] > 0, 1, -1)
    # df['macd_conv_12_26'] = np.where(df['macd_conv_12_26'] > 0, 1, -1)
    # df['bb_ind'] = np.where(df['Close'] > df['bolu'], 1, 0)
    # df['bb_ind'] = np.where(df['Close'] < df['bold'], -1, df['bb_ind'])
    # df['bb_ratio'] = df['ma_20'] / df['bold']
    #
    # df['period_return'] = df['Close'] / df['Close'].shift(-20) - 1
    # df = df.drop(['Currency', 'Date', 'Close', 'Open', 'High', 'Low', 'Volume'], axis=1)
    # print(df)
    # print('\n')

    # df = aroon(df)


    print(df)

