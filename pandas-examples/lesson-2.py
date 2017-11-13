import pandas as pd
import matplotlib.pyplot as plt


def test_run1():
    df = pd.read_csv("data/JD.csv")
    print df.tail()


def get_max_close(name):
    df = pd.read_csv("data/{}.csv".format(name))
    return df['Close'].max()


def plot_adj_close(name):
    df = pd.read_csv("data/{}.csv".format(name))
    print df['Adj Close']
    df['Adj Close'].plot()
    plt.show()


def plot_columns(name):
    df = pd.read_csv("data/{}.csv".format(name))
    df[['Open', 'High', 'Low']].plot()
    plt.show()


def main():
    plot_columns("DIS")


if __name__ == "__main__":
    main()
