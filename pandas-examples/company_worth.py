"""Company Worth"""

import math


def intrinsic_value(dividend_per_year, discount_per_year):
    return (float)(dividend_per_year / discount_per_year)


def book_value(total_asset, intangible_asset, liabilities):
    # intangible_asset: patents, branding
    # liabilities: loan
    return (total_asset - intangible_asset - liabilities)


def market_capitalization(total_shares, stock_price):
    return total_shares * stock_price
