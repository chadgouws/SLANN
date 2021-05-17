import datetime
import time
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import pi
from scipy.special import erf


def pdf(x):
    return 1/np.sqrt(2*pi) * np.exp(-x**2/2)


def cdf(x):
    return (1 + erf(x/np.sqrt(2))) / 2


def skew(x=0, e=0, w=1, a=0):
    t = (x - e) / w
    return 2 / w * pdf(t) * cdf(a*t)
    # You can of course use the scipy.stats.norm versions
    # return 2 * norm.pdf(t) * norm.cdf(a*t)


def normal(x, mu, sigma):
    return (2.*np.pi*sigma**2.)**-.5 * np.exp(-.5 * (x-mu)**2. / sigma**2.)


def read_csv(file):
    file_path = 'C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/' + file
    df = pd.read_csv(file_path)
    return df


def calculate_perc_change(df, exchange='gemini'):
    if exchange == 'gemini':
        df = df.loc[:, ('Unix Timestamp', 'Close')]
        df_close = df['Close']
        df['perc'] = 100 * (df_close / df_close.shift(-1) - 1)
        df = df.dropna()
    elif exchange == 'binance':
        df = df.loc[:, ('unix', 'close')]
        df_close = df['close']
        df['perc'] = 100 * (df_close / df_close.shift(-1) - 1)
        df = df.dropna()
    else:
        pass
    return df


def describe_data(df):
    return df.describe()


if __name__ == '__main__':
    # files = os.listdir('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/')
    # print(files)
    # files_1 = ['gemini_BTCUSD_1hr.csv', 'gemini_ETHUSD_1hr.csv', 'gemini_LTCUSD_1hr.csv', 'gemini_ZECUSD_1hr.csv']
    #
    # for file_name in files_1:
    #     df = read_csv(file_name)
    #     df_perc = calculate_perc_change(df, exchange='gemini')
    #     print(df_perc)
    #     length = len(df_perc.index)
    #
    #     for m in range(-2, 3, 1):
    #         for s in range(1, 4, 1):
    #             df_out = pd.DataFrame(columns=['Unix Timestamp', 'Close', 'perc_final', 'Symbol'])
    #             print(df_out)
    #             for _ in range(0, 10):
    #                 mu = m / 50
    #                 sigma = s / 10
    #                 n = length
    #
    #                 x = np.random.normal(mu, sigma, n)
    #                 df_perc['perc_add'] = x
    #                 df_perc['perc_final'] = df_perc['perc'] + df_perc['perc_add']
    #
    #                 df_adj = df_perc.loc[:, ('Unix Timestamp', 'Close', 'perc_final')]
    #                 df_adj['Symbol'] = [str(mu)[:6] + '~' + str(sigma)] * length
    #                 print('adj')
    #                 print(df_adj)
    #                 df_out = df_out.append(df_adj, ignore_index=True)
    #                 print('out')
    #                 print(df_out)
    #
    #             df_out.to_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/generated/' +
    #                           file_name.split('.')[0] + '_' +
    #                           datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S') + '.csv', sep=',', index=False)
    #             time.sleep(2.5)

    files_2 = ['Binance_ADAUSDT_1h.csv', 'Binance_BNBUSDT_1h.csv', 'Binance_ETCUSDT_1h.csv', 'Binance_LINKUSDT_1h.csv',
               'Binance_NEOUSDT_1h.csv', 'Binance_XLMUSDT_1h.csv', 'Binance_XRPUSDT_1h.csv']

    for file_name in files_2:
        df = read_csv(file_name)
        df_perc = calculate_perc_change(df, exchange='binance')
        print(df_perc)
        length = len(df_perc.index)

        for m in range(-2, 3, 1):
            for s in range(1, 4, 1):
                df_out = pd.DataFrame(columns=['unix', 'close', 'perc_final', 'symbol'])
                print(df_out)
                for _ in range(0, 10):
                    mu = m / 50
                    sigma = s / 10
                    n = length

                    x = np.random.normal(mu, sigma, n)
                    df_perc['perc_add'] = x
                    df_perc['perc_final'] = df_perc['perc'] + df_perc['perc_add']

                    df_adj = df_perc.loc[:, ('unix', 'close', 'perc_final')]
                    df_adj['symbol'] = [str(mu)[:6] + '~' + str(sigma)] * length
                    print('adj')
                    print(df_adj)
                    df_out = df_out.append(df_adj, ignore_index=True)
                    print('out')
                    print(df_out)

                df_out['Unix Timestamp'] = df_out['unix']
                df_out = df_out.drop(labels=['unix'], axis=1)
                df_out.to_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/generated/' +
                              file_name.split('.')[0] + '_' +
                              datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S') + '.csv', sep=',', index=False)
                time.sleep(2.5)
