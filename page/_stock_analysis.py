import streamlit as st
from function.services.finance import load_stock
from function.services.fetch import is_valid_cac40_ticker
from function.domain.scoring import calculate_global_score

from visual.price_chart import plot_stock_history
from visual.metric_table import display_key_ratios
from visual.score import display_score_gauge
from visual.info_table import display_info_table
from visual.news_section import display_news

import pandas as pd

def show_analysis_page():
    st.title("Stock Analysis")

    ticker = st.text_input("Enter the stock ticker :").upper()

    if ticker:
        if is_valid_cac40_ticker(ticker):
            with st.spinner(f"Analyzing {ticker}..."):
                try:
                    data = load_stock(ticker)
                    print(f"DEBUG: Checking data for {data.current_price}")
                    if data is not None:
                        try:
                            fig = plot_stock_history(data)
                            st.plotly_chart(fig, use_container_width=True)
                        except Exception as e:
                            st.error(f"Chart Error: {e}")

                        try:
                            display_key_ratios(data)
                        except Exception as e:
                            st.error(f"Ratios Table Error: {e}")
                            
                except Exception as e:
                    st.error(f"An error occurred while loading data: {e}")