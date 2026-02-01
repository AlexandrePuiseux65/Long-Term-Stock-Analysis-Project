import streamlit as st
from function.services.finance import load_stock
from function.services.fetch import is_valid_ticker
from visual.news_section import display_news
from visual.info_table import display_info_table

def show_info_page():
    st.title("Stock Information")

    ticker = st.text_input("Enter the stock ticker :").upper()

    if ticker:
        if is_valid_ticker(ticker):
            with st.spinner(f"Analyzing {ticker}..."):
                try:
                    data = load_stock(ticker)
                    print(f"DEBUG: Checking data for {data.current_price}")
                    if data is not None:
                        display_info_table(data)    
                except Exception as e:
                    st.error(f"An error occurred while loading data: {e}")
                try:
                    display_news(data.news)
                except Exception as e:
                    st.error(f"News Error: {e}") 
                