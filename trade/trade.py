import time

from pipeline import prepare_data as prep
from pipeline.trader import LunoPortfolio
from pipeline.luno_api import TradeLuno

from algorithm.NN import NeuralNetwork


def main_algo():
    lp = LunoPortfolio()
    tl = TradeLuno()
    trade_file = 'C:/Users/chadg/GARD/Projects/slann/data/test_luno_btc.csv'
    api_file = 'C:/Users/chadg/GARD/Projects/slann/data/test_luno.csv'
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
        tl.trade_currency_pair(pair, type)
        # write prices to file
        df_2 = prep.append_list_to_df(df, [[price_bid, lp.sma_9, lp.sma_26, type]])
        prep.write_df_to_file(df_2, trade_file, rows=26)
        prep.write_dict_to_file(ticker, api_file)
        print(type, price_bid)
        print(tl.curr)
        time.sleep(60)


def main_nn():
    # Intialize classes
    tl = TradeLuno()
    nn = NeuralNetwork()

    currency_pairs = ['XBTZAR', 'ETHZAR']
    # Get account balance
    tl.get_balance()

    for pair in currency_pairs:
        # Read price data from file
        # Read NN info from file

        # Get ticker price
        ticker = tl.get_ticker(pair)
        price_bid = prep.get_bid_price(ticker)
        # Check if API failed
        if price_bid == -1.0:
            print('API FAILED')
            continue               # Consider retrying   [ ticker = tl.get_ticker(pair) ]
        # Prepare data
        # NN output
        output = nn.feedforward(input)
        # Order type
        # Post order
        tl.trade_currency_pair(pair, type)
        # Write process to file


if __name__ == '__main__':
    main_algo()
