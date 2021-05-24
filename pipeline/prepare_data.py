import os
import csv
import random
import datetime

import numpy as np
import pandas as pd


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


def write_nn_to_file(nn, algo, gen=0):
    np.savetxt('C:/Users/chadg/GARD/Projects/slann/data/nn_architecture/' + algo + '_research_W1_' +
               datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S') + '_' + str(gen) + '.csv',
               nn.weights1, delimiter=",")
    np.savetxt('C:/Users/chadg/GARD/Projects/slann/data/nn_architecture/' + algo + '_research_W2_' +
               datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S') + '_' + str(gen) + '.csv',
               nn.weights2, delimiter=",")
    np.savetxt('C:/Users/chadg/GARD/Projects/slann/data/nn_architecture/' + algo + '_research_W3_' +
               datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S') + '_' + str(gen) + '.csv',
               nn.weights3, delimiter=",")


def read_nn_from_file(file_path):
    return np.genfromtxt('C:/Users/chadg/GARD/Projects/slann/data/nn_architecture/' + file_path, delimiter=',')


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


def get_training_data(periods=1000, samples=10):
    file_dir = 'C:/Users/chadg/GARD/Projects/slann/data/price_ticker/generated/'
    files = os.listdir(file_dir)
    df_all = pd.DataFrame(list(range(0, periods)), columns=['row_no'])
    for i in range(0, samples):
        file_no = random.randint(0, len(files)-1)
        file_name = files[file_no]
        df = pd.read_csv(file_dir + file_name)
        df['date'] = pd.to_datetime(df['Unix Timestamp'], unit='ms')
        df = df[df.date < datetime.datetime(2019, 7, 1, 0, 0, 0)]
        perc = df['perc_final'].tolist()
        start = random.randint(0, len(perc)-periods)
        df_all[str(i)] = perc[start:start+periods]

    df_all = df_all.drop(labels=['row_no'], axis=1)
    df_perc = (df_all + 100) / 100
    df_perc = df_perc.cumprod() * 1000
    return df_all, df_perc


def calculate_perc_change(df):
    df_price = df['price']
    df['perc'] = 100 * (df_price / df_price.shift(-1) - 1)
    df = df.dropna()
    return df['perc']


if __name__ == '__main__':
    a = read_nn_from_file()
    df = pd.DataFrame(a)
    print(df)
