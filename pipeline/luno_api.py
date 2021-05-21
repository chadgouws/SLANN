import os

import numpy as np

from luno_python.client import Client


class TradeLuno:

    def __init__(self):
        self.key_id = ''
        self.secret_key = ''
        self.conn = ''
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
        self.trade_perc = 0.9
        self.set_key_id()
        self.set_secret_key()
        self.set_connection()

    def set_key_id(self):
        self.key_id = 'gym8e4r7xs286'

    def set_secret_key(self):
        self.secret_key = 'vyVG9XJiVHjqTQi0Xtw42gpvzQK4DJIRt9BcWJeUFtU'

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
        try:
            self.conn.post_market_order(pair=pair, type=type, counter_volume=450.0,
                                        counter_account_id=account_id)
        except Exception as e:
            print(e)

    def _post_sell_order(self, pair, type, account_id):
        try:
            self.conn.post_market_order(pair=pair, type=type, base_volume=str(float(self.curr[pair]) - 0.000001)[:8],
                                        base_account_id=account_id)
        except Exception as e:
            print(e)

    def trade_currency_pair(self, pair, type):
        if type == 'BUY':
            self._post_buy_order(pair, type, self.account_id[pair])
        elif type == 'SELL':
            self._post_sell_order(pair, type, self.account_id['ZAR'])
        else:
            pass

    def post_limit_order(self):
        pass


if __name__ == '__main__':
    tl = TradeLuno()

    pair = 'XBTZAR'
    type = 'SELL'

    # tl.trade_currency_pair(pair, type)

    ticker = tl.get_ticker(pair)
    print(pair)
    tl.get_balance()
    #tl.trade_currency_pair(pair, type)
