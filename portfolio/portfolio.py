import datetime


class Portfolio:

    """
    The Portfolio class is the portfolio's holdings at a point in time, a snapshot of what
    assets are held and how much. It can take in buy or sell signals, use those to
    make trades and update itself.

    The Portfolio class is designed to work in tandem with PortfolioTimeline,
    which takes each snapshot of a portfolio and builds a timeline of how the portfolio changes
    over time.
    """

    def __init__(self, cash_initial=1000.0, buy_weight=0.1, sell_weight=0.1):
        self.asset_amt = {'cash': float(cash_initial)}
        self.asset_values = {}
        self.asset_prices = {'cash': 1.0}
        self.portfolio_value = self.asset_amt['cash']
        self.buy_weight = buy_weight
        self.sell_weight = sell_weight
        self.buy = 'BUY'
        self.sell = 'SELL'
        self.hold = 'HOLD'
        self.order_type = self.hold
        self.trade_amt = 0.0
        self.current_datetime = datetime.datetime.now()
        self.check_buy_weight()
        self.check_sell_weight()
        self.calculate_asset_values()

    def check_buy_weight(self):
        if self.buy_weight > 1.0:
            self.buy_weight = 1.0
        elif self.buy_weight <= 0.0:
            self.buy_weight = 0.01
        else:
            pass

    def check_sell_weight(self):
        if self.sell_weight > 1.0:
            self.sell_weight = 1.0
        elif self.sell_weight <= 0.0:
            self.sell_weight = 0.01
        else:
            pass

    def calculate_asset_values(self):
        self.asset_values = {k: float(self.asset_amt[k]) * float(self.asset_prices[k])
                             for k in self.asset_amt if k in self.asset_amt and k in self.asset_prices}

    def calculate_portfolio_value(self):
        self.portfolio_value = sum(self.asset_values.values())

    def get_order_type(self, algo_output, token=None):
        if token:
            if token not in self.asset_amt:
                self.asset_amt[token] = 0.0

        if isinstance(algo_output, str):
            algo_output = float(algo_output)

        if algo_output > 0.7:
            self.order_type = self.buy
        elif algo_output < 0.3:
            self.order_type = self.sell
        else:
            self.order_type = self.hold

    def trade_pair(self, token=None, buy_fee=0.001, sell_fee=0.001):
        if self.order_type == self.buy:
            trade_amt = self.buy_weight * self.portfolio_value
            if trade_amt <= self.asset_amt['cash']:
                self.trade_amt = trade_amt
            else:
                self.trade_amt = self.asset_amt['cash']
            self.asset_amt[token] = self.asset_amt[token] + (1 - buy_fee) * (self.trade_amt / self.asset_prices[token])
            self.asset_amt['cash'] = self.asset_amt['cash'] - self.trade_amt

        elif self.order_type == self.sell:
            trade_amt = self.sell_weight * self.portfolio_value / self.asset_prices[token]
            if trade_amt <= self.asset_amt[token]:
                self.trade_amt = trade_amt
            else:
                self.trade_amt = self.asset_amt[token]
            self.asset_amt['cash'] = self.asset_amt['cash'] + (1 - sell_fee) * (self.trade_amt * self.asset_prices[token])
            self.asset_amt[token] = self.asset_amt[token] - self.trade_amt
        else:
            self.trade_amt = 0

    def update_portfolio(self):
        self.calculate_asset_values()
        self.calculate_portfolio_value()

    def update_prices(self, price, current_datetime=datetime.datetime.now()):
        """
        Update the price of each asset using the given dictionary
        :param current_datetime:
        :param price:
        :return:
        """
        self.current_datetime = current_datetime
        for asset in price.keys():
            if isinstance(price[asset], str):
                self.asset_prices[asset] = float(price[asset])
            else:
                self.asset_prices[asset] = price[asset]
