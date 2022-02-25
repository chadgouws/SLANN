import unittest

import pandas as pd
import numpy as np

from analysis.metrics import roi, trade_profit_loss, win_ratio


df = pd.read_csv('C:/Users/chadg/GARD/Projects/slann/analysis/tests/metrics.test_data.csv')


class TestLoserROIAvg(unittest.TestCase):

    def test_all_losers(self):
        pass

    def test_no_losers(self):
        pass

    def test_no_trades(self):
        pass

    def test_some_losers(self):
        pass


class TestLoserROIMax(unittest.TestCase):

    def test_something(self):
        pass


class TestROI(unittest.TestCase):

    def test_array(self):
        data = np.array([1, 0.9, 1.1])
        control = (data[-1] / data[0]) - 1
        test = roi(data)
        self.assertEqual(control, test, 'Array breaks ROI calculation')

    def test_list(self):
        data = [1, 0.9, 1.1]
        control = (data[-1] / data[0]) - 1
        test = roi(data)
        self.assertEqual(control, test, 'List breaks ROI calculation')

    def test_negative_roi(self):
        data = np.array([1, 0.9, 0.8])
        control = (data[-1] / data[0]) - 1
        test = roi(data)
        self.assertEqual(control, test, 'Negative ROI breaks ROI calculation')

    def test_non_sequence(self):
        data = 1
        test = roi(data)
        self.assertIsNone(test, 'No elements breaks ROI calculation')

    def test_no_elements(self):
        data = np.array([])
        test = roi(data)
        self.assertIsNone(test, 'No elements breaks ROI calculation')

    def test_one_element(self):
        data = np.array([1])
        control = (data[-1] / data[0]) - 1
        test = roi(data)
        self.assertEqual(control, test, 'One element breaks ROI calculation')

    def test_pandas(self):
        data = pd.DataFrame([1, 0.9, 1.1])
        data = data.to_numpy()
        control = (data[-1] / data[0]) - 1
        test = roi(data)
        self.assertEqual(control, test, 'Positive ROI breaks ROI calculation')

    def test_positive_roi(self):
        data = np.array([1, 0.9, 1.1])
        control = (data[-1] / data[0]) - 1
        test = roi(data)
        self.assertEqual(control, test, 'Positive ROI breaks ROI calculation')

    def test_tuple(self):
        data = (1, 0.9, 1.1)
        control = (data[-1] / data[0]) - 1
        test = roi(data)
        self.assertEqual(control, test, 'Tuple breaks ROI calculation')

    def test_zero_roi(self):
        data = np.array([1, 0.9, 1.0])
        control = (data[-1] / data[0]) - 1
        test = roi(data)
        self.assertEqual(control, test, 'Zero ROI breaks ROI calculation')

    def test_zeroes(self):
        data = np.array([0.0, 0.0, 0.0])
        test = roi(data)
        self.assertIsNone(test, 'Zeroes break ROI calculation')


class TestWinnerROIAvg(unittest.TestCase):

    def test_something(self):
        pass


class TestWinnerROIMax(unittest.TestCase):

    def test_something(self):
        pass


