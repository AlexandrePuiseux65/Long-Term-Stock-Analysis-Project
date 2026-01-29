import streamlit as st
from function.domain.ratios import (
    get_average_price, per, roe, roa, net_margin, payout_ratio,
    dividend_coverage, leverage, price_to_book, operating_margin,
    dividend_yield, free_cash_flow, net_debt, payout_on_fcf,
    retention_ratio, interest_coverage_ratio, dividend_growth_rate,
    expected_total_return
)
from datetime import datetime
import pandas as pd

def display_key_ratios(stock):
    """Allow us to display the key ratios"""
    last_year = datetime.now().year - 1
    years = [last_year - i for i in range(5)]
    data = {}
    
    for y in years:
            data[str(y)] = [
                get_average_price(stock, y),
                per(stock, y),
                roe(stock, y),
                roa(stock, y),
                net_margin(stock, y),
                payout_ratio(stock, y),
                dividend_coverage(stock, y),
                leverage(stock, y),
                price_to_book(stock, y),
                operating_margin(stock, y),
                dividend_yield(stock, y),
                free_cash_flow(stock, y),
                net_debt(stock, y),
                payout_on_fcf(stock, y),
                retention_ratio(stock, y),
                interest_coverage_ratio(stock, y),
                dividend_growth_rate(stock, y),
                expected_total_return(stock, y)
        ]
    #dummy data - futur upgrade
    data["Industry AVG"] = ["-", 15, "15%", "5%", "10%", "60%", 2, 2.5, 2, "15%", "4%", "-", "-", "70%", "40%", 3, "5%", "9%"]
    data["Priority"] = [3, 3, 4, 2, 4, 5, 3, 5, 1, 2, 3, 4, 4, 5, 2, 5, 5, 3]

    df_ratio = pd.DataFrame(data, index=[
        "Average Price", "PER", "ROE", "ROA", "Net Margin", "Payout (%)",
        "Dividend Coverage", "Leverage", "Price to Book", "Operating Margin",
        "Dividend Yield", "Free Cash Flow", "Net Debt", "Payout on FCF",
        "Retention (%)", "Interest Coverage", "Dividend Growth Rate", "Expected Total Return"
    ])

    # Dummy data
    df_ratio["Status"] = "✅"
    print(df_ratio)
    return df_ratio