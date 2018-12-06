from alpha_vantage.timeseries import TimeSeries
import matplotlib
import matplotlib.pyplot as plt
import sys
import pandas as pd

def stock():
	print("\n")
	print("DAILY STOCK PRICE SEARCH!")
	start = input("Type in the start date in the format YYYY-MM-DD\n")
	end = input("Type in the end date in the format YYYY-MM-DD\n")
	symbol_in = input("Type in the stock symbol\n")
	ts = TimeSeries(key="Z8Y7RIN4WD8E0R01", output_format='pandas')
	data, meta_data = ts.get_daily(symbol=symbol_in,outputsize='full')
	norm_df = data.loc[start:end,'4. close']
	norm_df = pd.Series.to_frame(norm_df)
	norm_df = (norm_df - norm_df.mean())/(norm_df.max()-norm_df.min())
	norm_df.index = pd.to_datetime(norm_df.index)
	print(norm_df.info())
	return norm_df

def main():
	print(stock())

if __name__ == "__main__":
	main()
