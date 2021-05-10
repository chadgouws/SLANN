import copy
import datetime

import pandas as pd

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
        for gen in range(1, generations):
            # Simulate each NN for performance comparison
            self.cash_parent = self._simulate_nn('p')
            self.cash_child = self._simulate_nn('c')
            print('p cash: ', self.cash_parent)
            print('c cash: ', self.cash_child)
            # Compare performance and create next generation
            if self.cash_child >= self.cash_parent:
                self.parent = self.child
            else:
                self.parent = self.parent
            self.child = self._create_child()

            self.df_performance = prep.append_list_to_df(self.df_performance, [[gen, self.cash_parent, self.cash_child]])
        prep.write_df_to_file(self.df_performance, self.file_path)
        prep.write_nn_to_file(self.parent, algo='SMGANN')

    def _create_child(self):
        child = copy.deepcopy(self.parent)
        child.mutate()
        return child

    def _simulate_nn(self, nn_choice):
        if nn_choice == 'p':
            nn = self.parent
        elif nn_choice == 'c':
            nn = self.child
        else:
            pass

        prep.read_price_data(research=True)
        rp = ResearchPortfolio()
        for d in df.values:
            output = nn.feedforward(d)
            print(nn_choice + ' output: ', output)
            rp.order_type(output[0])
            rp.make_market_order(d[0])
            print(nn_choice + ' capital: ', rp.cash, rp.coin)

        return rp.cash + rp.coin * d[0]


if __name__ == '__main__':
    df = pd.DataFrame([[1, 0.8, 0.7],
                       [2, 1.7, 1.5],
                       [3, 2.5, 2.4],
                       [2, 2.2, 2.5],
                       [3, 2.9, 2.8]])

    egenn = EGeNN()
    egenn.best_nn(2)
