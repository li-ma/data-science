import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def normalize_data(df):
    return df / df.ix[0]


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(symbol),
                              index_col='Date',
                              parse_dates=True,
                              usecols=['Date', 'Adj Close'],
                              na_values=['nan'])
        # start left join
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp, how="left")
        df = df.dropna()
    return df


def plot_data(df, title="Stock Price"):
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Price")
    ax.set_ylabel("Date")
    plt.show()


def test1():
    # Define a date range
    dates = pd.date_range('2017-10-13', '2017-11-13')

    # Choose stock symbols to read
    symbols = ['JD', 'DIS', 'BABA']

    # Get stock data
    df = get_data(symbols, dates)

    print df
    print df.mean()
    print df.median()
    print df.std()


def main():
    # Define a date range
    dates = pd.date_range('2016-12-13', '2017-12-13')

    # Choose stock symbols to read
    symbols = ['JD']

    # Get stock data
    df = get_data(symbols, dates)
    print df['JD']

    ax = df['JD'].plot(title="JD rolling mean", label="JD")

    # rolling mean
    # rm_jd = pd.rolling_mean(df['JD'], window=20)
    rm_jd = df['JD'].rolling(20).mean()
    rm_jd.plot(label="Rolling mean", ax=ax)

    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')

    plt.show()





if __name__ == "__main__":
    main()
