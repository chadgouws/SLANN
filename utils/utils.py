import pandas as pd
import numpy as np


def recent_maximum_index(x):
    return int(np.argmax(x[::-1]))


def recent_minimum_index(x):
    return int(np.argmin(x[::-1]))


def set_candle(date, candle=4):
    # Currently this is only set to turn 1 hour candles into 4 hour candles
    hour = date.dt.hour
    df = pd.merge(date, hour, left_index=True, right_index=True)
    df.columns = ['Date', 'hour']
    df['mod'] = df['hour'] % candle
    df['adj'] = np.where(df['mod'] == 1, 3, df['mod'])
    df['adj'] = np.where(df['mod'] == 2, 2, df['adj'])
    df['adj'] = np.where(df['mod'] == 3, 1, df['adj'])
    df['dt'] = pd.to_timedelta(df['Date'])
    df['Date'] = df['Date'] + df['adj']

    print(df)


if __name__ == '__main__':
    df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/gemini_BTCUSD_1hr.csv', header=0)
    df = df.sort_values(by=['Date']).reset_index(drop=True)
    df['Date'] = pd.to_datetime(df['Date'])
    print(df['Date'])

    set_candle(df['Date'])
