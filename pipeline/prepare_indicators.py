import random

import pandas as pd
import numpy as np

from indicators import indicators as ict


def prepare_indicators(df):
    # Aroon
    df['aroon_up_300'], df['aroon_dn_300'] = ict.aroon(df['High'], df['Low'], period=300)
    # df['aroon_1000'] = ict.aroon(df['High'], df['Low'], period=1000)

    # Bollinger Bands
    df['bb_sma'], df['bolu'], df['bold'] = ict.bollinger_bands(df['Close'], period=8)
    df['bb_ratio'] = df['bb_sma'] / df['bold'] - 1

    # Simple Moving Average
    # df['sma_1000'] = ict.sma(df['Close'], period=1000)
    # df['sma_ratio_1000'] = df['Close'] / df['sma_ratio_1000']
    df['sma_350'] = ict.sma(df['Close'], period=350)
    df['sma_ratio_350'] = df['Close'] / df['sma_350'] - 1

    df['sma_400'] = ict.sma(df['Close'], period=400)
    df['price_ind_400'] = np.where(df['Close'] > df['sma_400'], 1, 0)
    df['sma_750'] = ict.sma(df['Close'], period=750)
    df['price_ind_750'] = np.where(df['Close'] > df['sma_750'], 1, 0)

    # MACD
    df['macd'], df['signal'], df['cd'] = ict.macd(df['Close'], fast=300, slow=648)
    df['macd_signal'] = np.where(df['macd'] > df['signal'], 1, 0)

    # RSI
    df['rsi_400'] = ict.rsi(df['Close'], period=400)
    df['rsi_900'] = ict.rsi(df['Close'], period=900)

    # Stochastic
    df['k'], df['d'] = ict.stochastic(df['Close'], df['High'], df['Low'], period=420)
    df['stoch_ind'] = np.where(df['k'] >= df['d'], 1, 0)

    # ADX
    df['adx'] = ict.adx(df['Close'], df['High'], df['Low'], period=190)

    # Max and min % change
    df['return'] = df['Close'] / df['Close'].shift(1) - 1
    df['max_return'] = df['return'].rolling(900).max()
    df['min_return'] = df['return'].rolling(900).min()
    return df


if __name__ == '__main__':
    pass
