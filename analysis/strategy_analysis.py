import matplotlib.pyplot as plt
import pandas as pd


def metric_evolution(iteration, metric, title='Title'):
    # Plot data
    plt.plot(iteration, metric)

    # Label plot
    plt.title(title)
    plt.ylabel(title)
    plt.xlabel('ITERATION')
    plt.show()


if __name__ == '__main__':
    file_path = 'C:/Users/chadg/GARD/Projects/slann/backtesting/backtesting_data/metrics/'
    file_name = ''
    df = pd.read_csv(file_path+file_name, header=0)

    metric_evolution(df['ITERATION'], df['SUPER_METRIC'], title='SUPER METRIC')
    metric_evolution(df['ITERATION'], df['ROI'], title='ROI')
    metric_evolution(df['ITERATION'], df['WIN_RATIO'], title='WIN RATIO')
    metric_evolution(df['ITERATION'], df['NO_OF_TRADES'], title='NO. OF TRADES')
