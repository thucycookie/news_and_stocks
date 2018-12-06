import boto3
import json
import csv
import pandas as pd
import sys
import matplotlib.pyplot as plt

def get_sent(csv_file_):
	csv_file = csv_file_
	comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
	original_csv = csv_file
	i = 0
	df = pd.read_csv(original_csv,sep='@\s*',skipinitialspace=True,quoting=csv.QUOTE_ALL,engine='python')
	df = df.iloc[:,[0,3,5]]
	df.columns = ['Date','Description','Title']
	df.Date = df.Date.str.slice(1,11)
	df = df.sort_values(by='Date')
	df_sent_score = pd.DataFrame(index=df['Date'],columns=['Title Scores','Description Scores'], dtype=float)
	df_sent_score.index = pd.to_datetime(df_sent_score.index)
	for index, row in df.iterrows():
		title = row["Title"]
		description = row["Description"]

		title_json = json.loads(json.dumps(comprehend.detect_sentiment(Text=title, LanguageCode='en'), sort_keys=True, indent=4))  
		description_json = json.loads(json.dumps(comprehend.detect_sentiment(Text=description, LanguageCode='en'), sort_keys=True, indent=4))

		title_score = (-1) * title_json['SentimentScore']['Negative'] + 0 * title_json["SentimentScore"]["Neutral"] + 1 * title_json["SentimentScore"]["Positive"]
		description_score = (-1) * description_json['SentimentScore']['Negative'] + 0 * description_json["SentimentScore"]["Neutral"] + 1 * description_json["SentimentScore"]["Positive"]
		df_sent_score.iloc[index] = [float(title_score),float(description_score)]
	df_sent_score = df_sent_score.dropna()

	#normalize the sentiment scores
	df_sent_score = (df_sent_score - df_sent_score.mean())/(df_sent_score.max() - df_sent_score.min())
	# df_sent_score.plot(y=["Title Scores","Description Scores"],figsize=(20,20))
	# print(df_sent_score)
	# plt.show()
	return df_sent_score

def main(argv):
	csv_file = input("Type in the name of your decoded csv file.")
	get_sent(csv_file)

if __name__ == "__main__":
	main(sys.argv[:])
