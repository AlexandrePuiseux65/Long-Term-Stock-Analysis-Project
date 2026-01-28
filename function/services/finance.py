from function.services.fetch import FetchDataStocks
from function.domain.stock import Stock

# factory fonction
def load_stock(ticker: str):
    try : 
        fetch = FetchDataStocks(ticker)

        return Stock(
            ticker=ticker,
            prices=fetch.get_price_history(),
            current_price=fetch.get_current_price(),
            market_cap=fetch.get_market_cap(),
            income_statement=fetch.get_income_statement(),
            cashflow=fetch.get_cashflow(),
            balance_sheet=fetch.get_balance_sheet(),
            revenue=fetch.get_revenue(),
            net_income = fetch.get_net_income(),
            ebit=fetch.get_ebit(),
            ebitda=fetch.get_ebitda(),
            operating_cashflow=fetch.get_operating_cashflow(),
            dividends=fetch.get_dividends(),
            dividents_all= fetch.get_annual_dividend(),
            shares_outstanding=fetch.get_shares_outstanding(),
            cash=fetch.get_cash(),
            total_debt=fetch.get_total_debt(),
            equity=fetch.get_equity(),
            total_assets=fetch.get_total_assets(),
            capex=fetch.get_capex(),
            interest_expense=fetch.get_interest_expense(),
            free_cash_flow=fetch.get_free_cash_flow(),
            sector_info=fetch.get_sector_info(),
            growth_estimates=fetch.get_growth_estimates(),
            news=fetch.get_news()
        )
    except Exception as e: 
        print(f"Error for {ticker}: {e}")
        return None

