import datetime

import pandas as pd
from matplotlib import pyplot as plt

from algorithm.NN import NeuralNetwork
from pipeline.trader import ResearchPortfolio
from pipeline import prepare_data as prep


class Crypto5Performance:

    def __init__(self):
        self.capital = 1000
        self.bitcoin_weight = 0.3
        self.ether_weight = 0.25
        self.ripple_weight = 0.2
        self.bitcoin_cash_weight = 0.15
        self.litecoin_weight = 0.1
        self.coin = {'BTC': 0.0,
                     'ETH': 0.0,
                     'XRP': 0.0,
                     'BCH': 0.0,
                     'LTC': 0.0}

    def calculate_performance(self):
        df = self._build_dataset()
        ind = list(df.index)
        dates = []
        value = []
        for i in ind:
            price = df.loc[[i]]
            print(price['date'][i])
            if pd.to_datetime(price['date']).dt.day[i] == 1:
                self._rebalance_fund(price, i)
            else:
                pass
            perc_change = self._calculate_perc_change(price, i)
            print(self.coin)
            print(self.capital)
            print(perc_change)
            print('\n')
            dates.append(price['date'][i])
            value.append(perc_change)

        df = pd.DataFrame({'date': dates,
                           'perc': value
                           })
        df.to_csv('crypto_5_performance.csv')


    def _build_dataset(self):
        files = ['BCH_USD_2018-06-01_2021-07-29-CoinDesk.csv', 'BTC_USD_2013-10-01_2021-07-29-CoinDesk.csv',
                 'ETH_USD_2015-08-09_2021-07-29-CoinDesk.csv', 'LTC_USD_2018-06-01_2021-07-29-CoinDesk.csv',
                 'XRP_USD_2018-06-01_2021-07-29-CoinDesk.csv']

        dir = 'C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/'

        df = pd.read_csv(dir+files[0], header=0)
        df['BCH'] = df['Closing Price (USD)']
        df = df[['Date', 'BCH']]

        df_btc = pd.read_csv(dir+files[1], header=0)
        df_btc['BTC'] = df_btc['Closing Price (USD)']
        df_btc = df_btc[['Date', 'BTC']]

        df_eth = pd.read_csv(dir+files[2], header=0)
        df_eth['ETH'] = df_eth['Closing Price (USD)']
        df_eth = df_eth[['Date', 'ETH']]

        df_ltc = pd.read_csv(dir+files[3], header=0)
        df_ltc['LTC'] = df_ltc['Closing Price (USD)']
        df_ltc = df_ltc[['Date', 'LTC']]

        df_xrp = pd.read_csv(dir+files[4], header=0)
        df_xrp['XRP'] = df_xrp['Closing Price (USD)']
        df_xrp = df_xrp[['Date', 'XRP']]

        df = pd.merge(df, df_btc, how='inner', left_on='Date', right_on='Date')
        df = pd.merge(df, df_eth, how='inner', left_on='Date', right_on='Date')
        df = pd.merge(df, df_ltc, how='inner', left_on='Date', right_on='Date')
        df = pd.merge(df, df_xrp, how='inner', left_on='Date', right_on='Date')

        df['date'] = pd.to_datetime(df['Date'])
        df = df[['date', 'BTC', 'ETH', 'BCH', 'LTC', 'XRP']]
        return df[df['date'] >= datetime.datetime(2020, 1, 1)]

    def _calculate_perc_change(self, price, i):
        capital = self.capital
        self.capital = self.coin['BTC'] * price['BTC'][i] + self.coin['ETH'] * price['ETH'][i] \
                       + self.coin['XRP'] * price['XRP'][i] + self.coin['BCH'] * price['BCH'][i] \
                       + self.coin['LTC'] * price['LTC'][i]
        return self.capital / capital

    def _rebalance_fund(self, price, i):
        self.coin['BTC'] = self.bitcoin_weight * self.capital / price['BTC'][i]
        self.coin['ETH'] = self.ether_weight * self.capital / price['ETH'][i]
        self.coin['XRP'] = self.ripple_weight * self.capital / price['XRP'][i]
        self.coin['BCH'] = self.bitcoin_cash_weight * self.capital / price['BCH'][i]
        self.coin['LTC'] = self.litecoin_weight * self.capital / price['LTC'][i]
        self.capital = self.coin['BTC'] * price['BTC'][i] + self.coin['ETH'] * price['ETH'][i] \
                       + self.coin['XRP'] * price['XRP'][i] + self.coin['BCH'] * price['BCH'][i] \
                       + self.coin['LTC'] * price['LTC'][i]


class NeuroPerformance:

    def __init__(self):
        self.nn = NeuralNetwork()
        self.cash = 0
        self.ether = 0
        self.bitcoin = 0

    def _get_data(self):
        df = prep.get_calc_data()
        df = df[['Symbol', 'Close', 'date']]
        df_price = df['Close']
        df['perc'] = 100 * (df_price / df_price.shift(-1) - 1)
        df = df.dropna()
        return df[['date', 'Close', 'perc']].sort_values(by=['date']).reset_index()

    def calculate(self):
        pd.set_option('display.max_rows', 500)
        df = self._get_data()
        print(df)
        df_date = df['date']
        df_price = df['Close']
        df_perc = df['perc']

        rp = ResearchPortfolio(1)
        df_out = pd.DataFrame([[df_date.loc[28], df_price.loc[28], 1000, 0]], columns=['date', 'price', 'cash', 'coin'])
        for start in range(0, df_perc.shape[0]-29):
            end = start + 29
            input = df_perc.loc[start:end].values.T
            output = self.nn.feedforward(input)
            perc_change = df_price.loc[end] / df_price.loc[start]
            rp.order_type(output, perc_change)
            rp.make_market_order([df_price.loc[end]])
            df_in = pd.DataFrame([[df_date.loc[end], df_price.loc[end], rp.cash[0], rp.coin[0]]],
                                 columns=['date', 'price', 'cash', 'coin'])
            df_out = df_out.append(df_in, ignore_index=True)

        df_out.to_csv('fund_performance.csv')


def show_performance():
    df = pd.read_csv('fund_performance.csv')
    df['capital'] = df['cash'] + df['coin'] * df['price']

    df[['date', 'capital']].to_csv('neuro_alpha_performance.csv', index=False)

    df = df[['date', 'price', 'capital']]
    df['price'] = df['price'] / 0.972

    df['datetime'] = pd.to_datetime(df['date'])
    df = df[df['datetime'] >= datetime.datetime(2017, 1, 1, 0, 0, 0)]
    df = df[df['datetime'].dt.hour == 0]
    df = df.reset_index()
    df['perf'] = df['capital'] / df['capital'].shift(1)
    df[['date', 'perf']].to_csv('neuro_alpha_performance.csv')
    print(df)

    plt.plot(df['datetime'].dt.date, df['capital'])
    plt.plot(df['datetime'].dt.date, df['price'])
    plt.show()


if __name__ == '__main__':
    np = NeuroPerformance()

    np.calculate()
    show_performance()
