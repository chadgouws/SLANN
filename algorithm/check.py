import pandas as pd
import numpy as np

from indicators import indicators as ict


def ema(close, period=12):
    """
    Returns the Exponential Moving Average (EMA) for the given period, which is a weighted moving average that
    gives a higher weighting to more recent prices.
    :param df:
    :param period:
    :return:
    """
    return close.ewm(span=period, min_periods=period).mean()


data_1 = {'Close': [8797.25, 8849.53, 8912.38, 8998.84, 8885.35],
          'High': [8809.79, 8868.30, 8912.38, 9070.65, 9033.33],
          'Low': [8756.70, 8774.73, 8827.30, 8880.68, 8824.10],
          }
df_1 = pd.DataFrame(data_1)


def test_one():
    df = pd.DataFrame()
    a = ict.aroon(df_1['High'], df_1['Low'], period=2)
    df['aroon_up'] = a['aroon_up']
    df['aroon_down']
    print(df)


if __name__ == '__main__':
    mutation_2 = np.random.rand(3, 3)
    print(mutation_2)
    indicator_21 = np.random.randint(-1, 2, (3, 3))
    print(indicator_21)
    indicator_22 = np.random.randint(-1, 2, (3, 3))
    print(indicator_22)
    weights2 = indicator_21 * indicator_22 * mutation_2
    print(weights2)
