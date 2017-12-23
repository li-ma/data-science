"""Company Worth"""

import math


def intrinsic_value(dividend_per_year, discount_per_year):
    return (float)(dividend_per_year / discount_per_year)


def book_value(total_asset, intangible_asset, liabilities):
    # intangible_asset: patents, branding
    # liabilities: loan
    return (total_asset - intangible_asset - liabilities)


def market_capitalization(avail_shares, stock_price):
    # avail_shares: available shares in the market
    return avail_shares * stock_price
