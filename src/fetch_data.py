import os
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch data function
def fetch_stock_data(ticker, start_date, end_date):
    return yf.download(ticker, start=start_date, end=end_date)

# Save data as CSV in ../data/
def save_data(df, ticker):
    os.makedirs("../data", exist_ok=True)
    file_path = f"../data/{ticker}.csv"
    df.to_csv(file_path)
    print(f"Data saved to {file_path}")

# Simple placeholder search function
def search(keyword, df):
    matches = [col for col in df.columns if keyword.lower() in col.lower()]
    print(f"Search '{keyword}': {matches}")
    return matches

# Simple placeholder reason function
def reason(text):
    result = f"Reasoned: {text}"
    print(result)
    return result

# Plot data function
def plot_stock_data(df, ticker):
    plt.figure(figsize=(10,5))
    plt.plot(df.index, df["Close"], label=f"{ticker} Close")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title(f"{ticker} Stock Price History")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    ticker = "AAPL"
    start_date = "2015-01-01"
    end_date = "2025-02-08"
    
    # Fetch, print and save data
    df = fetch_stock_data(ticker, start_date, end_date)
    print(df.head())
    save_data(df, ticker)
    
    # Test placeholder functions
    search("Close", df)
    reason("Testing reason function")
    
    # Plot the closing price
    plot_stock_data(df, ticker)
