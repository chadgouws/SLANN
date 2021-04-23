import time

from pipeline import prepare_data as prep
from pipeline.trader import LunoPortfolio
from pipeline.luno_api import TradeLuno


lp = LunoPortfolio()
tl = TradeLuno()
trade_file = 'C:/Users/chadg/GARD/Projects/slann/data/test_luno_btc.csv'
api_file = 'C:/Users/chadg/GARD/Projects/slann/data/test_luno.csv'
pair = 'XBTZAR'


def main():
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
        # write prices to file
        df_2 = prep.append_list_to_df(df, [[price_bid, lp.sma_9, lp.sma_26, type]])
        prep.write_df_to_file(df_2, trade_file, rows=26)
        prep.write_dict_to_file(ticker, api_file)
        print(type, price_bid)
        time.sleep(3)


if __name__ == '__main__':
    main()
