import os
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch historical stock data using yfinance.
    """
    print(f"Fetching data for {ticker} from {start_date} to {end_date}...")
    df = yf.download(ticker, start=start_date, end=end_date)
    return df

def ensure_data_folder(folder_path):
    """
    Ensure the data folder exists. If it's empty, add a .gitkeep placeholder.
    """
    os.makedirs(folder_path, exist_ok=True)
    if not os.listdir(folder_path):
        gitkeep_path = os.path.join(folder_path, ".gitkeep")
        with open(gitkeep_path, "w") as f:
            f.write("")
        print(f"Created .gitkeep in {folder_path}")
    else:
        print(f"Data folder '{folder_path}' is not empty; skipping .gitkeep creation.")

def save_data(df, folder, ticker):
    """
    Save DataFrame as CSV in the given folder.
    """
    file_path = os.path.join(folder, f"{ticker}.csv")
    df.to_csv(file_path)
    print(f"Data saved to {file_path}")

def plot_stock_data(df, ticker):
    """
    Plot the stock's closing price.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["Close"], label=f"{ticker} Close Price", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.title(f"{ticker} Stock Price History")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    ticker = "AAPL"
    start_date = "2015-01-01"
    end_date = "2025-02-08"

    # Determine the project root and data folder
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    data_folder = os.path.join(project_root, "data")

    # Ensure the data folder exists (and add .gitkeep if empty)
    ensure_data_folder(data_folder)

    # Fetch stock data
    df = fetch_stock_data(ticker, start_date, end_date)
    print("Data preview:")
    print(df.head())

    # Save the data to the data folder
    save_data(df, data_folder, ticker)

    # Plot the stock data
    plot_stock_data(df, ticker)
