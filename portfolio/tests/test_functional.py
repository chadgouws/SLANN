import unittest

from portfolio.portfolio import Portfolio
from portfolio.tests import data
from portfolio.tests import functions as func


class TestPortfolioFunctional(unittest.TestCase):

    def test_one_token(self):
        """
        Test the functions of the process on one token.
        Uses weight_1 and fee
        """
        port = Portfolio(cash_initial=data.cash_initial_1, buy_weight=data.weight_1, sell_weight=data.weight_1)
        port.asset_amt['BTC'] = data.asset_initial_1

        timeline = data.data_1
        for t in timeline:
            # Control function
            order = func.order_type(t['algo_output'])
            trade_amt, asset_amt, asset_value, portfolio_value = func.trade_token(order, token=t['token'],
                                                                                  asset_amt=t['asset_amt'],
                                                                                  asset_price=t['asset_price'],
                                                                                  weight=data.weight_1,
                                                                                  fee=data.fee)
            # Test function
            price = {t['token']: t['asset_price']['BTC']}
            port.update_prices(price)
            port.update_portfolio()
            port.get_order_type(t['algo_output'], token=t['token'])
            port.trade_pair(t['token'], buy_fee=data.fee, sell_fee=data.fee)
            port.update_portfolio()

            self.assertEqual(trade_amt, port.trade_amt, 'Trade amount not updated correctly')
            self.assertDictEqual(t['asset_price'], port.asset_prices, 'Price dictionary not updated correctly')
            self.assertDictEqual(asset_amt, port.asset_amt, 'Asset amount dictionary not updated correctly')
            self.assertDictEqual(asset_value, port.asset_values, 'Asset values dictionary not updated correctly')
            self.assertEqual(portfolio_value, port.portfolio_value, 'Portfolio value not updated correctly')

    def test_three_tokens_0(self):
        """
        Test the functions of the process on 3 tokens.
        Uses weight_1 and fee
        """
        port = Portfolio(cash_initial=data.cash_initial_0, buy_weight=data.weight_1, sell_weight=data.weight_1)
        port.asset_amt['BTC'] = data.asset_initial_0
        port.asset_amt['ETH'] = data.asset_initial_0
        port.asset_amt['XRP'] = data.asset_initial_0

        timeline = data.data_2
        asset_amt = {'cash': data.cash_initial_0, 'BTC': data.asset_initial_0,
                     'ETH': data.asset_initial_0, 'XRP': data.asset_initial_0}
        for t in timeline:
            # Control function
            order = func.order_type(t['algo_output'])
            trade_amt, asset_amt, asset_value, portfolio_value = func.trade_token(order, token=t['token'],
                                                                                  asset_amt=asset_amt,
                                                                                  asset_price=t['asset_price'],
                                                                                  weight=data.weight_1,
                                                                                  fee=data.fee)
            # Test function
            price = t['asset_price']
            port.update_prices(price)
            port.update_portfolio()
            port.get_order_type(t['algo_output'], token=t['token'])
            port.trade_pair(t['token'], buy_fee=data.fee, sell_fee=data.fee)
            port.update_portfolio()

            self.assertEqual(trade_amt, port.trade_amt, 'Trade amount not updated correctly')
            self.assertDictEqual(t['asset_price'], port.asset_prices, 'Price dictionary not updated correctly')
            self.assertDictEqual(asset_amt, port.asset_amt, 'Asset amount dictionary not updated correctly')
            self.assertDictEqual(asset_value, port.asset_values, 'Asset values dictionary not updated correctly')
            self.assertEqual(portfolio_value, port.portfolio_value, 'Portfolio value not updated correctly')

    def test_three_tokens_1(self):
        """
        Test the functions of the process on 3 tokens.
        Uses weight_1 and fee
        """
        port = Portfolio(cash_initial=data.cash_initial_1, buy_weight=data.weight_1, sell_weight=data.weight_1)
        port.asset_amt['BTC'] = data.asset_initial_1
        port.asset_amt['ETH'] = data.asset_initial_1
        port.asset_amt['XRP'] = data.asset_initial_1

        timeline = data.data_2
        asset_amt = {'cash': data.cash_initial_1, 'BTC': data.asset_initial_1,
                     'ETH': data.asset_initial_1, 'XRP': data.asset_initial_1}
        for t in timeline:
            # Control function
            order = func.order_type(t['algo_output'])
            trade_amt, asset_amt, asset_value, portfolio_value = func.trade_token(order, token=t['token'],
                                                                                  asset_amt=asset_amt,
                                                                                  asset_price=t['asset_price'],
                                                                                  weight=data.weight_1,
                                                                                  fee=data.fee)
            # Test function
            price = t['asset_price']
            port.update_prices(price)
            port.update_portfolio()
            port.get_order_type(t['algo_output'], token=t['token'])
            port.trade_pair(t['token'], buy_fee=data.fee, sell_fee=data.fee)
            port.update_portfolio()

            self.assertEqual(trade_amt, port.trade_amt, 'Trade amount not updated correctly')
            self.assertDictEqual(t['asset_price'], port.asset_prices, 'Price dictionary not updated correctly')
            self.assertDictEqual(asset_amt, port.asset_amt, 'Asset amount dictionary not updated correctly')
            self.assertDictEqual(asset_value, port.asset_values, 'Asset values dictionary not updated correctly')
            self.assertEqual(portfolio_value, port.portfolio_value, 'Portfolio value not updated correctly')

    def test_three_tokens_2(self):
        """
        Test the functions of the process on 3 tokens.
        Uses weight_1 and fee
        """
        port = Portfolio(cash_initial=data.cash_initial_2, buy_weight=data.weight_1, sell_weight=data.weight_1)
        port.asset_amt['BTC'] = data.asset_initial_2
        port.asset_amt['ETH'] = data.asset_initial_2
        port.asset_amt['XRP'] = data.asset_initial_2

        timeline = data.data_3
        asset_amt = {'cash': data.cash_initial_2, 'BTC': data.asset_initial_2,
                     'ETH': data.asset_initial_2, 'XRP': data.asset_initial_2}
        for t in timeline:
            # Control function
            order = func.order_type(t['algo_output'])
            trade_amt, asset_amt, asset_value, portfolio_value = func.trade_token(order, token=t['token'],
                                                                                  asset_amt=asset_amt,
                                                                                  asset_price=t['asset_price'],
                                                                                  weight=data.weight_1,
                                                                                  fee=data.fee)
            # Test function
            price = t['asset_price']
            port.update_prices(price)
            port.update_portfolio()
            port.get_order_type(t['algo_output'], token=t['token'])
            port.trade_pair(t['token'], buy_fee=data.fee, sell_fee=data.fee)
            port.update_portfolio()

            self.assertEqual(trade_amt, port.trade_amt, 'Trade amount not updated correctly')
            self.assertDictEqual(t['asset_price'], port.asset_prices, 'Price dictionary not updated correctly')
            self.assertDictEqual(asset_amt, port.asset_amt, 'Asset amount dictionary not updated correctly')
            self.assertDictEqual(asset_value, port.asset_values, 'Asset values dictionary not updated correctly')
            self.assertEqual(portfolio_value, port.portfolio_value, 'Portfolio value not updated correctly')

    def test_three_tokens_3(self):
        """
        Test the functions of the process on 3 tokens.
        Uses weight_1 and fee
        """
        port = Portfolio(cash_initial=data.cash_initial_3, buy_weight=data.weight_1, sell_weight=data.weight_1)
        port.asset_amt['BTC'] = data.asset_initial_3
        port.asset_amt['ETH'] = data.asset_initial_3
        port.asset_amt['XRP'] = data.asset_initial_3

        timeline = data.data_4
        asset_amt = {'cash': data.cash_initial_3, 'BTC': data.asset_initial_3,
                     'ETH': data.asset_initial_3, 'XRP': data.asset_initial_3}
        for t in timeline:
            # Control function
            order = func.order_type(t['algo_output'])
            trade_amt, asset_amt, asset_value, portfolio_value = func.trade_token(order, token=t['token'],
                                                                                  asset_amt=asset_amt,
                                                                                  asset_price=t['asset_price'],
                                                                                  weight=data.weight_1,
                                                                                  fee=data.fee)
            # Test function
            price = t['asset_price']
            port.update_prices(price)
            port.update_portfolio()
            port.get_order_type(t['algo_output'], token=t['token'])
            port.trade_pair(t['token'], buy_fee=data.fee, sell_fee=data.fee)
            port.update_portfolio()

            self.assertEqual(trade_amt, port.trade_amt, 'Trade amount not updated correctly')
            self.assertDictEqual(t['asset_price'], port.asset_prices, 'Price dictionary not updated correctly')
            self.assertDictEqual(asset_amt, port.asset_amt, 'Asset amount dictionary not updated correctly')
            self.assertDictEqual(asset_value, port.asset_values, 'Asset values dictionary not updated correctly')
            self.assertEqual(portfolio_value, port.portfolio_value, 'Portfolio value not updated correctly')


if __name__ == '__main__':
    unittest.main()
