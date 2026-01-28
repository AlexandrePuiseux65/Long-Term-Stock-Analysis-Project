from function.domain.stock import Stock
import pandas as pd

def _get_value_by_year(series: pd.Series, year: int):
    """gets the first available value for a specific calendar year"""
    values = series[series.index.year == year]
    if values.empty:
        return None
    return values.iloc[0]

def get_revenue(stock: Stock, year: int):
    """gets total revenue from the income statement"""
    df = stock.income_statement
    if "Total Revenue" not in df.index:
        return None
    return _get_value_by_year(df.loc["Total Revenue"], year)

def get_net_income(stock: Stock, year: int):
    """gets net income from the income statement"""
    df = stock.income_statement
    if "Net Income" not in df.index:
        return None
    return _get_value_by_year(df.loc["Net Income"], year)

def compute_bna(stock: Stock, year: int):
    """calculates earnings per share (bna) for a given year"""
    net_income = get_net_income(stock, year)
    shares = stock.shares_outstanding
    if net_income is None or not shares:
        return None
    return net_income / shares

def get_operating_cashflow(stock: Stock, year: int):
    """gets operating cash flow from the cashflow statement"""
    df = stock.cashflow
    if "Operating Cash Flow" not in df.index:
        return None
    return _get_value_by_year(df.loc["Operating Cash Flow"], year)

def compute_cf_per_share(stock: Stock, year: int):
    """calculates operating cash flow per share"""
    cashflow = get_operating_cashflow(stock, year)
    shares = stock.shares_outstanding
    if cashflow is None or not shares:
        return None
    return cashflow / shares

def get_ebitda(stock: Stock, year: int):
    """gets ebitda from the income statement using multiple key checks"""
    df = stock.income_statement
    for key in ["EBITDA", "Normalized EBITDA"]:
        if key in df.index:
            return _get_value_by_year(df.loc[key], year)
    return None

def get_ebit(stock: Stock, year: int):
    """gets earnings before interest and taxes (operating income)"""
    df = stock.income_statement
    for key in ["EBIT", "Operating Income"]:
        if key in df.index:
            return _get_value_by_year(df.loc[key], year)
    return None

def get_capex(stock: Stock, year: int):
    """gets capital expenditure from the cashflow statement"""
    df = stock.cashflow
    for key in ["Capital Expenditure", "CapitalExpenditure"]:
        if key in df.index:
            return _get_value_by_year(df.loc[key], year)
    return None

def get_cash_and_equiv(stock: Stock, year: int):
    """gets cash and cash equivalents from the balance sheet"""
    df = stock.balance_sheet
    for key in ["Cash And Cash Equivalents", "Cash Cash Equivalents And Short Term Investments"]:
        if key in df.index:
            return _get_value_by_year(df.loc[key], year)
    return None

def get_interest_expense(stock: Stock, year: int):
    """gets interest expense from the income statement"""
    df = stock.income_statement
    for key in ["Interest Expense", "Interest Expense Non Operating"]:
        if key in df.index:
            return _get_value_by_year(df.loc[key], year)
    return None