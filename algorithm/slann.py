import copy
import datetime

import pandas as pd
import numpy as np

from algorithm.NN import NeuralNetwork
from pipeline.trader import ResearchPortfolio
from pipeline import prepare_data as prep


class EGeNN:

    def __init__(self):
        self.parent = NeuralNetwork()
        self.child = NeuralNetwork()
        self.columns = ['generation', 'cash_parent', 'cash_child']
        self.df_performance = pd.DataFrame(columns=self.columns)
        self.file_path = 'C:/Users/chadg/GARD/Projects/slann/data/SMGANN/mgann_research_' + \
                         datetime.datetime.now().strftime('%Y-%m-%dT%H-%M-%S') + '.csv'
        self.cash_parent = 0
        self.cash_child = 0

    def best_nn(self, generations):
        for gen in range(1, generations+1):
            print('Generation: ', gen)
            # Simulate each NN for performance comparison
            df_perc, df_price = prep.get_training_data(periods=1000, samples=30)
            self.cash_parent = self._simulate_nn('p', df_perc, df_price)
            self.cash_child = self._simulate_nn('c', df_perc, df_price)
            print('Parent: ', self.cash_parent)
            print('Child:  ', self.cash_child)
            # Compare performance and create next generation
            if self.cash_child >= self.cash_parent:
                self.parent = self.child
            else:
                self.parent = self.parent
            self.child = self._create_child()

            self.df_performance = prep.append_list_to_df(self.df_performance, [[gen, self.cash_parent, self.cash_child]])
        prep.write_df_to_file(self.df_performance, self.file_path)
        prep.write_nn_to_file(self.parent, algo='SMGANN', gen=generations)

    def _create_child(self):
        child = copy.deepcopy(self.parent)
        child.mutate()
        return child

    def _simulate_nn(self, nn_choice, df_perc, df_price):
        if nn_choice == 'p':
            nn = self.parent
        elif nn_choice == 'c':
            nn = self.child
        else:
            pass

        rp = ResearchPortfolio()
        for start in range(0, df_perc.shape[0]-29):
            end = start + 29
            input = df_perc.loc[start:end, :].values.T
            output = nn.feedforward(input)
            rp.order_type(output)
            rp.make_market_order(df_price.loc[end, :])

        return sum(np.array(rp.cash) + np.array(rp.coin) * df_price.loc[999, :].values.T)


if __name__ == '__main__':
    generations = 2000
    egenn = EGeNN()

    egenn.best_nn(generations)
