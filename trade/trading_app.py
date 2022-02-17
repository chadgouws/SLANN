import time
import os
import csv

from luno_python.client import Client
from dotenv import load_dotenv
import pandas as pd
import numpy as np

from pipeline import prepare_data as prep


load_dotenv()


def read_nn_from_file(file_path):
    return np.genfromtxt('C:/Users/chadg/GARD/Projects/slann/' + file_path, delimiter=',')


def append_list_to_df(df, list_of_list):
    df_2 = pd.DataFrame(list_of_list, columns=list(df))
    return df_2.append(df, ignore_index=True)


def append_current_price_to_previous(price, df):
    return np.append([price], df['price'].values)


def get_bid_price(ticker):
    return float(ticker['bid'])


def calculate_perc_change(df):
    df_price = df['price']
    df['perc'] = 100 * (df_price / df_price.shift(-1) - 1)
    df = df.dropna()
    return df['perc']


def write_dict_to_file(data_dict, csv_file):
    with open(csv_file, mode='a', newline='') as f:
        fieldnames = ['pair', 'timestamp', 'bid', 'ask', 'last_trade', 'rolling_24_hour_volume', 'status', 'type']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow(data_dict)


def write_df_to_file(df, csv_file, rows=None):
    if rows is None:
        df.to_csv(csv_file, index=False)
    elif len(df.index) < rows:
        df.iloc[:len(df.index)].to_csv(csv_file, index=False)
    else:
        df.iloc[:rows].to_csv(csv_file, index=False)


class TradeLuno:

    def __init__(self):
        self.key_id = ''
        self.secret_key = ''
        self.conn = ''
        self.current_price = {'XBTZAR': 0,
                              'ETHZAR': 0,
                              }
        self.buy = 'BUY'
        self.sell = 'SELL'
        self.none = 'NONE'
        self.type = 'NONE'
        self.ticker_symbol = ['XBTZAR', 'ETHZAR']
        self.wallets = ['ZAR', 'XBT', 'ETH']
        self.account_id = {'ZAR': 8603911505957323427,
                           'XBTZAR': 2461204772888778137,
                           'ETHZAR': 5852488882750608294,
                           }
        self.curr = {'ZAR': '0',
                     'XBTZAR': '0',
                     'ETHZAR': '0',
                     }
        self.price_files = {'XBTZAR': 'C:/Users/chadg/GARD/Projects/slann/data/prod_prices/XBTZAR.csv',
                            'ETHZAR': 'C:/Users/chadg/GARD/Projects/slann/data/prod_prices/ETHZAR.csv',
                            }
        self.trade_perc = 0.35
        self.set_key_id()
        self.set_secret_key()
        self.set_connection()

    def set_key_id(self):
        self.key_id = str(os.getenv('KEY_ID'))

    def set_secret_key(self):
        self.secret_key = str(os.getenv('SECRET_KEY'))

    def set_connection(self):
        self.conn = Client(api_key_id=self.key_id, api_key_secret=self.secret_key)

    def get_ticker(self, ticker_symbol):
        try:
            ticker = self.conn.get_ticker(pair=ticker_symbol)
        except Exception as e:
            ticker = {'pair': ticker_symbol, 'timestamp': 000000, 'bid': '-1', 'ask': '-1',
                      'last_trade': '-1', 'rolling_24_hour_volume': '-1', 'status': 'API FAIL'}
        return ticker

    def get_tickers(self):
        try:
            tickers = self.conn.get_tickers()
        except Exception as e:
            tickers = {}
        return tickers

    def get_balance(self):
        try:
            balance = self.conn.get_balances(self.wallets)
        except Exception as e:
            balance = {'balance': [{'balance': '0'}, {'balance': '0'}, {'balance': '0'}]}

        self.curr['ZAR'] = balance['balance'][2]['balance']
        self.curr['XBTZAR'] = balance['balance'][0]['balance']
        self.curr['ETHZAR'] = balance['balance'][1]['balance']

    def _post_buy_order(self, pair, type, account_id):
        amount = round(self.trade_perc * float(self.curr['ZAR']), 1)
        # btc_amount = amount / float(self.current_price[pair])
        # if btc_amount > 0.00053:
        #     amount = amount
        # else:
        #     amount = round(0.000525 * float(self.current_price[pair]), 1)
        try:
            self.conn.post_market_order(pair=pair, type=type,
                                        counter_volume=amount,
                                        counter_account_id=account_id)
        except Exception as e:
            print(e)

    def _post_sell_order(self, pair, type, account_id):
        try:
            self.conn.post_market_order(pair=pair, type=type,
                                        base_volume=str(float(self.curr[pair]) - 0.000001)[:8],
                                        base_account_id=account_id)
        except Exception as e:
            print(e)

    def order_type(self, algo_output):
        if algo_output > 0.7:
            self.type = self.buy
        elif algo_output < 0.3:
            self.type = self.sell
        else:
            self.type = self.none

        self.type = self.sell

    def trade_currency_pair(self, pair):
        btc_zar_funds = float(self.curr['ZAR']) / self.current_price[pair]
        if self.type == 'BUY' and btc_zar_funds > 0.00054:
            self._post_buy_order(pair, self.type, self.account_id[pair])
        elif self.type == 'SELL':
            self._post_sell_order(pair, self.type, self.account_id['ZAR'])
        else:
            pass

    def post_limit_order(self):
        pass


