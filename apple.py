import yfinance as yf
import pandas as pd

# Define the ticker symbol for Apple
ticker_symbol = 'AAPL'

# Create a ticker object
ticker_data = yf.Ticker(ticker_symbol)

# Get historical prices for 2022 and 2023
apple_data_2000_2023 = ticker_data.history(period='1d', start='2000-01-01', end='2024-01-01', interval='1mo')
apple_data_2000_2022 = ticker_data.history(period='1d', start='2000-01-01', end='2023-01-01', interval='1mo')

# Drop rows with NaN values
apple_data_2000_2023.dropna(inplace=True)
apple_data_2000_2022.dropna(inplace=True)

# Save to CSV
apple_data_2000_2023.to_csv('apple_stock_prices_2000_2023.csv')
apple_data_2000_2022.to_csv('apple_stock_prices_2000_2022.csv')


import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(apple_data_2000_2023['Close'], label='2000-2023')
plt.plot(apple_data_2000_2022['Close'], label='2000-2022')
plt.title('Apple Stock Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.show()

