import unittest

from portfolio.portfolio import Portfolio


class TestPortfolioIntegration(unittest.TestCase):

    def test_buy_some_cash_some_btc(self):
        token = 'BTC'
        asset_amt = {'cash': 1000.0, token: 1.0}
        asset_value = {'cash': 1000.0, token: 1000.0}
        asset_price = {'cash': 1.0, token: 1000.0}
        portfolio_value = sum(asset_value.values())

        weight = 0.1
        fee = 0.001
        order = 1.0

        port = Portfolio(cash_initial=asset_amt['cash'], buy_weight=weight, sell_weight=weight)
        port.asset_amt[token] = 1.0

        price = {token: asset_price[token]}
        port.update_prices(price)
        port.update_portfolio()
        port.get_order_type(order, token=token)
        port.trade_pair(token, buy_fee=fee, sell_fee=fee)
        port.update_portfolio()

        if asset_amt['cash'] > 0:
            trade_amt = weight * portfolio_value
        else:
            trade_amt = 0.0

        asset_amt['cash'] = asset_amt['cash'] - trade_amt
        asset_amt[token] = asset_amt[token] + (1 - fee) * trade_amt / asset_price[token]

        asset_value['cash'] = asset_amt['cash'] * asset_price['cash']
        asset_value[token] = asset_amt[token] * asset_price[token]
        portfolio_value = sum(asset_value.values())

        self.assertEqual(trade_amt, port.trade_amt, 'Trade amount not updated correctly')
        self.assertDictEqual(asset_price, port.asset_prices, 'Price dictionary not updated correctly')
        self.assertDictEqual(asset_amt, port.asset_amt, 'Asset amount dictionary not updated correctly')
        self.assertDictEqual(asset_value, port.asset_values, 'Asset values dictionary not updated correctly')
        self.assertEqual(portfolio_value, port.portfolio_value, 'Portfolio value not updated correctly')

    def test_buy_some_cash_zero_btc(self):
        token = 'BTC'
        asset_amt = {'cash': 1000.0, token: 0.0}
        asset_value = {'cash': 1000.0, token: 0.0}
        asset_price = {'cash': 1.0, token: 1000.0}
        portfolio_value = sum(asset_value.values())

        weight = 0.1
        fee = 0.001
        order = 1.0

        port = Portfolio(cash_initial=asset_amt['cash'], buy_weight=weight, sell_weight=weight)

        price = {token: asset_price[token]}
        port.update_prices(price)
        port.get_order_type(order, token=token)
        port.trade_pair(token, buy_fee=fee, sell_fee=fee)
        port.update_portfolio()

        if asset_amt['cash'] > 0:
            trade_amt = weight * portfolio_value
        else:
            trade_amt = 0.0

        asset_amt['cash'] = asset_amt['cash'] - trade_amt
        asset_amt[token] = asset_amt[token] + (1 - fee) * trade_amt / asset_price[token]

        asset_value['cash'] = asset_amt['cash'] * asset_price['cash']
        asset_value[token] = asset_amt[token] * asset_price[token]
        portfolio_value = sum(asset_value.values())

        self.assertEqual(trade_amt, port.trade_amt, 'Trade amount not updated correctly')
        self.assertDictEqual(asset_price, port.asset_prices, 'Price dictionary not updated correctly')
        self.assertDictEqual(asset_amt, port.asset_amt, 'Asset amount dictionary not updated correctly')
        self.assertDictEqual(asset_value, port.asset_values, 'Asset values dictionary not updated correctly')
        self.assertEqual(portfolio_value, port.portfolio_value, 'Portfolio value not updated correctly')

    def test_buy_zero_cash_some_btc(self):
        token = 'BTC'
        asset_amt = {'cash': 0.0, token: 1.0}
        asset_value = {'cash': 0.0, token: 1000.0}
        asset_price = {'cash': 1.0, token: 1000.0}
        portfolio_value = sum(asset_value.values())

        weight = 0.1
        fee = 0.001
        order = 1.0

        port = Portfolio(cash_initial=asset_amt['cash'], buy_weight=weight, sell_weight=weight)
        port.asset_amt[token] = 1.0

        price = {token: asset_price[token]}
        port.update_prices(price)
        port.update_portfolio()
        port.get_order_type(order, token=token)
        port.trade_pair(token, buy_fee=fee, sell_fee=fee)
        port.update_portfolio()

        if asset_amt['cash'] > 0:
            trade_amt = weight * portfolio_value
        else:
            trade_amt = 0.0

        asset_amt['cash'] = asset_amt['cash'] - trade_amt
        asset_amt[token] = asset_amt[token] + (1 - fee) * trade_amt / asset_price[token]

        asset_value['cash'] = asset_amt['cash'] * asset_price['cash']
        asset_value[token] = asset_amt[token] * asset_price[token]
        portfolio_value = sum(asset_value.values())

        self.assertEqual(trade_amt, port.trade_amt, 'Trade amount not updated correctly')
        self.assertDictEqual(asset_price, port.asset_prices, 'Price dictionary not updated correctly')
        self.assertDictEqual(asset_amt, port.asset_amt, 'Asset amount dictionary not updated correctly')
        self.assertDictEqual(asset_value, port.asset_values, 'Asset values dictionary not updated correctly')
        self.assertEqual(portfolio_value, port.portfolio_value, 'Portfolio value not updated correctly')

    def test_buy_zero_cash_zero_btc(self):
        token = 'BTC'
        asset_amt = {'cash': 0.0, token: 0.0}
        asset_value = {'cash': 0.0, token: 0.0}
        asset_price = {'cash': 1.0, token: 1000.0}
        portfolio_value = sum(asset_value.values())

        weight = 0.1
        fee = 0.001
        order = 1.0

        port = Portfolio(cash_initial=asset_amt['cash'], buy_weight=weight, sell_weight=weight)

        price = {token: asset_price[token]}
        port.update_prices(price)
        port.update_portfolio()
        port.get_order_type(order, token=token)
        port.trade_pair(token, buy_fee=fee, sell_fee=fee)
        port.update_portfolio()

        if asset_amt['cash'] > 0:
            trade_amt = weight * portfolio_value
        else:
            trade_amt = 0.0

        asset_amt['cash'] = asset_amt['cash'] - trade_amt
        asset_amt[token] = asset_amt[token] + (1 - fee) * trade_amt / asset_price[token]

        asset_value['cash'] = asset_amt['cash'] * asset_price['cash']
        asset_value[token] = asset_amt[token] * asset_price[token]
        portfolio_value = sum(asset_value.values())

        self.assertEqual(trade_amt, port.trade_amt, 'Trade amount not updated correctly')
        self.assertDictEqual(asset_price, port.asset_prices, 'Price dictionary not updated correctly')
        self.assertDictEqual(asset_amt, port.asset_amt, 'Asset amount dictionary not updated correctly')
        self.assertDictEqual(asset_value, port.asset_values, 'Asset values dictionary not updated correctly')
        self.assertEqual(portfolio_value, port.portfolio_value, 'Portfolio value not updated correctly')

    def test_sell_some_cash_some_btc(self):
        token = 'BTC'
        asset_amt = {'cash': 1000.0, token: 1.0}
        asset_value = {'cash': 1000.0, token: 1000.0}
        asset_price = {'cash': 1.0, token: 1000.0}
        portfolio_value = sum(asset_value.values())

        weight = 0.1
        fee = 0.001
        order = 0.0

        port = Portfolio(cash_initial=asset_amt['cash'], buy_weight=weight, sell_weight=weight)
        port.asset_amt[token] = asset_amt[token]

        price = {token: asset_price[token]}
        port.update_prices(price)
        port.update_portfolio()
        port.get_order_type(order, token=token)
        port.trade_pair(token, buy_fee=fee, sell_fee=fee)
        port.update_portfolio()

        if asset_amt[token] > 0:
            trade_amt = weight * portfolio_value / asset_price[token]
        else:
            trade_amt = 0.0

        asset_amt[token] = asset_amt[token] - trade_amt
        asset_amt['cash'] = asset_amt['cash'] + (1 - fee) * trade_amt * asset_price[token]

        asset_value['cash'] = asset_amt['cash'] * asset_price['cash']
        asset_value[token] = asset_amt[token] * asset_price[token]
        portfolio_value = sum(asset_value.values())

        self.assertEqual(trade_amt, port.trade_amt, 'Trade amount not updated correctly')
        self.assertDictEqual(asset_price, port.asset_prices, 'Price dictionary not updated correctly')
        self.assertDictEqual(asset_amt, port.asset_amt, 'Asset amount dictionary not updated correctly')
        self.assertDictEqual(asset_value, port.asset_values, 'Asset values dictionary not updated correctly')
        self.assertEqual(portfolio_value, port.portfolio_value, 'Portfolio value not updated correctly')

    def test_sell_some_cash_zero_btc(self):
        token = 'BTC'
        asset_amt = {'cash': 1000.0, token: 1.0}
        asset_value = {'cash': 1000.0, token: 1000.0}
        asset_price = {'cash': 1.0, token: 1000.0}
        portfolio_value = sum(asset_value.values())

        weight = 0.1
        fee = 0.001
        order = 0.0

        port = Portfolio(cash_initial=asset_amt['cash'], buy_weight=weight, sell_weight=weight)
        port.asset_amt[token] = asset_amt[token]

        price = {token: asset_price[token]}
        port.update_prices(price)
        port.update_portfolio()
        port.get_order_type(order, token=token)
        port.trade_pair(token, buy_fee=fee, sell_fee=fee)
        port.update_portfolio()

        if asset_amt[token] > 0:
            trade_amt = weight * portfolio_value / asset_price[token]
        else:
            trade_amt = 0.0

        asset_amt[token] = asset_amt[token] - trade_amt
        asset_amt['cash'] = asset_amt['cash'] + (1 - fee) * trade_amt * asset_price[token]

        asset_value['cash'] = asset_amt['cash'] * asset_price['cash']
        asset_value[token] = asset_amt[token] * asset_price[token]
        portfolio_value = sum(asset_value.values())

        self.assertEqual(trade_amt, port.trade_amt, 'Trade amount not updated correctly')
        self.assertDictEqual(asset_price, port.asset_prices, 'Price dictionary not updated correctly')
        self.assertDictEqual(asset_amt, port.asset_amt, 'Asset amount dictionary not updated correctly')
        self.assertDictEqual(asset_value, port.asset_values, 'Asset values dictionary not updated correctly')
        self.assertEqual(portfolio_value, port.portfolio_value, 'Portfolio value not updated correctly')

    def test_sell_zero_cash_some_btc(self):
        token = 'BTC'
        asset_amt = {'cash': 1000.0, token: 1.0}
        asset_value = {'cash': 1000.0, token: 1000.0}
        asset_price = {'cash': 1.0, token: 1000.0}
        portfolio_value = sum(asset_value.values())

        weight = 0.1
        fee = 0.001
        order = 0.0

        port = Portfolio(cash_initial=asset_amt['cash'], buy_weight=weight, sell_weight=weight)
        port.asset_amt[token] = asset_amt[token]

        price = {token: asset_price[token]}
        port.update_prices(price)
        port.update_portfolio()
        port.get_order_type(order, token=token)
        port.trade_pair(token, buy_fee=fee, sell_fee=fee)
        port.update_portfolio()

        if asset_amt[token] > 0:
            trade_amt = weight * portfolio_value / asset_price[token]
        else:
            trade_amt = 0.0

        asset_amt[token] = asset_amt[token] - trade_amt
        asset_amt['cash'] = asset_amt['cash'] + (1 - fee) * trade_amt * asset_price[token]

        asset_value['cash'] = asset_amt['cash'] * asset_price['cash']
        asset_value[token] = asset_amt[token] * asset_price[token]
        portfolio_value = sum(asset_value.values())

        self.assertEqual(trade_amt, port.trade_amt, 'Trade amount not updated correctly')
        self.assertDictEqual(asset_price, port.asset_prices, 'Price dictionary not updated correctly')
        self.assertDictEqual(asset_amt, port.asset_amt, 'Asset amount dictionary not updated correctly')
        self.assertDictEqual(asset_value, port.asset_values, 'Asset values dictionary not updated correctly')
        self.assertEqual(portfolio_value, port.portfolio_value, 'Portfolio value not updated correctly')

    def test_sell_zero_cash_zero_btc(self):
        token = 'BTC'
        asset_amt = {'cash': 1000.0, token: 1.0}
        asset_value = {'cash': 1000.0, token: 1000.0}
        asset_price = {'cash': 1.0, token: 1000.0}
        portfolio_value = sum(asset_value.values())

        weight = 0.1
        fee = 0.001
        order = 0.0

        port = Portfolio(cash_initial=asset_amt['cash'], buy_weight=weight, sell_weight=weight)
        port.asset_amt[token] = asset_amt[token]

        price = {token: asset_price[token]}
        port.update_prices(price)
        port.update_portfolio()
        port.get_order_type(order, token=token)
        port.trade_pair(token, buy_fee=fee, sell_fee=fee)
        port.update_portfolio()

        if asset_amt[token] > 0:
            trade_amt = weight * portfolio_value / asset_price[token]
        else:
            trade_amt = 0.0

        asset_amt[token] = asset_amt[token] - trade_amt
        asset_amt['cash'] = asset_amt['cash'] + (1 - fee) * trade_amt * asset_price[token]

        asset_value['cash'] = asset_amt['cash'] * asset_price['cash']
        asset_value[token] = asset_amt[token] * asset_price[token]
        portfolio_value = sum(asset_value.values())

        self.assertEqual(trade_amt, port.trade_amt, 'Trade amount not updated correctly')
        self.assertDictEqual(asset_price, port.asset_prices, 'Price dictionary not updated correctly')
        self.assertDictEqual(asset_amt, port.asset_amt, 'Asset amount dictionary not updated correctly')
        self.assertDictEqual(asset_value, port.asset_values, 'Asset values dictionary not updated correctly')
        self.assertEqual(portfolio_value, port.portfolio_value, 'Portfolio value not updated correctly')

    def test_hold_some_cash_some_btc(self):
        token = 'BTC'
        asset_amt = {'cash': 1000.0, token: 1.0}
        asset_value = {'cash': 1000.0, token: 1000.0}
        asset_price = {'cash': 1.0, token: 1000.0}
        portfolio_value = sum(asset_value.values())

        weight = 0.1
        fee = 0.001
        order = 0.5

        port = Portfolio(cash_initial=asset_amt['cash'], buy_weight=weight, sell_weight=weight)
        port.asset_amt[token] = asset_amt[token]

        price = {token: asset_price[token]}
        port.update_prices(price)
        port.update_portfolio()
        port.get_order_type(order, token=token)
        port.trade_pair(token, buy_fee=fee, sell_fee=fee)
        port.update_portfolio()

        trade_amt = 0.0
        asset_amt[token] = asset_amt[token] - trade_amt
        asset_amt['cash'] = asset_amt['cash'] + (1 - fee) * trade_amt * asset_price[token]

        asset_value['cash'] = asset_amt['cash'] * asset_price['cash']
        asset_value[token] = asset_amt[token] * asset_price[token]
        portfolio_value = sum(asset_value.values())

        self.assertEqual(trade_amt, port.trade_amt, 'Trade amount not updated correctly')
        self.assertDictEqual(asset_price, port.asset_prices, 'Price dictionary not updated correctly')
        self.assertDictEqual(asset_amt, port.asset_amt, 'Asset amount dictionary not updated correctly')
        self.assertDictEqual(asset_value, port.asset_values, 'Asset values dictionary not updated correctly')
        self.assertEqual(portfolio_value, port.portfolio_value, 'Portfolio value not updated correctly')


class TestPortfolioTimelineIntegration:
    pass


if __name__ == '__main__':
    unittest.main()
