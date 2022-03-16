import random

import pandas as pd
import numpy as np

import pandas_ta as ta


def prepare_indicators(df):
    # Aroon
    df_aroon = ta.aroon(df['high'], df['low'], length=300, scalar=1)
    # df['aroon_1000'] = ict.aroon(df['High'], df['Low'], period=1000)

    # Bollinger Bands
    df_bb = ta.bbands(df['close'], length=8)
    df['bb_ratio'] = df_bb['BBM_8_2.0'] / df_bb['BBL_8_2.0'] - 1
    df['bb_ratio'] = np.where(df['bb_ratio'] > 2, 2, df['bb_ratio'])

    # Simple Moving Average
    # df['sma_1000'] = ict.sma(df['Close'], period=1000)
    # df['sma_ratio_1000'] = df['Close'] / df['sma_ratio_1000']
    # df['sma_350'] = ta.sma(df['Close'], length=350)
    # df['sma_ratio_350'] = df['Close'] / df['sma_350'] - 1
    #
    # df['sma_400'] = ta.sma(df['Close'], length=400)
    # df['price_ind_400'] = np.where(df['Close'] > df['sma_400'], 1, 0)
    # df['sma_750'] = ta.sma(df['Close'], length=750)
    # df['price_ind_750'] = np.where(df['Close'] > df['sma_750'], 1, 0)

    # MACD
    df_macd = ta.macd(df['close'], fast=300, slow=648)
    df_macd['macd_signal'] = np.where(df_macd['MACD_300_648_9'] > df_macd['MACDs_300_648_9'], 1, 0)

    # RSI
    df['rsi_500'] = ta.rsi(df['close'], length=500, scalar=1)
    # df['rsi_900'] = ta.rsi(df['Close'], length=900)

    # Stochastic
    df_stoch = ta.stoch(df['high'], df['low'], df['close'], k=420, d=5, scalar=1)
    # df_stoch['stoch_ind'] = np.where(df_stoch['STOCHk_14_3_3'] >= df_stoch['STOCHd_14_3_3'], 1, 0)

    # ADX
    # df['adx'] = ict.adx(df['Close'], df['High'], df['Low'], period=190)

    # Max and min % change
    # df['return'] = df['Close'] / df['Close'].shift(1) - 1
    # df['max_return'] = df['return'].rolling(900).max()
    # df['min_return'] = df['return'].rolling(900).min()

    df['aroon_up'] = df_aroon['AROONU_300']
    df['aroon_dn'] = df_aroon['AROOND_300']
    df['macd_signal'] = df_macd['macd_signal']
    df['stoch_d'] = df_stoch['STOCHd_420_5_3'] / 100
    return df


if __name__ == '__main__':

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/gemini_BTCUSD_1hr.csv', header=0)
    df = df.sort_values(by=['Date']).reset_index(drop=True)
    df = df.iloc[10000:]

    df = prepare_indicators(df)
    print(df)
