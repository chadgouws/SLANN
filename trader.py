import numpy as np
import pandas as pd


class Portfolio:

    def __init__(self, cash):
        self.cash = cash
        self.assets = 0
        self.capital = cash

        self.allocation = np.array([1, 0])                           # Initial allocation: 100% cash, 0% sin, 0% cos
        self.share_allocation = np.array([cash, 0])
        self.max_allocation = np.array([1, 1])
        self.min_allocation = np.array([0, 0])

        self.trade = 0
        self.prices = np.array([1, 0])

    def update_portfolio(self):
        self.cash = self.cash - np.multiply(self.trade, self.prices[1:])[0]
        self.assets = self.assets + self.trade

    def update_capital(self):
        self.capital = np.sum(np.multiply(self.share_allocation, self.prices))

    def calculate_shares(self):
        self.share_allocation = np.array([self.cash, self.assets])

    def update_allocation(self):                              # actions: buy = 1, sell = -1
        self.allocation = np.divide(np.multiply(self.share_allocation, self.prices), self.capital)

    def make_trade(self, action, price):
        if action > 0.5 and self.assets >= 0:
            action = 1
            no_of_shares = np.floor(np.divide(self.cash, price))
        elif action > 0.5 and self.assets < 0:
            action = 0
            no_of_shares = 0
        elif action <= 0.5 and self.assets > 0:
            action = -1
            no_of_shares = self.assets
        elif action <= 0.5 and self.assets <= 0:
            action = 0
            no_of_shares = 0
        else:
            action = 0
            no_of_shares = 0

        self.trade = np.multiply(action, no_of_shares)
        self.prices = np.array([1, price])


if __name__ == '__main__':

    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    p = Portfolio(100)
    actions = [  1,   1,  -1,   1,  -1,  -1,  -1,   1,  -1,   1,   1,   1,  -1,   1,  -1,  -1]
    prices =  [1.0, 1.1, 1.1, 1.2, 1.3, 1.1, 1.0, 1.2, 1.4, 1.3, 1.4, 1.5, 1.3, 1.2, 1.3, 1.4]
    data = []
    data.append([p.cash, p.assets, p.capital, p.share_allocation, p.prices, 0, p.trade, p.allocation])

    for i in range(len(actions)):
        p.make_trade(actions[i], prices[i])
        p.update_portfolio()
        p.calculate_shares()
        p.update_capital()
        p.update_allocation()
        data.append([p.cash, p.assets, p.capital, p.share_allocation, p.prices, actions[i], p.trade, p.allocation])

    df = pd.DataFrame(data, columns=['cash', 'assets', 'capital', 'share allocation', 'prices', 'action', 'trade', 'allocation'])
    print(df)
