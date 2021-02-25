import time

from luno_python.client import Client

tickers = ['XBTZAR', 'ETHZAR', 'XRPZAR', 'LTCZAR']


def main(t):

    client = Client(api_key_id='nbrtx6cadg4er', api_key_secret='nZWLPgYS2HjxkALYQ6LBA5xtVEcq5zJ1WtzpWKkJFdk')
    while True:
        try:
            # ticker = client.get_ticker(pair=tick)
            ticker = client.get_tickers()
            with open("luno_data.txt", "a") as f:
                f.write('\n' + str(ticker))
            # print(ticker)
        except Exception as e:
            print(e)

        time.sleep(t)


if __name__ == '__main__':

    t = 9

    main(t)
