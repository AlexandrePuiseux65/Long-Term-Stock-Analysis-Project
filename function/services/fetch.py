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

    '''
    > Get Market data
    '''
    def get_price_history(self, start="1990-01-01"):
        return self.stock.history(start=start)

    def get_current_price(self):
        return self.stock.info.get("currentPrice")

    def get_market_cap(self):
        return self.stock.info.get("marketCap")

    '''
    > Get fundamental data
    '''
    def get_income_statement(self):
        return self.stock.financials

    def get_cashflow(self):
        return self.stock.cashflow

    def get_balance_sheet(self):
        return self.stock.balance_sheet
    
    '''
    > Get market metrics
    '''
    def get_revenue(self):
        df = self.stock.financials
        for key in ["Total Revenue", "TotalRevenue"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_net_income(self):
        df = self.stock.financials
        for key in ["Net Income", "NetIncome"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_ebit(self):
        df = self.stock.financials
        for key in ["Ebit", "EBIT"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_ebitda(self):
        df = self.stock.financials
        for key in ["Ebitda", "EBITDA"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_operating_cashflow(self):
        df = self.stock.cashflow
        for key in ["Operating Cash Flow", "OperatingCashFlow"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_dividends(self):
        return self.stock.dividends

    def get_annual_dividend(self):
        divs = self.get_dividends()
        if divs.empty:
            return None
        annual_divs = divs.groupby(divs.index.year).sum()
        return annual_divs

    def get_shares_outstanding(self):
        return self.stock.info.get("sharesOutstanding")

    def get_cash(self):
        df = self.stock.balance_sheet
        for key in ["Cash", "Cash And Cash Equivalents"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_total_debt(self):
        df = self.stock.balance_sheet
        for key in ["Total Debt", "Long Term Debt"]:
            if key in df.index:
                return df.loc[key]
        return None

    def get_equity(self):
        df = self.stock.balance_sheet
        for key in ["Total Stockholder Equity"]:
            if key in df.index:
                return df.loc[key]
        return None

    '''
    > Get Stock news
    '''
    # to test
    def get_news(self):
        return self.stock.news
