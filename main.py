import sys
import subprocess
import os.path
from subprocess import STDOUT,PIPE
from boto_webhose import driver

def main(argv):
	print("WELCOME TO NEWSAPI\n")
	print("If you have any question refers to Newsapi documentation.\n")
	top_hd_or_everything = input("Type Top Headlines or Everything.\n") #0
	country_code = ""
	sources = ""
	category = ""
	keyword_hdl = ""
	start = ""
	end = ""
	domains = ""
	keyword_every = ""
	json_file = ""
	if top_hd_or_everything == "Top Headlines":	
		country_code = input("Enter a 2-leter ISO 3166-1 code for the coutry that you want to get headlines for. Type None if you do not want to.\n") #1
		sources = input("Enter sources in coma-separated style.Refer to the API doc for proper way to input the sources. Type None to skip\n") #2
		category = input("Type in: business, entertainment,general, health, science, sports or technology for the category. Type None to skip\n") #3
		keyword_hdl = input("Type in a keyword to search for. Surround phrases with quotes for exact match.Type None to skip\n")#4
	elif top_hd_or_everything:
		start = input("Enter date to start looking for news in the form of YYYY-MM-DD. Type None to skip.\n")#5
		end = input("Enter the date to stop looking for news in the form of YYYY-MM-DD. Type None to skip.\n")#6
		domains = input("Type in the domains. Refer to API doc for more info. Type None to skip.\n") #7
		keyword_every = input("Type in a keyword to search for. Surround phrases with quotes for exact match. Type None to skip\n") #9
	else:
		print("Wrong input")
	json_file = input("Type in the name with .json file that you want to write to.\n") #10

	proc = subprocess.check_output(["java","driver_prog",top_hd_or_everything,country_code,sources,category,keyword_hdl,start,end,domains,keyword_every,json_file],stdin=subprocess.PIPE)
	csv_file = json_file[:-5] + ".csv"	
	print("File name is ", csv_file)
	driver(csv_file)
	print("Done!")

if __name__ == "__main__":
	main(sys.argv[:])
