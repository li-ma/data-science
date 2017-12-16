"""Daily Returns"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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
    dr.ix[0, :] = 0
    return dr


def compute_cumulative_returns(df):
    """Compute and return the cumulative return values."""
    # Note: Returned DataFrame must have the same number of rows
    return (df / df.ix[0]) - 1.0


def test_histogram():
    # Read data
    dates = pd.date_range('2016-11-12', '2017-12-13')
    symbols = ['JD', 'BABA']
    df = get_data(symbols, dates)

    # Compute Daily Returns
    daily_returns = compute_daily_returns(df)
    daily_returns['JD'].hist(bins=20, label='JD')
    mean = daily_returns['JD'].mean()
    std = daily_returns['JD'].std()
    plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    # daily_returns['BABA'].hist(bins=20, label='BABA')
    plt.legend(loc='upper right')
    print daily_returns.kurtosis()
    plt.show()


def test_scatterplot():
    # Read data
    dates = pd.date_range('2016-11-12', '2017-12-13')
    symbols = ['JD', 'BABA']
    df = get_data(symbols, dates)

    # Compute Daily Returns
    daily_returns = compute_daily_returns(df)

    daily_returns.plot(kind='scatter', x='SPY', y='JD')
    beta_JD, alpha_JD = np.polyfit(daily_returns['SPY'], daily_returns['JD'], 1)
    plt.plot(daily_returns['SPY'], beta_JD * daily_returns['SPY'] + alpha_JD, '-', color='r')
    print "beta-JD: ", beta_JD
    print "alpha-JD: ", alpha_JD
    plt.show()

    daily_returns.plot(kind='scatter', x='SPY', y='BABA')
    beta_BA, alpha_BA = np.polyfit(daily_returns['SPY'], daily_returns['BABA'], 1)
    plt.plot(daily_returns['SPY'], beta_BA * daily_returns['SPY'] + alpha_BA, '-', color='r')
    print "beta-BABA: ", beta_BA
    print "alpha-BABA: ", alpha_BA
    plt.show()

    print daily_returns.corr(method='pearson')


if __name__ == "__main__":
    test_histogram()