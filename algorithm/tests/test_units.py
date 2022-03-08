import unittest

import numpy as np
import numpy.testing as np_test

from algorithm.activation_function import relu, relu_derivative, sigmoid, sigmoid_derivative, softmax


class TestReLu(unittest.TestCase):

    def test_integer(self):
        control = 2
        test = relu(2)
        self.assertEqual(control, test, 'Integer broke ReLu activation function')

    def test_numpy_array_float(self):
        data = np.array([-1.1, 0.0, 1.0, 2.2, 3.3])
        control = np.array([0.0, 0.0, 1.0, 2.2, 3.3])
        test = relu(data)
        np_test.assert_array_equal(control, test)

    def test_numpy_array_integer(self):
        data = np.array([-1, 0, 1, 2, 3])
        control = np.array([0, 0, 1, 2, 3])
        test = relu(data)
        np_test.assert_array_equal(control, test)

    def test_numpy_nd_array(self):
        data = np.array([[-1, 0, 1, 2, 3],
                         [-1, 0, 1, 2, 3]])
        control = np.array([[0, 0, 1, 2, 3],
                            [0, 0, 1, 2, 3]])
        test = relu(data)
        np_test.assert_array_equal(control, test)

    def test_numpy_dot_product(self):
        pass

    def test_one(self):
        control = np.array(1)
        test = relu(1)
        np_test.assert_array_equal(control, test)

    def test_one_negative(self):
        control = np.array(0)
        test = relu(-1)
        np_test.assert_array_equal(control, test)

    def test_zero(self):
        control = np.array(0)
        test = relu(0)
        np_test.assert_array_equal(control, test)


class TestReLuDerivative(unittest.TestCase):

    def test_integer(self):
        control = 1
        test = relu_derivative(2)
        self.assertEqual(control, test, 'Integer broke ReLu activation function')

    def test_numpy_array_float(self):
        data = np.array([-1.1, 0.0, 1.0, 2.2, 3.3])
        control = np.array([0.0, 1.0, 1.0, 1.0, 1.0])
        test = relu_derivative(data)
        np_test.assert_array_equal(control, test)

    def test_numpy_array_integer(self):
        data = np.array([-1, 0, 1, 2, 3])
        control = np.array([0.0, 1.0, 1.0, 1.0, 1.0])
        test = relu_derivative(data)
        np_test.assert_array_equal(control, test)

    def test_numpy_nd_array(self):
        data = np.array([[-1, 0, 1, 2, 3],
                         [-1, 0, 1, 2, 3]])
        control = np.array([[0, 1, 1, 1, 1],
                            [0, 1, 1, 1, 1]])
        test = relu_derivative(data)
        np_test.assert_array_equal(control, test)

    def test_numpy_dot_product(self):
        pass

    def test_one(self):
        control = np.array(1)
        test = relu_derivative(1)
        np_test.assert_array_equal(control, test)

    def test_one_negative(self):
        control = np.array(0)
        test = relu_derivative(-1)
        np_test.assert_array_equal(control, test)

    def test_zero(self):
        control = np.array(1)
        test = relu_derivative(0)
        np_test.assert_array_equal(control, test)


class TestSigmoid(unittest.TestCase):

    def test_integer(self):
        pass

    def test_numpy_array(self):
        pass

    def test_numpy_nd_array(self):
        pass

    def test_numpy_dot_product(self):
        pass


class TestSigmoidDerivative(unittest.TestCase):

    def test_integer(self):
        pass

    def test_numpy_array(self):
        pass

    def test_numpy_nd_array(self):
        pass

    def test_numpy_dot_product(self):
        pass


if __name__ == '__main__':
    unittest.main()
