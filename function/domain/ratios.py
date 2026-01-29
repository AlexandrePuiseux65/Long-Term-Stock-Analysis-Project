from function.domain.stock import Stock
from function.domain.metrics import (
    compute_bna,
    get_net_income,
    get_revenue,
    get_ebit,
    get_operating_cashflow,
    get_capex,
    get_cash_and_equiv,
    get_interest_expense,
    get_ebitda
)

def get_average_price(stock: Stock, year: int):
    """calculates the mean closing price for a specific year"""
    prices = stock.prices
    prices_year = prices[prices.index.year == year]
    if prices_year.empty:
        return None
    return prices_year["Close"].mean()

def per(stock: Stock, year: int):
    """calculates the price-to-earnings ratio using average yearly price"""
    bna = compute_bna(stock, year)
    price = get_average_price(stock, year)

    if bna is None or price is None or bna == 0:
        return None

    return price / bna

def roe(stock: Stock, year: int):
    """calculates return on equity to measure profitability relative to shareholders' equity"""
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
    """calculates return on assets to measure how efficiently assets generate profit"""
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
    """calculates net profit margin as a percentage of total revenue"""
    net_income = get_net_income(stock, year)
    revenue = get_revenue(stock, year)

    if net_income is None or revenue is None or revenue == 0:
        return None

    return net_income / revenue

def payout_ratio(stock: Stock, year: int):
    """calculates the percentage of net income paid out as dividends"""
    dividends = stock.dividends
    net_income = get_net_income(stock, year)

    dividends_year = dividends[dividends.index.year == year].sum()

    if net_income is None or net_income == 0:
        return None

    return dividends_year / net_income

def dividend_coverage(stock: Stock, year: int):
    """calculates how many times a company can pay its dividend using its profits"""
    bna = compute_bna(stock, year)
    dividends = stock.dividends
    shares = stock.shares_outstanding

    dividends_year = dividends[dividends.index.year == year].sum()
    dividend_per_share = dividends_year / shares if shares else None

    if bna is None or dividend_per_share is None or dividend_per_share == 0:
        return None

    return bna / dividend_per_share

def leverage(stock: Stock, year: int):
    """calculates the financial leverage using the debt to ebitda ratio"""
    debt_df = stock.balance_sheet

    if "Total Debt" not in debt_df.index:
        return None

    debt = debt_df.loc["Total Debt"]
    debt_year = debt[debt.index.year == year]
    ebitda = get_ebitda(stock, year)

    if debt_year.empty or ebitda is None or ebitda == 0:
        return None

    return debt_year.iloc[0] / ebitda

def price_to_book(stock: Stock, year: int):
    """calculates the market price relative to the company's book value per share"""
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
    """calculates operating margin (ebit / revenue)"""
    ebit = get_ebit(stock, year)
    revenue = get_revenue(stock, year)

    if ebit is None or revenue is None or revenue == 0:
        return None

    return ebit / revenue

def dividend_yield(stock: Stock, year: int):
    """calculates dividend yield based on average price of the year"""
    dividends = stock.dividends
    dividends_year = dividends[dividends.index.year == year].sum()
    
    price = get_average_price(stock, year)
    shares = stock.shares_outstanding

    if price is None or not shares or price == 0:
        return None
    
    dividend_per_share = dividends_year / shares
    return dividend_per_share / price

def free_cash_flow(stock: Stock, year: int):
    """calculates free cash flow (operating cash flow + capex)"""
    ocf = get_operating_cashflow(stock, year)
    capex = get_capex(stock, year)

    if ocf is None or capex is None:
        return None
    return ocf + capex

def net_debt(stock: Stock, year: int):
    """calculates net debt (total debt - cash)"""
    debt_df = stock.balance_sheet
    if "Total Debt" not in debt_df.index:
        return None
    
    debt = debt_df.loc["Total Debt"]
    debt_year = debt[debt.index.year == year]
    
    cash = get_cash_and_equiv(stock, year)

    if debt_year.empty or cash is None:
        return None

    return debt_year.iloc[0] - cash

def payout_on_fcf(stock: Stock, year: int):
    """calculates payout ratio based on free cash flow instead of net income"""
    dividends = stock.dividends
    dividends_paid = dividends[dividends.index.year == year].sum()
    fcf = free_cash_flow(stock, year)

    if fcf is None or fcf <= 0:
        return None

    return dividends_paid / fcf

def retention_ratio(stock: Stock, year: int):
    """calculates the percentage of earnings kept by the company (1 - payout)"""
    payout = payout_ratio(stock, year)
    if payout is None:
        return None
    return 1 - payout

def interest_coverage_ratio(stock: Stock, year: int):
    """calculates how easily a company can pay interest on debt (ebit / interest)"""
    ebit = get_ebit(stock, year)
    interest = get_interest_expense(stock, year)

    if ebit is None or interest is None or interest == 0:
        return None

    return ebit / abs(interest)

def dividend_growth_rate(stock: Stock, year: int):
    """calculates dividend growth compared to the previous year"""
    divs = stock.dividends
    current_div = divs[divs.index.year == year].sum()
    prev_div = divs[divs.index.year == (year - 1)].sum()

    if prev_div is None or prev_div == 0:
        return None

    return (current_div - prev_div) / prev_div

def expected_total_return(stock: Stock, year: int):
    """estimates total return (yield + growth)"""
    yield_val = dividend_yield(stock, year)
    growth = dividend_growth_rate(stock, year)

    if yield_val is None or growth is None:
        return None

    return yield_val + growth