import numpy as np
import pandas as pd


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


class NeuralNetwork:

    def __init__(self):
        self.input_size = 3
        self.layer_1_size = 4
        self.output_size = 1
        self.weights1 = np.random.rand(self.input_size, self.layer_1_size) - np.random.rand(self.input_size, self.layer_1_size)
        self.weights2 = np.random.rand(self.layer_1_size, self.output_size) - np.random.rand(self.layer_1_size, self.output_size)

    def feedforward(self, input):
        self.layer1 = sigmoid(np.dot(input, self.weights1))
        return sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self, input, output, y):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(y - output) * sigmoid_derivative(output)))
        d_weights1 = np.dot(input.T,  (np.dot(2*(y - output) * sigmoid_derivative(output),
                                              self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def mutate(self):
        mutation_1 = np.random.rand(self.input_size, self.layer_1_size) / 5 - np.random.rand(self.input_size, self.layer_1_size) / 5
        indicator_1 = np.random.randint(0, 2, (self.input_size, self.layer_1_size))
        self.weights1 = indicator_1 * mutation_1 + self.weights1

        mutation_2 = np.random.rand(self.layer_1_size, self.output_size) / 5 - np.random.rand(self.layer_1_size, self.output_size) / 5
        indicator_2 = np.random.randint(0, 2, (self.layer_1_size, self.output_size))
        self.weights2 = indicator_2 * mutation_2 + self.weights2


if __name__ == '__main__':
    X = np.array([[1, 1, 1],
                  [0, 0, 0],
                  [1, 0, 0],
                  [1, 0, 1]])
    y = np.array([[1],
                  [0],
                  [0],
                  [1]])

    nn = NeuralNetwork()
    print(nn.weights1)
    nn.mutate()
    print(nn.weights1)


    # print('\ninput')
    # print(X)
    # print('\ny')
    # print(y)
    # print('\nw1')
    # print(nn.weights1)
    # print('\nw2')
    # print(nn.weights2)
    # print('\n')
    #
    # count = 0
    # actions = pd.DataFrame()
    # for _ in range(10000):
    #     output = nn.feedforward(X)
    #     actions = actions.append(pd.DataFrame(output).T, ignore_index=True)
    #     nn.backprop(X, output, y)
    #     count += 1
    #     print(count)
    #     print(output)
    #
    # print('\nW1')
    # print(nn.weights1)
    # print('\nW2')
    # print(nn.weights2)
