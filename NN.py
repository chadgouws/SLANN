import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


class NeuralNetwork:

    def __init__(self, x, y):
        self.input      = x
        self.weights1   = np.random.rand(3, 4)
        self.weights2   = np.random.rand(4, 1)
        self.y          = y
        self.output     = np.zeros(self.y.shape)

    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.output = sigmoid(np.dot(self.layer1, self.weights2))

    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2*(self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2*(self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2


if __name__ == '__main__':
    X = np.array([[1, 1, 1],
                  [0, 0, 0],
                  [1, 0, 0],
                  [1, 0, 1]])
    y = np.array([[1],
                  [0],
                  [0],
                  [1]])

    nn = NeuralNetwork(X, y)

    print('\ninput')
    print(nn.input)
    print('\ny')
    print(nn.y)
    print('\nw1')
    print(nn.weights1)
    print('\nw2')
    print(nn.weights2)
    print('\noutput')
    print(nn.output)

    count = 0
    for _ in range(10000):
        nn.feedforward()
        nn.backprop()
        count += 1
        print(count)
        print(nn.output)

    print('\nW1')
    print(nn.weights1)
    print('\nW2')
    print(nn.weights2)
