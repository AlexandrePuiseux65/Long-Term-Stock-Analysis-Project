from function.domain.stock import Stock
import pandas as pd


def _get_value_by_year(series: pd.Series, year: int):
    values = series[series.index.year == year]
    if values.empty:
        return None
    return values.iloc[0]

def get_revenue(stock: Stock, year: int):
    df = stock.income_statement
    if "Total Revenue" not in df.index:
        return None
    return _get_value_by_year(df.loc["Total Revenue"], year)

def get_net_income(stock: Stock, year: int):
    df = stock.income_statement
    if "Net Income" not in df.index:
        return None
    return _get_value_by_year(df.loc["Net Income"], year)

def compute_bna(stock: Stock, year: int):
    net_income = get_net_income(stock, year)
    shares = stock.shares_outstanding
    if net_income is None or not shares:
        return None
    return net_income / shares

def get_operating_cashflow(stock: Stock, year: int):
    df = stock.cashflow
    if "Operating Cash Flow" not in df.index:
        return None
    return _get_value_by_year(df.loc["Operating Cash Flow"], year)

def compute_cf_per_share(stock: Stock, year: int):
    cashflow = get_operating_cashflow(stock, year)
    shares = stock.shares_outstanding
    if cashflow is None or not shares:
        return None
    return cashflow / shares

def get_ebitda(stock: Stock, year: int):
    df = stock.income_statement
    for key in ["EBITDA", "Normalized EBITDA"]:
        if key in df.index:
            return _get_value_by_year(df.loc[key], year)
    return None

def get_ebit(stock: Stock, year: int):
    pass

def get_capex(stock: Stock, year: int):
    pass

def get_cash_and_equiv(stock: Stock, year: int):
    pass

def get_interest_expense(stock: Stock, year: int):
    pass