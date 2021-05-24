from luno_python.client import Client


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
        self.key_id = 'bjtqvhbw5w9wn'

    def set_secret_key(self):
        self.secret_key = 'B9nVRZePMJI_c5Jq-ukFrcoAYsg7mCDvvyIXnf7cNlg'

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
        btc_amount = amount / float(self.current_price[pair])
        if btc_amount > 0.00053:
            amount = amount
        else:
            amount = round(0.00053 * float(self.current_price[pair]), 1)
        try:
            self.conn.post_market_order(pair=pair, type=type,
                                        counter_volume=amount,
                                        counter_account_id=account_id)
        except Exception as e:
            print(e)

    def _post_sell_order(self, pair, type, account_id):
        try:
            self.conn.post_market_order(pair=pair, type=type, base_volume=str(float(self.curr[pair]) - 0.000001)[:8],
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


if __name__ == '__main__':
    tl = TradeLuno()

    pair = 'XBTZAR'
    type = 'SELL'

    # tl.trade_currency_pair(pair, type)

    ticker = tl.get_ticker(pair)
    print(pair)
    tl.get_balance()
    #tl.trade_currency_pair(pair, type)
