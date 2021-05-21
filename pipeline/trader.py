import numpy as np

from pipeline.prepare_data import moving_average


class Portfolio:

    def __init__(self, cash):
        self.cash = cash
        self.coins = 0
        self.capital = cash

        self.allocation = np.array([1, 0])                           # Initial allocation: 100% cash, 0% sin, 0% cos
        self.share_allocation = np.array([cash, 0])
        self.max_allocation = np.array([1, 1])
        self.min_allocation = np.array([0, 0])

        self.trade = 0
        self.prices = np.array([1, 0])

    def update_portfolio(self):
        self.cash = self.cash - np.multiply(self.trade, self.prices[1:])[0]
        self.coins = self.coins + self.trade

    def update_capital(self):
        self.capital = np.sum(np.multiply(self.share_allocation, self.prices))

    def calculate_shares(self):
        self.share_allocation = np.array([self.cash, self.coins])

    def update_allocation(self):                              # actions: buy = 1, sell = -1
        self.allocation = np.divide(np.multiply(self.share_allocation, self.prices), self.capital)

    def make_trade(self, action, price):
        if action > 0.5 and self.coins >= 0:
            action = 1
            no_of_coins = np.divide(self.cash, price)
        elif action > 0.5 and self.coins < 0:
            action = 0
            no_of_coins = 0
        elif action <= 0.5 and self.coins > 0:
            action = -1
            no_of_coins = self.coins
        elif action <= 0.5 and self.coins <= 0:
            action = 0
            no_of_coins = 0
        else:
            action = 0
            no_of_coins = 0

        self.trade = np.multiply(action, no_of_coins)
        self.prices = np.array([1, price])


class LunoPortfolio:

    def __init__(self):
        self.buy = 'BUY'
        self.sell = 'SELL'
        self.none = 'NONE'
        self.type = self.none
        self.sma_9 = 0
        self.sma_26 = 0
        self.sma_50 = 0

    def sma_2(self, prices, sma_9, sma_26):
        self.sma_9 = moving_average(prices, 9)
        self.sma_26 = moving_average(prices, 26)
        if self.sma_9 > self.sma_26 and sma_9 <= sma_26:
            self.type = self.buy
        elif self.sma_9 < self.sma_26 and sma_9 >= sma_26:
            self.type = self.sell
        else:
            self.type = self.none
        return self.type

    def sma_3(self, prices):
        self.sma_9 = moving_average(prices, 9)
        self.sma_26 = moving_average(prices, 26)
        self.sma_50 = moving_average(prices, 50)
        if self.sma_9 > self.sma_26 > self.sma_50 and self.sma_9 > self.sma_50:
            self.type = self.buy
        elif self.sma_9 < self.sma_26:
            self.type = self.sell
        elif self.sma_9 < self.sma_50:
            self.type = self.sell
        else:
            self.type = self.none
        return self.type


class ResearchPortfolio:

    def __init__(self):
        self.buy = 'BUY'
        self.sell = 'SELL'
        self.none = 'NONE'
        self.batch_size = 30
        self.type = []
        self.coin = [0] * self.batch_size
        self.cash = [1000] * self.batch_size

    def make_market_order(self, price):
        for t in range(0, len(self.type)):
            if self.type[t] == 'BUY' and self.cash[t] > 0:
                self.coin[t] = self.cash[t] / price[t]
                self.cash[t] = 0
            elif self.type[t] == 'SELL' and self.coin[t] > 0:
                self.cash[t] = price[t] * self.coin[t]
                self.coin[t] = 0
            else:
                pass

    def order_type(self, algo_output):
        self.type = []
        for a in algo_output:
            if a > 0.7:
                self.type.append(self.buy)
            elif a < 0.3:
                self.type.append(self.sell)
            else:
                self.type.append(self.none)


if __name__ == '__main__':
    rp = ResearchPortfolio()
    n = np.random.rand(1, 10)[0]
    p = np.random.rand(1, 10)[0]

    rp.order_type(n)
    rp.make_market_order(p)
    print(rp.cash)
    print(rp.coin)
