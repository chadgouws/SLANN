import numpy as np

from NN import sigmoid


a = np.array([[1, 0, 3]])

b = np.array([[4, 1, 4, 4],
              [2, 1, 2, 1],
              [1, 1, 1, 1]])
print(a)
print(b)
print(np.dot(a, b))
print(sigmoid(0.282238))
