import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def metric_evolution(iteration, metric, title='Title'):
    # Plot data
    plt.scatter(iteration, metric, s=10)
    plt.grid(visible=True)

    # Label plot
    plt.title(title)
    plt.ylabel(title)
    plt.xlabel('ITERATION')
    plt.show()


def compare_two_metrics(iteration, metric_1, metric_2, title='Title'):
    # Plot data
    plt.bar(iteration, 100 * (metric_1 - metric_2) / metric_2)

    # Label plot
    plt.title(title)
    plt.ylabel('Percentage Change [%]')
    plt.xlabel('ITERATION')
    plt.show()


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
    file_path = 'C:/Users/chadg/GARD/Projects/slann/backtesting/backtesting_data/metrics/'
    file_name = 'nn_architecture_relu-softmax-6-10-None-3_850-10_2022-04-07T10-55-14.csv'
    df = pd.read_csv(file_path+file_name, header=0)
    df['ITERATION'] = np.where(df['SUPER_METRIC'] > -1000, 1, 0)
    df['ITERATION'] = df['ITERATION'].cumsum()

    metric_evolution(df['ITERATION'], df['NO_OF_TRADES'], title='NO. OF TRADES')

    metric_evolution(df['ITERATION'], df['SUPER_METRIC'], title='SUPER METRIC')
    metric_evolution(df['ITERATION'], df['ROI'], title='ROI')
    metric_evolution(df['ITERATION'], df['WIN_RATIO'], title='WIN RATIO')
    metric_evolution(df['ITERATION'], df['MAX_DRAWDOWN'], title='MAX DRAWDOWN')

    metric_evolution(df['ITERATION'], df['LOSER_ROI_MAX'], title='LOSER ROI MAX')
    metric_evolution(df['ITERATION'], df['LOSER_ROI_AVG'], title='LOSER ROI AVG')
    metric_evolution(df['ITERATION'], df['WINNER_ROI_MAX'], title='WINNER ROI MAX')
    metric_evolution(df['ITERATION'], df['WINNER_ROI_AVG'], title='WINNER ROI AVG')