class TestTradeProfitLoss(unittest.TestCase):

    def test_asset_value_negative(self):
        df = pd.DataFrame([['BUY', -10.0, 0], ['BUY', -10.0, 0], ['BUY', -10.0, 0], ['BUY', -10.0, 0]],
                          columns=['TRADE', 'TRADE_NET_VALUE', 'ASSET_VALUE'])
        test = trade_profit_loss(df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        self.assertIsNone(test, 'Asset value negative broke Trade Profit Loss Calc.')

    def test_buys_only_negative(self):
        df = pd.DataFrame([['BUY', -10.0, 0], ['BUY', -10.0, 0], ['BUY', -10.0, 0], ['BUY', -10.0, 0]],
                          columns=['TRADE', 'TRADE_NET_VALUE', 'ASSET_VALUE'])
        test = trade_profit_loss(df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        self.assertIsNone(test, 'Buys only negative broke Trade Profit Loss Calc.')

    def test_buys_only_positive_loss(self):
        df = pd.DataFrame([['BUY', 10.0, 9.99], ['BUY', 10.0, 19.98], ['BUY', 10.0, 29.97], ['BUY', 10.0, 39.96]],
                          columns=['TRADE', 'TRADE_NET_VALUE', 'ASSET_VALUE'])
        control = -0.04
        test = trade_profit_loss(df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        self.assertEqual(control, test, 'Buys only positive broke Trade Profit Loss Calc.')

    def test_buys_only_positive_profit(self):
        df = pd.DataFrame([['BUY', 10.0, 9.99], ['BUY', 10.0, 19.9], ['BUY', 10.0, 30.0], ['BUY', 10.0, 41.0]],
                          columns=['TRADE', 'TRADE_NET_VALUE', 'ASSET_VALUE'])
        control = 1.0
        test = trade_profit_loss(df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        self.assertEqual(control, test, 'Buys only positive broke Trade Profit Loss Calc.')

    def test_buys_only_zero(self):
        df = pd.DataFrame([['BUY', 0.0, 0.0], ['BUY', 0.0, 0.0], ['BUY', 0.0, 0.0], ['BUY', 0.0, 0.0]],
                          columns=['TRADE', 'TRADE_NET_VALUE', 'ASSET_VALUE'])
        test = trade_profit_loss(df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        self.assertIsNone(test, 'Buys only zero broke Trade Profit Loss Calc.')

    def test_holds_only_negative(self):
        df = pd.DataFrame([['HOLD', -10.0, 10.0], ['HOLD', -10.0, 10.0], ['HOLD', -10.0, 10.0], ['HOLD', -10.0, 10.0]],
                          columns=['TRADE', 'TRADE_NET_VALUE', 'ASSET_VALUE'])
        test = trade_profit_loss(df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        self.assertIsNone(test, 'Holds only negative broke Trade Profit Loss Calc.')

    def test_holds_only_positive(self):
        df = pd.DataFrame([['HOLD', 10.0, 10.0], ['HOLD', 10.0, 10.0], ['HOLD', 10.0, 10.0], ['HOLD', 10.0, 10.0]],
                          columns=['TRADE', 'TRADE_NET_VALUE', 'ASSET_VALUE'])
        test = trade_profit_loss(df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        self.assertIsNone(test, 'Holds only positive broke Trade Profit Loss Calc.')

    def test_holds_only_profit(self):
        df = pd.DataFrame([['HOLD', 0.0, 10.0], ['HOLD', 0.0, 10.0], ['HOLD', 0.0, 10.0], ['HOLD', 0.0, 10.1]],
                          columns=['TRADE', 'TRADE_NET_VALUE', 'ASSET_VALUE'])
        control = 0.1
        test = trade_profit_loss(df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        self.assertEqual(control, test, 'Holds only profit broke Trade Profit Loss Calc.')

    def test_holds_only_zero(self):
        df = pd.DataFrame([['HOLD', 0.0, 0.0], ['HOLD', 0.0, 0.0], ['HOLD', 0.0, 0.0], ['HOLD', 0.0, 0.0]],
                          columns=['TRADE', 'TRADE_NET_VALUE', 'ASSET_VALUE'])
        test = trade_profit_loss(df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        self.assertIsNone(test, 'Holds only zero broke Trade Profit Loss Calc.')

    def test_list(self):
        trade = ['BUY', 'BUY', 'BUY', 'BUY']
        trade_net_value = [10.0, 10.0, 10.0, 10.0]
        asset_value = [9.99, 19.98, 29.97, 39.96]
        control = -0.04
        test = trade_profit_loss(trade, trade_net_value, asset_value)
        self.assertEqual(control, test, 'List broke Trade Profit Loss Calc.')

    def test_no_elements(self):
        test = trade_profit_loss([], [], [])
        self.assertIsNone(test, 'No elements broke Trade Profit Loss calculation')

    def test_one_element(self):
        df = pd.DataFrame([['BUY', 10.0, 9.99]], columns=['TRADE', 'TRADE_NET_VALUE', 'ASSET_VALUE'])
        control = -0.01
        test = trade_profit_loss(df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        self.assertEqual(control, test, 'One element breaks Trade Profit Loss calculation')

    def test_one_to_one(self):
        df = pd.DataFrame([['HOLD', 0.00, 9.99], ['BUY', 10.0, 19.98], ['SELL', 9.99, 9.98],
                           ['HOLD', 0.0, 9.98], ['BUY', 10.0, 19.97], ['BUY', 10.0, 29.96]],
                          columns=['TRADE', 'TRADE_NET_VALUE', 'ASSET_VALUE'])
        control = -0.04
        test = trade_profit_loss(df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        self.assertEqual(control, test, 'One to one broke Trade Profit Loss Calc.')

    def test_one_to_zero(self):
        df = pd.DataFrame([['HOLD', 0.00, 9.99], ['BUY', 10.0, 19.98], ['SELL', 9.99, 9.98],
                           ['HOLD', 0.0, 9.98], ['BUY', 10.0, 19.97], ['BUY', 10.0, 29.96]],
                          columns=['TRADE', 'TRADE_NET_VALUE', 'ASSET_VALUE'])
        control = -0.04
        test = trade_profit_loss(df['TRADE'], df['TRADE_NET_VALUE'], df['ASSET_VALUE'])
        self.assertEqual(control, test, 'One to zero broke Trade Profit Loss Calc.')

    def test_sells_only_negative(self):
        df = pd.DataFrame([['SELL', -10.0], ['SELL', -10.0], ['SELL', -10.0], ['SELL', -10.0]],
                          columns=['TRADE', 'TRADE_NET_VALUE'])
        initial_asset_amt = 0
        control = 0
        test = win_ratio(df['TRADE'], df['TRADE_NET_VALUE'])
        self.assertEqual(control, test, 'Sells only negative broke Trade Profit Loss Calc.')

    def test_sells_only_positive(self):
        df = pd.DataFrame([['SELL', 10.0], ['SELL', 10.0], ['SELL', 10.0], ['SELL', 10.0]],
                          columns=['TRADE', 'TRADE_NET_VALUE'])
        initial_asset_amt = 0
        control = 0
        test = win_ratio(df['TRADE'], df['TRADE_NET_VALUE'])
        self.assertEqual(control, test, 'Sells only positive broke Trade Profit Loss Calc.')

    def test_sells_only_zero(self):
        df = pd.DataFrame([['SELL', 0.0], ['SELL', 0.0], ['SELL', 0.0], ['SELL', 0.0]],
                          columns=['TRADE', 'TRADE_NET_VALUE'])
        initial_asset_amt = 0
        control = 0
        test = win_ratio(df['TRADE'], df['TRADE_NET_VALUE'])
        self.assertEqual(control, test, 'Sells only zero broke Trade Profit Loss Calc.')

    def test_tuple(self):
        trade = ('BUY', 'BUY', 'BUY', 'BUY')
        trade_net_value = (10.0, 10.0, 10.0, 10.0)
        asset_value = (9.99, 19.98, 29.97, 39.96)
        control = -0.04
        test = trade_profit_loss(trade, trade_net_value, asset_value)
        self.assertEqual(control, test, 'List broke Trade Profit Loss Calc.')

    def test_zeroes(self):
        df = pd.DataFrame([['SELL', 0.0], ['BUY', 0.0], ['SELL', 0.0], ['HOLD', 0.0], ['BUY', 0.0], ['BUY', 0.0]],
                          columns=['TRADE', 'TRADE_NET_VALUE'])
        initial_asset_amt = 0
        control = 0
        test = win_ratio(df['TRADE'], df['TRADE_NET_VALUE'])
        self.assertEqual(control, test, 'Zeroes only broke Trade Profit Loss Calc.')

    def test_zero_to_zero(self):
        df = pd.DataFrame([['SELL', 0.0], ['BUY', 0.0], ['SELL', 0.0], ['HOLD', 0.0], ['BUY', 0.0], ['BUY', 0.0]],
                          columns=['TRADE', 'TRADE_NET_VALUE'])
        initial_asset_amt = 0
        control = 0
        test = win_ratio(df['TRADE'], df['TRADE_NET_VALUE'])
        self.assertEqual(control, test, 'Zero to zero broke Trade Profit Loss Calc.')

    def test_zero_to_one(self):
        df = pd.DataFrame([['SELL', 0.0], ['BUY', 0.0], ['SELL', 0.0], ['HOLD', 0.0], ['BUY', 0.0], ['BUY', 0.0]],
                          columns=['TRADE', 'TRADE_NET_VALUE'])
        initial_asset_amt = 0
        control = 0
        test = win_ratio(df['TRADE'], df['TRADE_NET_VALUE'])
        self.assertEqual(control, test, 'Zero to one broke Trade Profit Loss Calc.')


if __name__ == '__main__':
    unittest.main()
