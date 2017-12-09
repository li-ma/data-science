import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


def test1():
    print np.array([(3, 2, 4), (5, 6, 7)])
    print np.empty(5)
    print np.empty((5, 4))
    print np.ones((5, 4), dtype=np.int)
    print np.zeros((5, 4), dtype=np.int_)
    print np.random.rand(5, 4)
    print np.random.normal(50, 10, size=(5, 4))
    print np.random.randint(10, 100, size=(1, 2))


def test2():
    a = np.ones((3, 4), dtype=np.int_)
    print a.shape
    print len(a.shape)
    print a.shape[0]  # rows
    print a.shape[1]  # columns
    print a.size
    print a.dtype


def test3():
    np.random.seed(1234567890)
    a = np.random.randint(0, 10, size=(5, 4))
    print 'Array:\n', a
    print 'Sum: ', a.sum()
    print 'Sum of each column: ', a.sum(axis=0)
    print 'Sum of each row: ', a.sum(axis=1)
    print 'Minimum of each column: ', a.min(axis=0)
    print 'Maximum of each row: ', a.max(axis=1)
    print 'Mean of all: ', a.mean()


def get_max_index(a):
    """Return the index of the maximum value in given 1D array."""
    return a.argmax()


def test4():
    a = np.random.randint(0, 10, size=(5, 5))
    print "Array:", a

    print a[3, 3]
    print a[3, 3:5]
    print a[:, 0:3:2]

    print a[3, 3]
    a[3, 3] = 999
    print a[3, 3]
    print a

    a[3, :] = 888
    print a

    a[4, :] = [-1, -2, -3, -4, -5]
    print a


def test5():
    a = np.random.random(5)
    print a

    indices = np.array([1, 1, 2, 3])
    print a[indices]

    b = np.random.random((3, 3))
    print 'mean: ', b.mean()
    print b[b < b.mean()]


def main():
    a = np.array([(1, 2, 3, 4, 5), (10, 20, 30, 40, 50)])
    print a * a
    print a / 2
    print a / a


if __name__ == "__main__":
    main()
