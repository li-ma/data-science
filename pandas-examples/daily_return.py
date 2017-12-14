"""Daily Returns"""

import os
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


def compute_daily_returns1(df):
    """Compute and return the daily return values."""
    # Note: Returned DataFrame must have the same number of rows
    dr = df.copy()  # match size and column name
    # compute daily return for row 1 onwards
    dr[1:] = (df[1:] / df[:-1].values) - 1.0
    # set daily returns for row 0 to 0
    dr.ix[0, :] = 0
    return dr


def compute_daily_returns2(df):
    """Compute and return the daily return values."""
    # Note: Returned DataFrame must have the same number of rows
    dr = (df / df.shift(1)) - 1.0
    dr.ix[0, :] = 0
    return dr


def compute_cumulative_returns(df):
    """Compute and return the cumulative return values."""
    # Note: Returned DataFrame must have the same number of rows
    return (df / df.ix[0]) - 1.0


def test_run():
    # Read data
    dates = pd.date_range('2017-11-12', '2017-12-13')
    symbols = ['JD', 'BABA']
    df = get_data(symbols, dates)

    # Compute Daily Returns
    daily_returns = compute_cumulative_returns(df)
    plot_data(daily_returns, title="Cumulative returns", ylabel="Cumulative returns")


if __name__ == "__main__":
    test_run()