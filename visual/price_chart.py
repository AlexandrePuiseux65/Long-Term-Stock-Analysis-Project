import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def plot_stock_history(stock):
    df_prices = stock.prices
    div_history = stock.dividends.groupby(stock.dividends.index.year).sum()
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(x=df_prices.index, y=df_prices['Close'], name="Stock Price", line=dict(color="#1f77b4")),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            x=pd.to_datetime(div_history.index, format='%Y'), 
            y=div_history.values, 
            name="AD", 
            line=dict(color="#2ca02c", width=3),
            mode='lines+markers'
        ),
        secondary_y=True,
    )

    fig.update_layout(
        title=f"Price vs Dividend History: {stock.ticker}",
        template="plotly_dark",
        xaxis_title="Year",
        hovermode="x unified"
    )

    fig.update_yaxes(title_text="Price (€)", secondary_y=False)
    fig.update_yaxes(title_text="Dividend Amount (€)", secondary_y=True)
    return fig