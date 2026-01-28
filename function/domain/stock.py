class Stock:
    """
    Domain object holding raw financial and market data.
    """

    def __init__(
        self,
        ticker,
        prices,
        current_price,
        market_cap,
        income_statement,
        cashflow,
        balance_sheet,
        revenue,
        net_income,
        ebit,
        ebitda,
        operating_cashflow,
        dividends,
        dividents_all,
        shares_outstanding,
        cash,
        total_debt,
        equity,
        total_assets,
        capex,
        interest_expense,
        free_cash_flow,
        sector_info,
        growth_estimates,
        news
    ):
        self.ticker=ticker
        self.prices=prices
        self.current_price=current_price
        self.market_cap=market_cap
        self.income_statement=income_statement
        self.cashflow=cashflow
        self.balance_sheet=balance_sheet
        self.revenue=revenue
        self.net_income=net_income
        self.ebit=ebit
        self.ebitda=ebitda
        self.operating_cashflow=operating_cashflow
        self.dividends=dividends
        self.dividents_all=dividents_all
        self.shares_outstanding=shares_outstanding
        self.cash=cash
        self.total_debt=total_debt
        self.equity=equity
        self.total_assets=total_assets
        self.capex=capex
        self.interest_expense=interest_expense
        self.free_cash_flow=free_cash_flow
        self.sector_info=sector_info
        self.growth_estimates=growth_estimates
        self.news=news

    def __repr__(self):
        return f"Stock(ticker={self.ticker}, price={self.current_price}, cap={self.market_cap})"
