import unittest

from portfolio.portfolio import Portfolio, PortfolioTimeline


class TestPortfolioUnits(unittest.TestCase):

    def test_calculate_asset_values_numeric(self):
        """
        The method should be able to use numeric values
        :return:
        """
        cash = 1000.0
        btc = 10.0
        eth = 15.0
        xrp = 12.9

        cash_price = 1.0
        btc_price = 21385.06
        eth_price = 3462.12
        xrp_price = 12.91

        port = Portfolio(cash_initial=cash)

        port.asset_amt['BTC'] = btc
        port.asset_amt['ETH'] = eth
        port.asset_amt['XRP'] = xrp

        port.asset_prices['cash'] = cash_price
        port.asset_prices['BTC'] = btc_price
        port.asset_prices['ETH'] = eth_price
        port.asset_prices['XRP'] = xrp_price

        port.calculate_asset_values()

        control_amt = {'cash': cash, 'BTC': btc, 'ETH': eth, 'XRP': xrp}
        control_prices = {'cash': cash_price, 'BTC': btc_price, 'ETH': eth_price, 'XRP': xrp_price}
        control_values = {k: control_amt[k] * control_prices[k] for k in control_amt}
        self.assertEqual(control_values, port.asset_values)

    def test_calculate_asset_values_string(self):
        """
        The method should be able to evaluate string values
        :return:
        """
        cash = 1000.0
        btc = 10.0
        eth = 15.0
        xrp = 12.9

        cash_price = 1.0
        btc_price = 21385.06
        eth_price = 3462.12
        xrp_price = 12.91

        port = Portfolio(cash_initial=cash)

        # Convert to string for test
        port.asset_amt['BTC'] = str(btc)
        port.asset_amt['ETH'] = str(eth)
        port.asset_amt['XRP'] = str(xrp)

        port.asset_prices['cash'] = str(cash_price)
        port.asset_prices['BTC'] = str(btc_price)
        port.asset_prices['ETH'] = str(eth_price)
        port.asset_prices['XRP'] = str(xrp_price)

        port.calculate_asset_values()

        control_amt = {'cash': cash, 'BTC': btc, 'ETH': eth, 'XRP': xrp}
        control_prices = {'cash': cash_price, 'BTC': btc_price, 'ETH': eth_price, 'XRP': xrp_price}
        control_values = {k: control_amt[k] * control_prices[k] for k in control_amt}
        self.assertEqual(control_values, port.asset_values)

    def test_calculate_asset_values_missing_price(self):
        """
        The method should be able to ignore missing data
        :return:
        """
        cash = 1000.0
        btc = 10.0
        eth = 15.0
        xrp = 12.9

        cash_price = 1.0
        btc_price = 21385.06
        eth_price = 3462.12
        xrp_price = 12.91

        port = Portfolio(cash_initial=cash)

        port.asset_amt['BTC'] = btc
        port.asset_amt['ETH'] = eth
        port.asset_amt['XRP'] = xrp

        port.asset_prices['cash'] = cash_price
        port.asset_prices['BTC'] = btc_price
        port.asset_prices['ETH'] = eth_price

        port.calculate_asset_values()

        control_amt = {'cash': cash, 'BTC': btc, 'ETH': eth}
        control_prices = {'cash': cash_price, 'BTC': btc_price, 'ETH': eth_price}
        control_values = {k: control_amt[k] * control_prices[k] for k in control_amt}
        self.assertEqual(control_values, port.asset_values)

    def test_calculate_portfolio_value_cash(self):
        c = 1000.0
        port = Portfolio(cash_initial=c)
        self.assertEqual(c, port.portfolio_value, 'Portfolio value is incorrect')

    def test_calculate_portfolio_value_two(self):
        c = 1000.0
        btc = 100.0

        port = Portfolio(cash_initial=c)
        port.asset_values['BTC'] = btc
        port.calculate_portfolio_value()

        total = c + btc
        self.assertEqual(total, port.portfolio_value, 'Portfolio value is incorrect')

    def test_calculate_portfolio_value_three(self):
        c = 1000.0
        btc = 100.0
        eth = 150.0

        port = Portfolio(cash_initial=c)
        port.asset_values['BTC'] = btc
        port.asset_values['ETH'] = eth
        port.calculate_portfolio_value()

        total = c + btc + eth
        self.assertEqual(total, port.portfolio_value, 'Portfolio value is incorrect')

    def test_calculate_portfolio_value_numeric(self):
        c = 1000.0
        btc = 100.0
        eth = 150.0
        xrp = 121.9

        port = Portfolio(cash_initial=c)
        port.asset_values['BTC'] = btc
        port.asset_values['ETH'] = eth
        port.asset_values['XRP'] = xrp
        port.calculate_portfolio_value()

        total = c + btc + eth + xrp
        self.assertEqual(total, port.portfolio_value, 'Portfolio value is incorrect')

    def test_calculate_portfolio_cash_value_string(self):
        """
        Initial cash must be converted to float type upon instantiation
        :return:
        """
        c = '1000.0'
        port = Portfolio(cash_initial=c)

        self.assertIsInstance(port.asset_values['cash'], float)

    """
    Test whether the model output is being converted into the correct buy, sell or hold signal
    SELL: [0.0:0.3)
    HOLD: [0.3:0.7]
    BUY:  (0.7:1.0]
    """

    def test_get_order_type_zero(self):
        port = Portfolio()
        port.get_order_type(0)
        self.assertEqual(port.order_type, port.sell)

    def test_get_order_type_1(self):
        port = Portfolio()
        port.get_order_type(0.1)
        self.assertEqual(port.order_type, port.sell)

    def test_get_order_type_299(self):
        port = Portfolio()
        port.get_order_type(0.29999)
        self.assertEqual(port.order_type, port.sell)

    def test_get_order_type_3(self):
        port = Portfolio()
        port.get_order_type(0.3)
        self.assertEqual(port.order_type, port.hold)

    def test_get_order_type_5(self):
        port = Portfolio()
        port.get_order_type(0.5)
        self.assertEqual(port.order_type, port.hold)

    def test_get_order_type_7(self):
        port = Portfolio()
        port.get_order_type(0.7)
        self.assertEqual(port.order_type, port.hold)

    def test_get_order_type_711(self):
        port = Portfolio()
        port.get_order_type(0.700001)
        self.assertEqual(port.order_type, port.buy)

    def test_get_order_type_9(self):
        port = Portfolio()
        port.get_order_type(0.9)
        self.assertEqual(port.order_type, port.buy)

    def test_get_order_type_one(self):
        port = Portfolio()
        port.get_order_type(1.0)
        self.assertEqual(port.order_type, port.buy)

    def test_get_order_type_string(self):
        port = Portfolio()
        output = '1.0'
        port.get_order_type(output)
        self.assertEqual(port.order_type, port.buy)

    def test_buy_weight_ceiling(self):
        """
        Trades should be checked to make sure they aren't worth more than 100%
        :return:
        """
        port = Portfolio(buy_weight=1.0)
        self.assertLessEqual(port.buy_weight, 1.0)

    def test_buy_weight_ceiling_above(self):
        """
        Trades should be checked to make sure they aren't worth more than 100%
        :return:
        """
        port = Portfolio(buy_weight=1.1)
        self.assertLessEqual(port.buy_weight, 1.0)

    def test_buy_weight_floor(self):
        """
        Trades should be checked to make sure they are greater than 0%
        :return:
        """
        port = Portfolio(buy_weight=0.0)
        self.assertGreater(port.buy_weight, 0.0)

    def test_sell_weight_ceiling(self):
        """
        Trades should be checked to make sure they aren't worth more than 100%
        :return:
        """
        port = Portfolio(sell_weight=1.0)
        self.assertLessEqual(port.sell_weight, 1.0)

    def test_sell_weight_ceiling_above(self):
        """
        Trades should be checked to make sure they aren't worth more than 100%
        :return:
        """
        port = Portfolio(sell_weight=1.1)
        self.assertLessEqual(port.buy_weight, 1.0)

    def test_sell_weight_floor(self):
        """
        Trades should be checked to make sure they are greater than 0%
        :return:
        """
        port = Portfolio(sell_weight=0.0)
        self.assertGreater(port.sell_weight, 0)

    def test_trade_pair_buy_not_enough_cash(self):
        btc = 'BTC'
        cash = 1000.0
        fee = 0.001
        port = Portfolio(cash_initial=cash, buy_weight=0.5, sell_weight=0.5)

        port.asset_amt[btc] = 1.0
        port.asset_prices[btc] = 5000.0
        port.portfolio_value = cash + port.asset_amt[btc] * port.asset_prices[btc]
        port.order_type = port.buy

        control = 0.0

        port.trade_pair(btc, buy_fee=fee)
        self.assertEqual(control, port.asset_amt['cash'])

    def test_trade_pair_buy_100_percent(self):
        """
        Maximum trade size is 100% of the cash
        :return:
        """
        btc = 'BTC'
        cash = 10000.0
        fee = 0.001
        port = Portfolio(cash_initial=cash, buy_weight=1.0, sell_weight=1.0)

        port.asset_amt[btc] = 0.0
        port.asset_prices[btc] = 5000.0
        port.portfolio_value = cash + port.asset_amt[btc] * port.asset_prices[btc]
        port.order_type = port.buy

        control = (1 - fee) * port.buy_weight * (cash / port.asset_prices[btc])

        port.trade_pair(btc, buy_fee=fee)
        self.assertEqual(control, port.asset_amt[btc])

    def test_trade_pair_buy_10_percent(self):
        """
        Can trade 10% of the portfolio
        :return:
        """
        btc = 'BTC'
        cash = 10000.0
        fee = 0.001
        port = Portfolio(cash_initial=cash, buy_weight=0.1, sell_weight=0.1)

        port.asset_amt[btc] = 0.0
        port.asset_prices[btc] = 5000.0
        port.portfolio_value = cash + port.asset_amt[btc] * port.asset_prices[btc]
        port.order_type = port.buy

        control = (1 - fee) * port.buy_weight * (cash / port.asset_prices[btc])

        port.trade_pair(btc, buy_fee=fee)
        self.assertEqual(control, port.asset_amt[btc])

    def test_trade_pair_buy_btc_amt(self):
        btc = 'BTC'
        cash = 10000.0
        fee = 0.001
        port = Portfolio(cash_initial=cash, buy_weight=1.0, sell_weight=1.0)

        port.asset_amt[btc] = 0.0
        port.asset_prices[btc] = 5000.0
        port.portfolio_value = cash + port.asset_amt[btc] * port.asset_prices[btc]
        port.order_type = port.buy

        control = (1 - fee) * port.buy_weight * (cash / port.asset_prices[btc])

        port.trade_pair(btc, buy_fee=fee)
        self.assertEqual(control, port.asset_amt[btc])

    def test_trade_pair_sell_100_percent(self):
        """
        Maximum trade size is 100% of the portfolio
        :return:
        """
        btc = 'BTC'
        cash = 0.0
        fee = 0.001
        port = Portfolio(cash_initial=cash, buy_weight=1.0, sell_weight=1.0)

        port.asset_amt[btc] = 1.0
        port.asset_prices[btc] = 5000.0
        port.portfolio_value = cash + port.asset_amt[btc] * port.asset_prices[btc]
        port.order_type = port.sell

        control = (1 - fee) * (cash + port.sell_weight * port.asset_prices[btc] * port.asset_amt[btc])

        port.trade_pair(btc, sell_fee=fee)
        self.assertEqual(control, port.asset_amt['cash'])

    def test_trade_pair_sell_10_percent(self):
        """
        Can trade 10% of the portfolio
        :return:
        """
        btc = 'BTC'
        cash = 0.0
        fee = 0.001
        port = Portfolio(cash_initial=cash, buy_weight=0.1, sell_weight=0.1)

        port.asset_amt[btc] = 1.0
        port.asset_prices[btc] = 5000.0
        port.portfolio_value = cash + port.asset_amt[btc] * port.asset_prices[btc]
        port.order_type = port.sell

        control = (1 - fee) * (cash + port.sell_weight * port.asset_prices[btc] * port.asset_amt[btc])

        port.trade_pair(btc, sell_fee=fee)
        self.assertEqual(control, port.asset_amt['cash'])

    def test_trade_pair_sell_btc_amt(self):
        btc = 'BTC'
        cash = 0.0
        fee = 0.001
        port = Portfolio(cash_initial=cash, buy_weight=1.0, sell_weight=1.0)

        port.asset_amt[btc] = 1.0
        port.asset_prices[btc] = 5000.0
        port.portfolio_value = cash + port.asset_amt[btc] * port.asset_prices[btc]
        port.order_type = port.sell

        control = (1 - fee) * (cash + port.sell_weight * port.asset_prices[btc] * port.asset_amt[btc])

        port.trade_pair(btc, sell_fee=fee)
        self.assertEqual(control, port.asset_amt['cash'])

    def test_update_prices_numeric(self):
        c = 1000.0

        price = {'BTC': 21002.31, 'ETH': 3214.01, 'XRP': 12.31}

        port = Portfolio(cash_initial=c)
        port.update_prices(price)
        price['cash'] = 1.0

        self.assertEqual(price, port.asset_prices, 'Asset prices were not updated correctly')

    def test_update_prices_string(self):
        c = 1000.0

        price = {'BTC': '21002.31', 'ETH': '3214.01', 'XRP': '12.31'}
        for asset in price.keys():
            price[asset] = float(price[asset])

        port = Portfolio(cash_initial=c)
        port.update_prices(price)

        price['cash'] = 1.0
        self.assertEqual(price, port.asset_prices, 'Asset prices were not updated correctly')


class TestPortfolioTimeline(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
