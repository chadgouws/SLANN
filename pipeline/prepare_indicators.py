import random

import pandas as pd
import numpy as np

import pandas_ta as ta


def prepare_indicators(df):
    # Aroon
    df_aroon = ta.aroon(df['high'], df['low'], length=14, scalar=1)

    # Bollinger Bands
    df_bb = ta.bbands(df['close'], length=20)
    df['bb_ratio'] = df_bb['BBM_20_2.0'] / df_bb['BBL_20_2.0'] - 1
    df['bb_ratio'] = np.where(df['bb_ratio'] > 2, 2, df['bb_ratio'])

    # Simple Moving Average
    # df['sma_1000'] = ict.sma(df['Close'], period=1000)

    # MACD
    # df_macd = ta.macd(df['close'], fast=12, slow=26)
    # df_macd['macd_signal'] = np.where(df_macd['MACD_12_26_9'] > df_macd['MACD_12_26_9'], 1, 0)

    # RSI
    df['rsi_14'] = ta.rsi(df['close'], length=14, scalar=1)
    df['rsi_sma'] = ta.sma(df['rsi_14'], length=14)
    df['rsi_sma_diff'] = df['rsi_14'] - df['rsi_sma']

    # Stochastic
    df_stoch = ta.stoch(df['high'], df['low'], df['close'], k=14, d=3, scalar=1)
    # df_stoch['stoch_ind'] = np.where(df_stoch['STOCHk_14_3_3'] >= df_stoch['STOCHd_14_3_3'], 1, 0)

    df['aroon_up'] = df_aroon['AROONU_14']
    df['aroon_dn'] = df_aroon['AROOND_14']
    # df['macd_signal'] = df_macd['macd_signal']
    df['stoch_d'] = df_stoch['STOCHd_14_3_3'] / 100
    return df


def build_period(df):

    # Time mod
    df['date_day'] = df['date'].dt.date
    df['hour'] = df['date'].dt.hour
    df['hour_mod'] = df['hour'] % 4
    df['hour_adj'] = df['hour'] - df['hour_mod']

    # High
    df_high = df[['date_day', 'high', 'hour_adj']]
    df_high = df_high.groupby(by=['date_day', 'hour_adj']).max().reset_index()

    # Low
    df_low = df[['date_day', 'low', 'hour_adj']]
    df_low = df_low.groupby(by=['date_day', 'hour_adj']).min().reset_index()

    # Close
    df_close = df[df['hour_mod'] == 3]
    df_close = df_close[['date_day', 'hour_adj', 'close']]

    # Open
    df = df[df['hour_mod'] == 0]
    df = df[['unix', 'date', 'symbol', 'open', 'volume', 'date_day', 'hour_adj']]

    df = pd.merge(df, df_low, how='inner', on=['date_day', 'hour_adj'])
    df = pd.merge(df, df_high, how='inner', on=['date_day', 'hour_adj'])
    df = pd.merge(df, df_close, how='inner', on=['date_day', 'hour_adj'])

    return df[['unix', 'date', 'symbol', 'open', 'high', 'low', 'close', 'volume']]


if __name__ == '__main__':

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price/Gemini_BTCUSD_1hr.csv', header=0)
    df = df.sort_values(by=['date']).reset_index(drop=True)
    df = df.iloc[54000:]
    df['date'] = pd.to_datetime(df['date'])
    build_period(df)

    # df = prepare_indicators(df)
    # print(df)
