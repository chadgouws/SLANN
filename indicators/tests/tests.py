import unittest

import numpy as np
import pandas as pd
import pandas.testing as pd_testing

from indicators import indicators as ict


class TestADX(unittest.TestCase):

    def test_dn_max_edge_case(self):
        df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/gemini_BTCUSD_1hr.csv', header=0)
        control = pd.DataFrame()
        control['adx'] = ict.adx(df['Close'], df['High'], df['Low'])
        control = control.dropna()

        test = control.copy()
        print(test[test['adx'] > 100])
        test = test[test['adx'] <= 100]

        pd_testing.assert_frame_equal(control, test)

    def test_dn_min_edge_case(self):
        df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/gemini_BTCUSD_1hr.csv', header=0)
        control = pd.DataFrame()
        control['adx'] = ict.adx(df['Close'], df['High'], df['Low'])
        control = control.dropna()

        test = control.copy()
        test = test[test['adx'] >= 0]

        pd_testing.assert_frame_equal(control, test)


class TestAroon(unittest.TestCase):
    data_1 = {'Close': [8797.25, 8849.53, 8912.38, 8998.84, 8885.35],
              'High': [8809.79, 8868.30, 8912.38, 9070.65, 9033.33],
              'Low': [8756.70, 8774.73, 8827.30, 8880.68, 8824.10],
              }
    df_1 = pd.DataFrame(data_1)

    def test_dn_max_edge_case(self):
        df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/gemini_BTCUSD_1hr.csv', header=0)
        control = pd.DataFrame()
        control['up'], control['dn'] = ict.aroon(df['High'], df['Low'])
        control = control.dropna()

        test = control.copy()
        test = test[test['dn'] <= 100]

        pd_testing.assert_frame_equal(control, test)

    def test_dn_min_edge_case(self):
        df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/gemini_BTCUSD_1hr.csv', header=0)
        control = pd.DataFrame()
        control['up'], control['dn'] = ict.aroon(df['High'], df['Low'])
        control = control.dropna()

        test = control.copy()
        test = test[test['dn'] >= 0]

        pd_testing.assert_frame_equal(control, test)

    def test_up_max_edge_case(self):
        df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/gemini_BTCUSD_1hr.csv', header=0)
        control = pd.DataFrame()
        control['up'], control['dn'] = ict.aroon(df['High'], df['Low'])
        control = control.dropna()

        test = control.copy()
        test = test[test['up'] <= 100]

        pd_testing.assert_frame_equal(control, test)

    def test_up_min_edge_case(self):
        df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/gemini_BTCUSD_1hr.csv', header=0)
        control = pd.DataFrame()
        control['up'], control['dn'] = ict.aroon(df['High'], df['Low'])
        control = control.dropna()

        test = control.copy()
        test = test[test['up'] >= 0]

        pd_testing.assert_frame_equal(control, test)

    def test_two(self):
        pass


class TestBollingerBands(unittest.TestCase):
    pass


class TestMACD(unittest.TestCase):
    pass


class TestMA(unittest.TestCase):
    pass


class TestRSI(unittest.TestCase):

    data_1 = {'Close': [3323.32, 3333.02, 3339.99, 3350.0, 3358.96, 3404.43, 3436.54, 3581.67, 3594.57, 3596.82,
                        3606.72, 3608.24, 3626.39, 3632.41, 3638.04, 3669.29, 3681.24, 3687.01, 3687.27, 3688.01,
                        3691.92, 3702.84, 3712.52, 3713.43, 3716.63, 3722.95, 3724.73, 3725.0, 3729.73, 3730.29,
                        3740.01, 3765.89, 3774.8, 3800.88, 3811.0, 3813.21, 3814.17, 3814.99, 3816.27, 3817.87,
                        3819.42, 3826.18, 3828.55, 3829.75]
              }
    df_1 = pd.DataFrame(data_1)

    def test_max_edge_case(self):
        df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/gemini_BTCUSD_1hr.csv', header=0)
        control = pd.DataFrame()
        control['rsi'] = ict.rsi(df['Close'])
        test = control.copy()
        test['rsi'] = test[test['rsi'] <= 100]
        pd_testing.assert_frame_equal(control, test)

    def test_min_edge_case(self):
        df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/gemini_BTCUSD_1hr.csv', header=0)
        control = pd.DataFrame()
        control['rsi'] = ict.rsi(df['Close'])
        test = control.copy()
        test['rsi'] = test[test['rsi'] >= 0]
        pd_testing.assert_frame_equal(control, test)

    def test_10(self):
        pass

    def test_20(self):
        pass

    def test_50(self):
        pass

    def test_100(self):
        pass


class TestStochastic(unittest.TestCase):

    def test_max_edge_case(self):
        df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/gemini_BTCUSD_1hr.csv', header=0)
        control = pd.DataFrame()
        control['k'], control['d'] = ict.stochastic(df['Close'], df['High'], df['Low'])
        test = control.copy()
        test['k'] = test[test['k'] <= 100]
        pd_testing.assert_frame_equal(control, test)

    def test_min_edge_case(self):
        df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/data/price_ticker/real/gemini_BTCUSD_1hr.csv', header=0)
        control = pd.DataFrame()
        control['k'], control['d'] = ict.stochastic(df['Close'], df['High'], df['Low'])
        test = control.copy()
        test['k'] = test[test['k'] >= 0]
        pd_testing.assert_frame_equal(control, test)


class TestTrueRange(unittest.TestCase):
    data_1 = {'Close': [8797.25, 8849.53, 8912.38, 8998.84, 8885.35],
              'High': [8809.79, 8868.30, 8912.38, 9070.65, 9033.33],
              'Low': [8756.70, 8774.73, 8827.30, 8880.68, 8824.10],
              }
    df_1 = pd.DataFrame(data_1)

    def test_one(self):
        control = pd.DataFrame([53.09, 93.57, 85.08, 189.97, 209.23], columns=['test'])

        test = pd.DataFrame()
        test['test'] = ict.true_range(self.df_1['Close'], self.df_1['High'], self.df_1['Low'])

        pd_testing.assert_frame_equal(control, test)

    def test_two(self):
        pass

    def test_three(self):
        pass


if __name__ == '__main__':
    unittest.main()
