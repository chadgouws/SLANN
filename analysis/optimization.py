import datetime

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator

import pandas_ta as ta

from indicators import indicators as ict


def optimize_indicator(df, indicator=None, return_period=24, indicator_period=20):
    return indicator(df, period=indicator_period)


if __name__ == '__main__':

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/gemini_BTCUSD_1hr.csv', header=0)
    df = df.sort_values(by=['Date']).reset_index(drop=True)
    df = df.iloc[10000:]

    corr = []

    grid_size = 1000
    step_size = 10
    start_coordinate = 10
    roi = list(range(start_coordinate, grid_size, step_size))
    period = list(range(start_coordinate, grid_size, step_size))

    for t in roi:
        for p in period:
            help(ta.adx(df['High'], df['Low'], df['Close'], length=p, scalar=1))
            df['adx'] = ta.adx(df['High'], df['Low'], df['Close'], length=p, scalar=1)
            df['return'] = abs(df['Close'].shift(-1*t) / df['Close'] - 1)
            a = df[['adx', 'return']].corr()

            print('\n')
            print('Time:   ', t)
            print('Period: ', p)
            print('Correlation: ', a.iloc[0]['return'])

            corr.append(a.iloc[0]['return'])

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    # Make data.
    X, Y = np.meshgrid(roi, period)
    Z = np.array(corr).reshape([int((grid_size - start_coordinate) / step_size), int((grid_size - start_coordinate) / step_size)])

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(-0.2, 0.3)
    ax.zaxis.set_major_locator(LinearLocator(10))
    # A StrMethodFormatter is used automatically
    ax.zaxis.set_major_formatter('{x:.02f}')

    ax.set_xlabel('Time', fontsize=10, rotation=0)
    ax.set_ylabel('Period', fontsize=10, rotation=0)
    ax.set_zlabel('Correlation', fontsize=10, rotation=0)

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()



