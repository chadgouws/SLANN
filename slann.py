import numpy as np
import pandas as pd
import copy

from . import NN


class SlaNN:

    def __init__(self):
        self.parent = NN.NeuralNetwork()

    def best_nn(self, iterations):
        for _ in range(0, iterations):
            parent = self.parent
            child = self._create_child()
            parent_actions = self._simulate_nn(parent)
            child_actions = self._simulate_nn(child)
            # is Performance(C1) > Performance(P)
                # Set P = C1
                # or create C2

    def _evolution_policy(self):
        #while _nn_performance()
        pass

    def _create_child(self):
        child = copy.deepcopy(self.parent)
        child.backprop()
        return child

    def _simulate_nn(self, nn):
        output = []

        for d in self.df:
            nn.feedforward(d)
            output.append(nn.output)

        return output

    def _calculate_performance(self, output):
        actions = []

        for action in output:
            if action > 0.7:
                actions.append(1)
            elif 0.3 <= action <= 0.7:
                actions.append(0.5)
            else:
                actions.append(0)

        temp = -1
        for i in range(0, len(actions)):
            if actions[i] == 1 and temp != actions[i]:
                position = ['Buy', self.df[i]]
            elif actions[i] == 0 and temp != actions[i]:
                position = ['Sell', self.df[i]]
            else:
                position = ['Hold', self.df[i]]

            temp = actions[i]


if __name__ == '__main__':

