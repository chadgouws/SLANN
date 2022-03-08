import numpy as np
from scipy.special import softmax

# This script contains activation functions and their respective derivatives that
# are generally used for deep learning models


def binary_step(x):
    if x < 0:
        return 0
    else:
        return 1


def binary_step_derivative(x):
    return 0


def leaky_relu(x):
    if x < 0:
        return 0.01 * x
    else:
        return x


def leaky_relu_derivative(x):
    if x < 0:
        return 0.01
    else:
        return 1


def linear(x):
    return 2 * x


def linear_derivative(x):
    return 2


def relu(x):
    return np.where(x < 0, 0, x)


def relu_derivative(x):
    return np.where(x < 0, 0, 1)


def sigmoid(x):
    x[x < -14] = -14
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


if __name__ == '__main__':
    print(relu(1), relu(0), relu(-1))
    print(relu_derivative(1), relu_derivative(0), relu_derivative(-1))
