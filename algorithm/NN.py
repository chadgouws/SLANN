import numpy as np
import pandas as pd

import pipeline.prepare_data as prep


def sigmoid(x):
    x[x < -14] = -14
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


class NeuralNetwork:

    def __init__(self):
        self.input_size = 30
        self.layer_1_size = 35
        self.layer_2_size = 25
        self.output_size = 1
        self.weights1 = self._set_nn(weight=1, init=False)
        self.weights2 = self._set_nn(weight=2, init=False)
        self.weights3 = self._set_nn(weight=3, init=False)

    def feedforward(self, input):
        self.layer1 = sigmoid(np.dot(input, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        return sigmoid(np.dot(self.layer2, self.weights3))

    def backprop(self, input, output, y):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights3 = np.dot(self.layer2.T, (2*(y - output) * sigmoid_derivative(output)))
        d_weights2 = np.dot(self.layer1.T, (2*(y - output) * sigmoid_derivative(output)))
        d_weights1 = np.dot(input.T,  (np.dot(2*(y - output) * sigmoid_derivative(output),
                                              self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def mutate(self):
        mutation_1 = np.random.rand(self.input_size, self.layer_1_size) - np.random.rand(self.input_size, self.layer_1_size)
        indicator_11 = np.random.randint(0, 2, (self.input_size, self.layer_1_size))
        indicator_12 = np.random.randint(0, 2, (self.input_size, self.layer_1_size))
        self.weights1 = indicator_11 * indicator_12 * mutation_1 + self.weights1

        mutation_2 = np.random.rand(self.layer_1_size, self.layer_2_size) - np.random.rand(self.layer_1_size, self.layer_2_size)
        indicator_21 = np.random.randint(0, 2, (self.layer_1_size, self.layer_2_size))
        indicator_22 = np.random.randint(0, 2, (self.layer_1_size, self.layer_2_size))
        self.weights2 = indicator_21 * indicator_22 * mutation_2 + self.weights2

        mutation_3 = np.random.rand(self.layer_2_size, self.output_size) - np.random.rand(self.layer_2_size, self.output_size)
        indicator_31 = np.random.randint(0, 2, (self.layer_2_size, self.output_size))
        indicator_32 = np.random.randint(0, 2, (self.layer_2_size, self.output_size))
        self.weights3 = indicator_31 * indicator_32 * mutation_3 + self.weights3

    def _set_nn(self, weight=-1, init=False):
        if weight == 1:
            if init:
                w = np.random.rand(self.input_size, self.layer_1_size) - np.random.rand(self.input_size, self.layer_1_size)
            else:
                w = prep.read_nn_from_file('SMGANN_1000_research_W1_2021-05-21T10-48-09.csv')
        elif weight == 2:
            if init:
                w = np.random.rand(self.layer_1_size, self.layer_2_size) - np.random.rand(self.layer_1_size, self.layer_2_size)
            else:
                w = prep.read_nn_from_file('SMGANN_1000_research_W2_2021-05-21T10-48-09.csv')
        elif weight == 3:
            if init:
                w = np.random.rand(self.layer_2_size, self.output_size) - np.random.rand(self.layer_2_size, self.output_size)
            else:
                w = prep.read_nn_from_file('SMGANN_1000_research_W3_2021-05-21T10-48-09.csv')
                w = w.reshape((25, 1))
        else:
            pass

        return w


if __name__ == '__main__':
    X = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                  [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                  [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                  [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
                  [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
                  [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1]])
    y = np.array([[1],
                  [0],
                  [0],
                  [1],
                  [1],
                  [0],
                  [0],
                  [1],
                  [1],
                  [1]])

    nn = NeuralNetwork()


    print('\ninput')
    print(X)
    print('\ny')
    print(y)
    print('\nw1')
    print(nn.weights1)
    print('\nw2')
    print(nn.weights2)
    print('\n')

    count = 0
    actions = pd.DataFrame()
    for _ in range(10000):
        output = nn.feedforward(X)
        actions = actions.append(pd.DataFrame(output).T, ignore_index=True)
        nn.backprop(X, output, y)
        count += 1
        print(count)
        print(output)

    print('\nW1')
    print(nn.weights1)
    print('\nW2')
    print(nn.weights2)
