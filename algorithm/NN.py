import numpy as np
import pandas as pd

import pipeline.prepare_data as prep
from algorithm.activation_function import sigmoid, sigmoid_derivative, relu, relu_derivative, softmax


class NeuralNetwork:

    def __init__(self):
        self.input_size = 20
        self.layer_1_size = 25
        self.layer_2_size = 20
        self.output_size = 1
        self.weights1 = self._set_nn(weight=1, init=True)
        self.weights2 = self._set_nn(weight=2, init=True)
        self.weights3 = self._set_nn(weight=3, init=True)

    def feedforward(self, input):
        self.layer1 = relu(np.dot(input, self.weights1))
        self.layer2 = relu(np.dot(self.layer1, self.weights2))
        return sigmoid(np.dot(self.layer2, self.weights3))

    def backprop(self, input, output, y):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        # d_weights3 = np.dot(self.layer2.T, (2*(y - output) * sigmoid_derivative(output)))
        d_weights2 = np.dot(self.layer1.T, (2*(y - output) * relu_derivative(output)))
        d_weights1 = np.dot(input.T, (np.dot(2*(y - output) * relu_derivative(output),
                                             self.weights2.T) * relu_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def mutate(self):
        mutation_1 = np.random.rand(self.input_size, self.layer_1_size)
        indicator_11 = np.random.randint(0, 2, (self.input_size, self.layer_1_size))
        indicator_12 = np.random.randint(0, 3, (self.input_size, self.layer_1_size))
        self.weights1 = indicator_11 * indicator_12 * mutation_1 + self.weights1

        mutation_2 = np.random.rand(self.layer_1_size, self.output_size)
        indicator_21 = np.random.randint(0, 2, (self.layer_1_size, self.output_size))
        indicator_22 = np.random.randint(0, 3, (self.layer_1_size, self.output_size))
        self.weights2 = indicator_21 * indicator_22 * mutation_2 + self.weights2

        mutation_3 = np.random.rand(self.layer_2_size, self.output_size)
        indicator_31 = np.random.randint(0, 2, (self.layer_2_size, self.output_size))
        indicator_32 = np.random.randint(0, 3, (self.layer_2_size, self.output_size))
        self.weights3 = indicator_31 * indicator_32 * mutation_3 + self.weights3

    def _set_nn(self, weight=-1, init=False):
        if weight == 1:
            if init:
                w = np.random.rand(self.input_size, self.layer_1_size)
            else:
                w = prep.read_nn_from_file('SMGANN_research_W1_2021-08-11T14-45-26_4000.csv')
        elif weight == 2:
            if init:
                w = np.random.rand(self.layer_1_size, self.output_size)
            else:
                w = prep.read_nn_from_file('SMGANN_research_W2_2021-08-11T14-45-26_4000.csv')
        elif weight == 3:
            if init:
                w = np.random.rand(self.layer_2_size, self.output_size)
            else:
                w = prep.read_nn_from_file('SMGANN_research_W3_2021-08-11T14-45-26_4000.csv')
                w = w.reshape((25, 1))
        else:
            pass

        return w


class NeuralNetwork5:

    def __init__(self, init=True):
        self.input_size = 6
        self.layer_1_size = 10
        self.output_size = 3
        self.weights1 = self._set_nn(weight=1, init=init)
        self.weights2 = self._set_nn(weight=2, init=init)

    def feedforward(self, input):
        self.layer1 = relu(np.dot(input, self.weights1))
        return softmax(list(np.dot(self.layer1, self.weights2)))

    def backprop(self, input, output, y):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        # d_weights3 = np.dot(self.layer2.T, (2*(y - output) * sigmoid_derivative(output)))
        d_weights2 = np.dot(self.layer1.T, (2*(y - output) * relu_derivative(output)))
        d_weights1 = np.dot(input.T, (np.dot(2*(y - output) * relu_derivative(output),
                                             self.weights2.T) * relu_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def mutate(self, alpha=0.2):
        mutation_1 = alpha * np.random.rand(self.input_size, self.layer_1_size)
        indicator_11 = np.random.randint(-1, 2, (self.input_size, self.layer_1_size))
        indicator_12 = np.random.randint(-1, 2, (self.input_size, self.layer_1_size))
        self.weights1 = indicator_11 * indicator_12 * mutation_1 + self.weights1

        mutation_2 = alpha * np.random.rand(self.layer_1_size, self.output_size)
        indicator_21 = np.random.randint(-1, 2, (self.layer_1_size, self.output_size))
        indicator_22 = np.random.randint(-1, 2, (self.layer_1_size, self.output_size))
        self.weights2 = indicator_21 * indicator_22 * mutation_2 + self.weights2

    def _set_nn(self, weight=-1, init=False):
        if weight == 1:
            if init:
                w = np.random.rand(self.input_size, self.layer_1_size)
            else:
                w = prep.read_nn_from_file('SMGANN_research_W1_2021-08-11T14-45-26_4000.csv')
        elif weight == 2:
            if init:
                w = np.random.rand(self.layer_1_size, self.output_size)
            else:
                w = prep.read_nn_from_file('SMGANN_research_W2_2021-08-11T14-45-26_4000.csv')
        else:
            pass

        return w


if __name__ == '__main__':
    X = np.array([1, 2, 1, 1, 2])
    y = np.array([1, 2, 3])

    nn = NeuralNetwork5()


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
    for _ in range(10):
        output = nn.feedforward(X)
        # actions = actions.append(pd.DataFrame(output).T, ignore_index=True)
        # nn.backprop(X, output, y)
        count += 1
        print('\n', count)
        print(output)
        nn.mutate()

