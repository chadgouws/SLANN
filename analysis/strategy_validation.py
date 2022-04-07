import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def analyze_strategy(time, portfolio, asset, title='Title'):
    # Normalize data
    portfolio = 100 * portfolio / portfolio.loc[0]
    asset = 100 * asset / asset.loc[0]

    # Plot data
    plt.plot(time, portfolio)
    plt.plot(time, asset)

    # Label plot
    plt.title(title)
    plt.ylabel(title)
    plt.xlabel('TIME')
    plt.legend(['PORTFOLIO', 'ASSET'])
    plt.show()


if __name__ == '__main__':
    file_path = 'C:/Users/chadg/GARD/Projects/slann/backtesting/backtesting_data/analysis/'
    file_name = 'nn_architecture_relu-softmax-6-10-None-3_2000-10_2022-03-11T10-55-14.csv'
    df = pd.read_csv(file_path+file_name, header=0)
    df['ITERATION'] = np.where(df['SUPER_METRIC'] > -1000, 1, 0)
    df['ITERATION'] = df['ITERATION'].cumsum()
    print(df)

    metric_evolution(df['ITERATION'], df['SUPER_METRIC'], title='SUPER METRIC')
    metric_evolution(df['ITERATION'], df['ROI'], title='ROI')
    metric_evolution(df['ITERATION'], df['WIN_RATIO'], title='WIN RATIO')
    metric_evolution(df['ITERATION'], df['NO_OF_TRADES'], title='NO. OF TRADES')
    metric_evolution(df['ITERATION'], df['LOSER_ROI_MAX'], title='LOSER ROI MAX')
    compare_two_metrics(df['ITERATION'], df['ROI'], df['ROI_ASSET'], title='ROI')
    compare_two_metrics(df['ITERATION'], df['STD_DEV_PORTFOLIO'], df['STD_DEV_ASSET'], title='STD DEV')
