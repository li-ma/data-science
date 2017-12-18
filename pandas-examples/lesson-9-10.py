"""Portfolio Optimizer"""

import math
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spo


def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                              parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])
    return df


def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


def compute_daily_returns(df):
    """Compute and return the daily return values."""
    # Note: Returned DataFrame must have the same number of rows
    dr = (df / df.shift(1)) - 1.0
    # dr.ix[0, :] = 0
    return dr


def compute_cumulative_returns(df):
    """Compute and return the cumulative return values."""
    # Note: Returned DataFrame must have the same number of rows
    return (df / df.ix[0]) - 1.0


def normalize_data(df):
    return df / df.ix[0]


def test_optimizer():
    # f(x) = -1 * sharpe ratio
    # initial x = allocation of stocks
    # range x = [0, 1]
    # constraints x: sum(x) = 1.0
    pass


def fx(allocs):
    # Read data
    dates = pd.date_range('2016-11-12', '2017-11-12')
    symbols = ['JD', 'BABA', 'DIS']
    df = get_data(symbols, dates)
    start_val = 100000

    normed = normalize_data(df)
    alloced = normed * allocs
    pos_vals = alloced * start_val
    port_val = pos_vals.sum(axis=1)

    # Compute Daily Returns
    daily_returns = compute_daily_returns(port_val)
    avg_daily_returns = daily_returns.mean()
    std_daily_returns_risk = daily_returns.std()
    daily_risk_free = math.log(1.0 + 0.1, 252) - 1.0
    sampling_rate = math.sqrt(252)  # weekly: 52, monthly: 12
    sharpe_ratio = sampling_rate * (avg_daily_returns - daily_risk_free) / std_daily_returns_risk
    return sharpe_ratio * (-1.0)


def test_portfolio():
    # Model portfolio
    allocs = [0.2, 0.2, 0.3, 0.3]

    min_result = spo.minimize(fx,
                              allocs,
                              method='SLSQP',
                              bounds=((0.0, 1.0), (0.0, 1.0), (0.0, 1.0), (0.0, 1.0)),
                              constraints=({'type': 'eq', 'fun': lambda x:  x[0] + x[1] + x[2] + x[3] - 1.0},),
                              options={'disp': True})
    print 'Sharpe Ratio: ', min_result


if __name__ == "__main__":
    test_portfolio()