def sigmoid(x):
    x[x < -14] = -14
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


class NeuralNetwork:

    def __init__(self):
        self.input_size = 30
        self.layer_1_size = 35
        self.layer_2_size = 25
        self.output_size = 1
        self.weights1 = self._set_nn(weight=1, init=False)
        self.weights2 = self._set_nn(weight=2, init=False)
        self.weights3 = self._set_nn(weight=3, init=False)

    def feedforward(self, input):
        self.layer1 = sigmoid(np.dot(input, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        return sigmoid(np.dot(self.layer2, self.weights3))

    def backprop(self, input, output, y):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights3 = np.dot(self.layer2.T, (2*(y - output) * sigmoid_derivative(output)))
        d_weights2 = np.dot(self.layer1.T, (2*(y - output) * sigmoid_derivative(output)))
        d_weights1 = np.dot(input.T,  (np.dot(2*(y - output) * sigmoid_derivative(output),
                                              self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def mutate(self):
        mutation_1 = np.random.rand(self.input_size, self.layer_1_size) - np.random.rand(self.input_size, self.layer_1_size)
        indicator_11 = np.random.randint(0, 2, (self.input_size, self.layer_1_size))
        indicator_12 = np.random.randint(0, 2, (self.input_size, self.layer_1_size))
        self.weights1 = indicator_11 * indicator_12 * mutation_1 + self.weights1

        mutation_2 = np.random.rand(self.layer_1_size, self.layer_2_size) - np.random.rand(self.layer_1_size, self.layer_2_size)
        indicator_21 = np.random.randint(0, 2, (self.layer_1_size, self.layer_2_size))
        indicator_22 = np.random.randint(0, 2, (self.layer_1_size, self.layer_2_size))
        self.weights2 = indicator_21 * indicator_22 * mutation_2 + self.weights2

        mutation_3 = np.random.rand(self.layer_2_size, self.output_size) - np.random.rand(self.layer_2_size, self.output_size)
        indicator_31 = np.random.randint(0, 2, (self.layer_2_size, self.output_size))
        indicator_32 = np.random.randint(0, 2, (self.layer_2_size, self.output_size))
        self.weights3 = indicator_31 * indicator_32 * mutation_3 + self.weights3

    def _set_nn(self, weight=-1, init=False):
        if weight == 1:
            if init:
                w = np.random.rand(self.input_size, self.layer_1_size) - np.random.rand(self.input_size, self.layer_1_size)
            else:
                w = read_nn_from_file('data/nn_architecture/SMGANN_1000_research_W1_2021-05-21T10-48-09.csv')
        elif weight == 2:
            if init:
                w = np.random.rand(self.layer_1_size, self.layer_2_size) - np.random.rand(self.layer_1_size, self.layer_2_size)
            else:
                w = read_nn_from_file('data/nn_architecture/SMGANN_1000_research_W2_2021-05-21T10-48-09.csv')
        elif weight == 3:
            if init:
                w = np.random.rand(self.layer_2_size, self.output_size) - np.random.rand(self.layer_2_size, self.output_size)
            else:
                w = read_nn_from_file('data/nn_architecture/SMGANN_1000_research_W3_2021-05-21T10-48-09.csv')
                w = w.reshape((25, 1))
        else:
            pass

        return w


api_file = 'C:/Users/chadg/GARD/Projects/slann/data/SMGANN/test_luno.csv'          # 'repositories/kauta_web_app/data/test_luno.csv'


def main_nn(currency_pairs):
    tl = TradeLuno()
    nn = NeuralNetwork()                                                        # Initialize Neural Net

    #tl.get_balance()                                                            # Get account balance from API
    df = prep.get_calc_data()
    df = df[['Symbol', 'Close', 'date']]
    df_price = df['Close']
    df['perc'] = 100 * (df_price / df_price.shift(-1) - 1)
    df = df.dropna()
    print(df)
    for pair in currency_pairs:
        # df = pd.read_csv(tl.price_files[pair], header=0)                        # Read price data from file
        # Get ticker data from API
        # ticker = tl.get_ticker(pair)
        tl.current_price[pair] = get_bid_price(ticker)
        # Check if API failed - if it fails, pause process for 60s then call API again
        if tl.current_price == -1.0:
            time.sleep(60)
            ticker = tl.get_ticker(pair)
            price_bid = get_bid_price(ticker)
            if price_bid == -1.0:
                continue
        df_prices = append_list_to_df(df, [[tl.current_price[pair]]])      # Append current price to previous
        df_perc = calculate_perc_change(df_prices)                         # Prepare data into perc
        output = nn.feedforward(df_perc.values.reshape(1, 30))                  # NN makes market prediction: 0-1
        tl.order_type(output[0][0])                                             # Order type BUY/SELL
        # tl.trade_currency_pair(pair)                                            # Post SELL/BUY order to API
        # Write process to file
        df_2 = append_list_to_df(df, [[tl.current_price[pair]]])
        write_df_to_file(df_2, tl.price_files[pair], rows=30)
        ticker['type'] = tl.type
        write_dict_to_file(ticker, api_file)


if __name__ == '__main__':
    currency_pairs = ['XBTZAR']                                                 #, 'ETHZAR'
    main_nn(currency_pairs)
