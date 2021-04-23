import copy

import pandas as pd

from algorithm.NN import NeuralNetwork
from pipeline.trader import ResearchPortfolio


class EGeNN:

    def __init__(self):
        self.parent = NeuralNetwork()
        self.child = NeuralNetwork()
        self.portfolio_parent = ResearchPortfolio()
        self.portfolio_child = ResearchPortfolio()

    def best_nn(self, iterations, df):
        for _ in range(0, iterations):
            # Simulate each NN for performance comparison
            cash_parent = self._simulate_nn('p', df)
            cash_child = self._simulate_nn('c', df)
            print('p cash: ', cash_parent)
            print('c cash: ', cash_child)
            # Compare performance and create next generation
            if cash_child > cash_parent:
                self.parent = self.child
            else:
                self.parent = self.parent
            self.child = self._create_child()

    def _create_child(self):
        child = copy.deepcopy(self.parent)
        child.mutate()
        return child

    def _simulate_nn(self, nn_choice, df):
        if nn_choice == 'p':
            nn = self.parent
        elif nn_choice == 'c':
            nn = self.child
        else:
            pass

        rp = ResearchPortfolio()
        for d in df.values:
            output = nn.feedforward(d)
            print(nn_choice + ' output: ', output)
            rp.order_type(output[0])
            rp.make_market_order(d[0])
            print(nn_choice + ' capital: ', rp.cash, rp.coin)

        return rp.cash + rp.coin * d[0]


if __name__ == '__main__':
    df = pd.DataFrame([[1, 0.8, 0.7], [2, 1.7, 1.5], [3, 2.5, 2.4], [2, 2.2, 2.5], [3, 2.9, 2.8]])
    print(df)
    egenn = EGeNN()

    egenn.best_nn(2, df)
