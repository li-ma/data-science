""" CAPM and Technology Analysis """


# Market Index:
# USA: S&P500
# UK: FTA
# JAPAN: TOPIX


def momentum(price):
    # n: 1 day, 5 days, 10 days, etc.
    return (float)(price[t1+n] / price[t1]) - 1.0


def simple_moving_average(price):
    # proxy for value
    # arbitrage opportunity
    # n: last n days window
    return (float)(price[t1] / price[t1-n:t1].mean()) - 1.0


def bollinger_bands(price):
    # look for cross from outside to inside, towards the SMA
    # vice versa
    # > 1.0 or < -1.0
    return (price[t] - sma[t]) / (2.0 * price.std()[t])
