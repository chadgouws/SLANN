import os
import random
from datetime import datetime

import pandas as pd

from algorithm import slann


file_dir = 'C:/Users/chadg/GARD/Projects/slann/data/price_ticker/generated/'


def get_training_data():
    files = os.listdir(file_dir)
    df_all = pd.DataFrame(list(range(0, 1000)), columns=['row_no'])
    for i in range(0, 10):
        file_no = random.randint(0, len(files))
        file_name = files[file_no]
        df = pd.read_csv(file_dir + file_name)
        df['date'] = pd.to_datetime(df['Unix Timestamp'], unit='ms')
        df = df[df.date < datetime(2019, 7, 1, 0, 0, 0)]
        perc = df['perc_final'].tolist()
        start = random.randint(0, len(perc)-1000)
        df_all[str(i)] = perc[start:start+1000]
    return df_all.drop(labels=['row_no'], axis=1)


if __name__ == '__main__':
    data = get_training_data()
    print(data)
