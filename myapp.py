import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""

# Simple Stock Price App

#### Shown are the stock closing price and volume for Apple Inc.

""")

# define the ticker symbol
ticker_symbol = "AAPL"

# get data on this ticker
ticker_data = yf.Ticker(ticker_symbol)

# get historical prices for this ticker
ticker_df = ticker_data.history(
    period='1d', start='2010-5-31', end='2022-10-13')

st.write("### Apple Closing Price")
st.line_chart(ticker_df.Close)
st.write("--------")
st.write("### Apple Volume")
st.line_chart(ticker_df.Volume)
