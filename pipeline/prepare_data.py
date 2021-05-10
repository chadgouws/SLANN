import os
import csv
import time
import datetime

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


def write_nn_to_file(nn, algo):
    df = pd.DataFrame([[nn.weights1, nn.weights2]])
    df.to_csv('C:/Users/chadg/GARD/Projects/slann/data/nn_architecture/' +
              algo + '_research_' +
              datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S') + '.csv', index=False, header=False)


def read_df_from_file(csv_file):
    prices = pd.read_csv(csv_file)
    return prices


def read_price_data(research=False):
    if research:
        file_path = 'C:/Users/chadg/GARD/Projects/slann/data/price_ticker/generated/'
    else:
        file_path = 'C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/'

    files = os.listdir(file_path)
    print(files)


def move_prices_to_folder(current, to):
    files = os.listdir(current)
    print(files)
    for file in files:
        df = pd.read_csv(current + file, sep=',')
        df = df.drop(columns=['Date', 'Open', 'High', 'Low'])
        df.to_csv(to + file, sep=',', index=False)


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
    current_loc = 'C:/Users/chadg/GARD/Data/Crypto/'
    to_loc = 'C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/'

    move_prices_to_folder(current_loc, to_loc)
