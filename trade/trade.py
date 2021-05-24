import time

import pandas as pd

from pipeline import prepare_data as prep
from pipeline.trader import LunoPortfolio
from pipeline.luno_api import TradeLuno

from algorithm.NN import NeuralNetwork


tl = TradeLuno()

api_file = 'C:/Users/chadg/GARD/Projects/slann/data/test_luno.csv'


def main_nn(currency_pairs):
    # Intialize classes
    nn = NeuralNetwork()

    tl.get_balance()                                                            # Get account balance

    for pair in currency_pairs:
        df = pd.read_csv(tl.price_files[pair], header=0)                 # Read price data from file
        # Get ticker data from API
        ticker = tl.get_ticker(pair)
        price_bid = prep.get_bid_price(ticker)
        # Check if API failed - if it fails, call API again
        if price_bid == -1.0:
            ticker = tl.get_ticker(pair)
            price_bid = prep.get_bid_price(ticker)
            if price_bid == -1.0:
                continue
        df_prices = prep.append_list_to_df(df, [[price_bid]])                   # Append current price to previous
        df_perc = prep.calculate_perc_change(df_prices)                         # Prepare data into perc
        output = nn.feedforward(df_perc.values.reshape(1, 30))                  # NN makes market prediction: 0-1
        tl.order_type(output[0][0])                                             # Order type BUY/SELL
        # tl.trade_currency_pair(pair)                                            # Post SELL/BUY order to API
        # Write process to file
        df_2 = prep.append_list_to_df(df, [[price_bid]])
        prep.write_df_to_file(df_2, tl.price_files[pair], rows=30)
        ticker['type'] = tl.type
        prep.write_dict_to_file(ticker, api_file)


def main_algo():
    lp = LunoPortfolio()

    trade_file = 'C:/Users/chadg/GARD/Projects/slann/data/test_luno_btc.csv'
    pair = 'XBTZAR'

    while True:
        # get data
        df = prep.read_df_from_file(trade_file)
        tl.get_balance()
        ticker = tl.get_ticker(pair)
        # prepare data
        price_bid = prep.get_bid_price(ticker)
        if price_bid == -1.0:
            print('API FAILED')
            continue
        prices = prep.append_current_price_to_previous(price_bid, df)
        sma_9, sma_26 = prep.get_previous_prices(df)
        type = lp.sma_2(prices, sma_9, sma_26)
        # post order
        tl.trade_currency_pair(pair)
        # write prices to file
        df_2 = prep.append_list_to_df(df, [[price_bid, lp.sma_9, lp.sma_26, type]])
        prep.write_df_to_file(df_2, trade_file, rows=26)
        prep.write_dict_to_file(ticker, api_file)
        print(type, price_bid)
        print(tl.curr)
        time.sleep(60)


if __name__ == '__main__':
    currency_pairs = ['XBTZAR']                                                 #, 'ETHZAR'
    start = time.time()
    main_nn(currency_pairs)
    print(time.time() - start, 'seconds')
