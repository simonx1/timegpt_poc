import pandas as pd
from nixtlats import TimeGPT
import time


# Load the data
df = pd.read_csv('apple_stock_prices_2000_2022.csv')

df['Date'] = pd.to_datetime(df['Date'], utc=True)
# If you want to convert to a specific timezone, use: df['Date'] = df['Date'].dt.tz_convert('YourTimezone')
# Format the date
df['Date'] = df['Date'].dt.date

# Print the first few rows of the DataFrame
print(df.head())

# Continue with your analysis
timegpt = TimeGPT()
timegpt.validate_token()

timegpt.plot(df, time_col='Date', target_col='Close')

timegpt_fcst_df = timegpt.forecast(df=df, h=12, time_col='Date', target_col='Close', freq='MS')
timegpt_fcst_df.head()

timegpt.plot(df, timegpt_fcst_df, time_col='Date', target_col='Close')


print(timegpt_fcst_df)

time.sleep(10)
