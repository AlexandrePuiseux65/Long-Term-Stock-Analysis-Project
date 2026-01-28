import pandas as pd 
import yfinance as yf

'''
This fonction test that the ticker we trying to use if correct for Paris market.
It also print the name of the stock in the terminal.
'''
def is_valid_cac40_ticker(ticker):
    df = pd.read_csv('data/cac40.csv')
    if ticker in df["symbol_paris"].values:
        return True
    else: 
        return False

'''
Fetch raw financial and market data from Yahoo Finance.
No financial calculations here.
'''
class FetchDataStocks:
    def __init__(self, ticker) -> None:
        if not is_valid_cac40_ticker(ticker):
            raise ValueError(f"ERREUR: {ticker} not a valid CAC40 ticker")

        self.ticker = ticker
        self.stock = yf.Ticker(ticker)

    def get_price_history(self, start="1990-01-01"):
        """gets historical stock price data from a specific start date"""
        return self.stock.history(start=start)

    def get_current_price(self):
        """gets the latest market price of the stock"""
        return self.stock.info.get("currentPrice")

    def get_market_cap(self):
        """gets the total market capitalization of the company"""
        return self.stock.info.get("marketCap")

    def get_income_statement(self):
        """gets the full income statement (financials) dataframe"""
        return self.stock.financials

    def get_cashflow(self):
        """gets the full cash flow statement dataframe"""
        return self.stock.cashflow

    def get_balance_sheet(self):
        """gets the full balance sheet dataframe"""
        return self.stock.balance_sheet

    def get_revenue(self):
        """gets total revenue data from income statement"""
        df = self.stock.financials
        for key in ["Total Revenue", "TotalRevenue"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_net_income(self):
        """gets net income (profit) data from income statement"""
        df = self.stock.financials
        for key in ["Net Income", "NetIncome"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_ebit(self):
        """gets earnings before interest and taxes"""
        df = self.stock.financials
        for key in ["Ebit", "EBIT"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_ebitda(self):
        """gets earnings before interest, taxes, depreciation and amortization"""
        df = self.stock.financials
        for key in ["Ebitda", "EBITDA"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_operating_cashflow(self):
        """gets cash generated from core business operations"""
        df = self.stock.cashflow
        for key in ["Operating Cash Flow", "OperatingCashFlow"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_dividends(self):
        """gets raw historical dividend payment events"""
        return self.stock.dividends

    def get_annual_dividend(self):
        """calculates the sum of dividends paid per calendar year"""
        divs = self.get_dividends()
        if divs.empty:
            return None
        annual_divs = divs.groupby(divs.index.year).sum()
        return annual_divs

    def get_shares_outstanding(self):
        """gets the total number of shares currently in circulation"""
        return self.stock.info.get("sharesOutstanding")

    def get_cash(self):
        """gets cash and cash equivalents from balance sheet"""
        df = self.stock.balance_sheet
        for key in ["Cash", "Cash And Cash Equivalents"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_total_debt(self):
        """gets total debt (short and long term) from balance sheet"""
        df = self.stock.balance_sheet
        for key in ["Total Debt", "Long Term Debt"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_equity(self):
        """gets total stockholder equity from balance sheet"""
        df = self.stock.balance_sheet
        for key in ["Total Stockholder Equity"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_total_assets(self):
        """gets total assets from balance sheet"""
        df = self.stock.balance_sheet
        for key in ["Total Assets", "TotalAssets"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_capex(self):
        """gets capital expenditure (investment in assets) from cashflow"""
        df = self.stock.cashflow
        for key in ["Capital Expenditure", "CapitalExpenditure"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_interest_expense(self):
        """gets the cost of interest paid on debt from income statement"""
        df = self.stock.financials
        for key in ["Interest Expense", "InterestExpense"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_free_cash_flow(self):
        """gets cash remaining after all operating and capital expenses"""
        df = self.stock.cashflow
        for key in ["Free Cash Flow", "FreeCashFlow"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_sector_info(self):
        """gets the industrial sector classification of the company"""
        return self.stock.info.get("sector")
    
    def get_growth_estimates(self):
        """gets projected earnings growth percentage"""
        return self.stock.info.get("earningsGrowth")
        
    def get_news(self):
        """gets recent news headlines and links for the stock"""
        return self.stock.news