import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def analyse_metric(iteration, metric, title='Title'):
    df = pd.DataFrame({'ITERATION': iteration, 'METRIC': metric})
    df['ITERATION'] = (df['ITERATION'] + 1) / 50
    df['ITERATION'] = np.ceil(df['ITERATION'])
    df_agg = df.groupby(['ITERATION']).mean()
    plt.plot(range(1, 21), df_agg['METRIC'])
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    file_name = 'C:/Users/chadg/GARD/Projects/slann/backtesting/backtesting_data/metrics/nn_architecture_relu-softmax-6-10-None-3_2000-1000_2022-03-10T11-28-00.csv'
    df = pd.read_csv(file_name, header=0)

    analyse_metric(df['ITERATION'], df['SUPER_METRIC'], title='SUPER METRIC')
    analyse_metric(df['ITERATION'], df['ROI'], title='ROI')
    analyse_metric(df['ITERATION'], df['WIN_RATIO'], title='WIN RATIO')
    analyse_metric(df['ITERATION'], df['NO_OF_TRADES'], title='NO OF TRADES')
