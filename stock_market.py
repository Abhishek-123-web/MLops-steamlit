import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Stock Market App")

#stock market app
#stock

st.write("This What my hope of getting Hike!!")

ticker_symbol = st.text_input("Enter the Stock ticker Symbol", "AAPL")

ticker_data = yf.Ticker(ticker_symbol)

starting_date = st.date_input("Enter the starting date", value=pd.to_datetime("2021-01-01"))

hist = ticker_data.history(start ="2022-05-31", end = "2022-07-31")

st.write("I am going to show you the data of Apple Stock")

st.write(hist)


col1, col2 = st.columns(2)

with col1:
    st.title("This plot is Volume of AAPL")

    st.line_chart(hist.Volume)

with col2:
    st.title("This is plot of Price")

    st.line_chart(hist.Close)

    