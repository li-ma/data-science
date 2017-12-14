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


def test_run1(start, end):
    dates = pd.date_range(start, end)
    df1 = pd.DataFrame(index=dates)
    for name in ['JD', 'DIS', 'BABA']:
        df_temp = pd.read_csv("data/{}.csv".format(name),
                              index_col='Date',
                              parse_dates=True,
                              usecols=['Date', 'Adj Close'],
                              na_values=['nan'])
        # start left join
        df_temp = df_temp.rename(columns={'Adj Close': name})
        df1 = df1.join(df_temp, how="left")
    # drop nan
    df1 = df1.dropna(subset=['SPY'])
    print df1


def normalize_data(df):
    return df / df.ix[0]


def main():
    # Define a date range
    dates = pd.date_range('2017-10-13', '2017-11-13')

    # Choose stock symbols to read
    symbols = ['JD', 'DIS', 'BABA']

    # Get stock data
    df = get_data(symbols, dates)

    print df
    print df.ix['2017-10-20':'2017-10-25']
    print df['JD']
    print df[['JD', 'DIS']]
    print df.ix['2017-10']
    ax = normalize_data(df).plot(title="Stock Price")
    ax.set_xlabel("Price")
    ax.set_ylabel("Date")
    plt.show()


if __name__ == "__main__":
    main()
