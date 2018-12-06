import boto3
import json
import csv
import pandas as pd
import sys
import matplotlib.pyplot as plt
from webhose import webhose_func
from stock_prices import stock
from boto_news_api import get_sent

def score(df_arr,stock_df,newsAPI_df):
	comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
	search_terms = df_arr[len(df_arr)//2:]
	df_arr = df_arr[:len(df_arr)//2]
	df_arr_2 = []
	for df in df_arr:
		i = 0
		title_scores = []
		df.index = df.index.str.slice(0,10)
		df.index = pd.to_datetime(df.index)
		df = df.sort_index()
		for index, row in df.iterrows():
			title = row["Title"]
			title_json = json.loads(json.dumps(comprehend.detect_sentiment(Text=title, LanguageCode='en'), sort_keys=True, indent=4))  
			title_score = (-1) * title_json['SentimentScore']['Negative'] + 0 * title_json["SentimentScore"]["Neutral"] + 1 * title_json["SentimentScore"]["Positive"]
			title_scores.append(float(title_score))
		title_scores = pd.Series(title_scores)
		df.insert(loc=1,column="Title Scores", value = title_scores.values)
		df = df.dropna(axis=0)
		df["Title Scores"] = df["Title Scores"].resample('3T').mean()
		df.loc[:,"Title Scores"] = (df.loc[:,"Title Scores"] - df.loc[:,"Title Scores"].mean())/(df.loc[:,"Title Scores"].max() - df.loc[:,"Title Scores"].min())
		df_arr_2.append(df)
	fig = plt.figure(figsize=(70,70))
	ax1 = fig.add_subplot(4,1,1)
	
	ax_arr = []
	
	for i in range(len(search_terms)):
		ax_arr.append(fig.add_subplot(4,1,i+2))
	
	ax1.plot(newsAPI_df.index,newsAPI_df["Title Scores"],c='blue',label='sentiment')
	ax1.plot(stock_df.index,stock_df["4. close"],c='orange',label='stock price')
	ax1.set_title("NewsAPI")
	ax1.tick_params(axis='x',bottom='off',labelbottom='off')	
	ax1.legend(loc="upper left",fancybox=True)
	
	colors = ["black","teal","darkblue"]	
	
	for i in range(len(df_arr)):
		ax_arr[i].plot(df_arr_2[i].index,df_arr_2[i]["Title Scores"],label=str(search_terms[i]),color=colors[i])
	
		ax_arr[i].plot(stock_df.index,stock_df["4. close"],c='crimson',label='stock')
		if i == 0:
			ax_arr[i].set_title("Webhose")
		ax_arr[i].legend(loc="upper left",fancybox=True)
		
		if i != len(df_arr) - 1:
			ax_arr[i].xaxis.set_visible(False)
	
	plt.setp(ax_arr[-1].xaxis.get_majorticklabels(), rotation=45)
	plt.show()

def driver(csv_file_for_news_api_name):
	csv_file_for_news_api = csv_file_for_news_api_name
	score(webhose_func(),stock(),get_sent(csv_file_for_news_api))	

def main():
	csv_file_for_news_api_name = input("What is the name of your decoded csv?\n")
	driver()

if __name__ == "__main__":
	main(sys.argv[:])
