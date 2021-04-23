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
            # Compare performance and create next generation
            if cash_child > cash_parent:
                self.parent = self.child
            else:
                self.parent = self.parent
            self.child = self._create_child()
            # Reset each NN portfolio for next iteration
            self.portfolio_parent = ResearchPortfolio()
            self.portfolio_child = ResearchPortfolio()

    def _create_child(self):
        child = copy.deepcopy(self.parent)
        # slightly change NN weights
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
            print(d)
            output = nn.feedforward(d)
            print(output)
            rp.order_type(output)
            rp.make_market_order(d)

        return rp.cash + rp.coin * d


if __name__ == '__main__':
    df = pd.DataFrame([[1], [2], [3], [2], [3]])
    print(df)
    egenn = EGeNN()

    egenn.best_nn(2, df)
