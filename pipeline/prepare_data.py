import csv
import time

import numpy as np
import pandas as pd


def write_dict_to_file(data_dict, csv_file):
    with open(csv_file, mode='a', newline='') as f:
        fieldnames = ['pair', 'timestamp', 'bid', 'ask', 'last_trade', 'rolling_24_hour_volume', 'status']
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


def read_df_from_file(csv_file):
    prices = pd.read_csv(csv_file)
    return prices


def append_list_to_df(df, list_of_list):
    df_2 = pd.DataFrame(list_of_list, columns=list(df))
    return df_2.append(df, ignore_index=True)


def append_current_price_to_previous(price, df):
    return np.append([price], df['price'].values)


def get_bid_price(ticker):
    return float(ticker['bid'])


def get_previous_prices(df):
    ma = df.iloc[0]
    return ma['sma 9'], ma['sma 26']


def moving_average(prices, period):
    length = len(prices)
    if period > length:
        avg = np.average(prices[:length])
    else:
        avg = np.average(prices[:period])
    return avg


if __name__ == '__main__':
    file_name = 'C:/Users/chadg/GARD/Projects/slann/data/test_luno_btc.csv'

    for i in range(1, 20):
        # read
        df = read_df_from_file(file_name)
        # get ticker
        ticker = i
        prices = df['price'].values
        prices_new = np.array([ticker])
        prices = np.append(prices_new, prices)
        # make trade decision
        avg_1 = moving_average(prices, 9)
        avg_2 = moving_average(prices, 26)
        #write data
        df_2 = pd.DataFrame([[ticker, avg_1, avg_2]], columns=list(df))
        df_2 = df_2.append(df, ignore_index=True)
        write_df_to_file(df_2, file_name)
        time.sleep(1)
