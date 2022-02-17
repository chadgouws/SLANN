from portfolio.tests import data


def order_type(algo_output):
    if algo_output > 0.7:
        return 'BUY'
    elif algo_output < 0.3:
        return 'SELL'
    else:
        return 'HOLD'


def trade_token(order, token=None, asset_amt=None, asset_price=None, weight=None, fee=None):
    # Update portfolio
    asset_value = {k: asset_price[k] * asset_amt[k] for k in asset_amt if k in asset_price.keys()}
    portfolio_value = sum(asset_value.values())

    # Make market order
    if order == 'BUY':
        trade_amt = weight * portfolio_value
        if trade_amt > asset_amt['cash']:
            trade_amt = asset_amt['cash']
        else:
            pass
        asset_amt[token] = asset_amt[token] + (1 - fee) * (trade_amt / asset_price[token])
        asset_amt['cash'] = asset_amt['cash'] - trade_amt

    elif order == 'SELL':
        trade_amt = weight * portfolio_value / asset_price[token]
        if trade_amt > asset_amt[token]:
            trade_amt = asset_amt[token]
        else:
            trade_amt = trade_amt
        asset_amt['cash'] = asset_amt['cash'] + (1 - fee) * trade_amt * asset_price[token]
        asset_amt[token] = asset_amt[token] - trade_amt

    else:
        trade_amt = 0

    # Update portfolio
    asset_value = {k: asset_price[k] * asset_amt[k] for k in asset_amt if k in asset_price.keys()}
    portfolio_value = sum(asset_value.values())

    return trade_amt, asset_amt, asset_value, portfolio_value


if __name__ == '__main__':
    timeline = data.data_2

    for t in timeline:
        order = order_type(t['algo_output'])
        trade_amt, asset_amt, asset_value, portfolio_value = trade_token(order, token=t['token'],
                                                                         asset_amt=t['asset_amt'],
                                                                         asset_price=t['asset_price'],
                                                                         weight=data.weight_1, fee=data.fee)

        print(t['token'])
        print(asset_amt, '\n')
