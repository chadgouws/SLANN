import datetime
from pathlib import Path

import pandas as pd


def reset_data():
    dir = Path(__file__).resolve().parent.parent
    df = pd.read_csv(str(dir) + '/data/price_ticker/real/gemini_BTCUSD_1hr.csv', )

    df = df.drop(['Unix Timestamp', 'Volume', 'Open', 'High', 'Low', 'Symbol'], axis=1)
    df['date'] = pd.to_datetime(df['Date'])
    df = df[df['date'] >= datetime.datetime(2017, 1, 1)]
    print(df)
    # df = df[df['date'] <= datetime.datetime(2018, 12, 31)]
    df['perc'] = df['Close'] * 100 / 972.00 - 100
    df = df[df['date'].dt.hour == 0]
    df = df.drop(['date', 'Close'], axis=1)
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    df.to_csv('bitoin_perf_01012020-12102021.csv')
    print(df)


if __name__ == '__main__':
    reset_data()