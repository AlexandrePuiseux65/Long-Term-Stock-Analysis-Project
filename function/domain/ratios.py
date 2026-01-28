from function.domain.stock import Stock
from function.domain.metrics import get_ebitda
from function.domain.metrics import (
    compute_bna,
    get_net_income,
    get_revenue
)
import pandas as pd


def get_average_price(stock: Stock, year: int):
    prices = stock.prices
    prices_year = prices[prices.index.year == year]
    if prices_year.empty:
        return None
    return prices_year["Close"].mean()


def per(stock: Stock, year: int):
    bna = compute_bna(stock, year)
    price = get_average_price(stock, year)

    if bna is None or price is None or bna == 0:
        return None

    return price / bna


def roe(stock: Stock, year: int):
    net_income = get_net_income(stock, year)
    equity_df = stock.balance_sheet

    if "Total Stockholder Equity" not in equity_df.index:
        return None

    equity = equity_df.loc["Total Stockholder Equity"]
    equity_year = equity[equity.index.year == year]

    if equity_year.empty or net_income is None or equity_year.iloc[0] == 0:
        return None

    return net_income / equity_year.iloc[0]


def roa(stock: Stock, year: int):
    net_income = get_net_income(stock, year)
    assets_df = stock.balance_sheet

    if "Total Assets" not in assets_df.index:
        return None

    assets = assets_df.loc["Total Assets"]
    assets_year = assets[assets.index.year == year]

    if assets_year.empty or net_income is None or assets_year.iloc[0] == 0:
        return None

    return net_income / assets_year.iloc[0]


def net_margin(stock: Stock, year: int):
    net_income = get_net_income(stock, year)
    revenue = get_revenue(stock, year)

    if net_income is None or revenue is None or revenue == 0:
        return None

    return net_income / revenue


def payout_ratio(stock: Stock, year: int):
    dividends = stock.dividends
    net_income = get_net_income(stock, year)

    dividends_year = dividends[dividends.index.year == year].sum()

    if net_income is None or net_income == 0:
        return None

    return dividends_year / net_income


def dividend_coverage(stock: Stock, year: int):
    bna = compute_bna(stock, year)
    dividends = stock.dividends
    shares = stock.shares_outstanding

    dividends_year = dividends[dividends.index.year == year].sum()
    dividend_per_share = dividends_year / shares if shares else None

    if bna is None or dividend_per_share is None or dividend_per_share == 0:
        return None

    return bna / dividend_per_share


def leverage(stock: Stock, year: int):
    debt_df = stock.balance_sheet

    if "Total Debt" not in debt_df.index:
        return None

    debt = debt_df.loc["Total Debt"]
    debt_year = debt[debt.index.year == year]

    from domain.metrics import get_ebitda
    ebitda = get_ebitda(stock, year)

    if debt_year.empty or ebitda is None or ebitda == 0:
        return None

    return debt_year.iloc[0] / ebitda


def price_to_book(stock: Stock, year: int):
    equity_df = stock.balance_sheet
    shares = stock.shares_outstanding

    if "Total Stockholder Equity" not in equity_df.index or not shares:
        return None

    equity = equity_df.loc["Total Stockholder Equity"]
    equity_year = equity[equity.index.year == year]

    prices = stock.prices
    prices_year = prices[prices.index.year == year]

    if equity_year.empty or prices_year.empty:
        return None

    book_value_per_share = equity_year.iloc[0] / shares
    price_avg = prices_year["Close"].mean()

    return price_avg / book_value_per_share

def operating_margin(stock: Stock, year: int):
    pass

def dividend_yield(stock: Stock, year: int):
    pass

def free_cash_flow(stock: Stock, year: int):
    pass

def net_debt(stock: Stock, year: int):
    pass

def payout_on_fcf(stock: Stock, year: int):
    pass

def retention_ratio(stock: Stock, year: int):
    pass

def interest_coverage_ratio(stock: Stock, year: int):
    pass

def dividend_growth_rate(stock: Stock, year: int):
    pass

def expected_total_return(stock: Stock, year: int):
    pass