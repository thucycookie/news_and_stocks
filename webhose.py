import webhoseio
import sys
import pandas as pd

def webhose_func():
	YOUR_API_KEY = "a161f6e5-ab51-40a1-afaf-ba13e67baefa"
	webhoseio.config(token=YOUR_API_KEY)
	print("\n")
	print("WELCOME TO WEBHOSE\n")
	search = input("Input the string that you want to search for! It can be somethinglike ipod OR ipad\nType in a list of strings like cow,chicken,pig to plot sentiment for those words against the stock price.\n3 TERMS ARE ENOUGH!\n")
	search_terms = search.split(",")
	search_df_arr = []
	for search in search_terms:
		search += " language:english"
		sort = input("\nType crawled, relevancy, rating or publishes for your sorting option\n")
		timestamp = 1541348859918
		size = input("\nWhat is the number of post returned per request? 1 is the smallest and 100 is the biggest!\n")
		query_params = {
		"accuracy_confidence": "high",
		"q": search,
		"sort": sort,
		"ts": timestamp,
		"size": size, 	
		}
		output = webhoseio.query("filterWebContent", query_params)
		number_of_posts = len(output['posts'])
		dates = []
    
		for a in range(number_of_posts):
			dates.append(output['posts'][a]['published'])

		df = pd.DataFrame(index=dates,columns=["Title"])
		for i in range(number_of_posts):
			df.iloc[i] = [output['posts'][i]['title']]
		search_df_arr.append(df)
	
	search_df_arr = search_df_arr + search_terms
	return search_df_arr

def main(argv):
	print(webhose_func())

if __name__ == "__main__":
	main(sys.argv[:])
