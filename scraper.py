#!/usr/bin/python3

from lxml import html
import requests
import json
import argparse
from collections import OrderedDict
from bs4 import BeautifulSoup

def parse(ticker):
    
    url = "http://finance.yahoo.com/quote/%s?p=%s" % (ticker, ticker)
    response = requests.get(url, headers={"User-agent": "Mozilla/5.0"}).text
    soup = BeautifulSoup(response, "html.parser")   
    data_dict = {}

    try:
        #the structure of html can be revealed by inspecting the website
        #The data we are interested in is divided into 2 tbody --> 8 tr each --> 2 td each
        tbody = soup.find_all("tbody")

        tr_col1 = tbody[0].find_all("tr")
        tr_col2 = tbody[1].find_all("tr")
        
        for i in range(len(tr_col1)):
           td_col1 = tr_col1[i].find_all("td")
           data_dict[td_col1[0].text] = td_col1[1].text

        for i in range(len(tr_col2)):
            td_col2 = tr_col2[i].find_all("td")
            data_dict[td_col2[0].text] = td_col2[1].text

    except:
        print("Error with website layout for this ticker")
        tr_col1 = tr_col2 = None
    
    
    print(data_dict.get("EPS (TTM)"))


if __name__ == "__main__":
    
    #using argeparse to get the stock ticker from user
    argparser = argparse.ArgumentParser(description='Evaulate a stock ticker')
    argparser.add_argument('ticker', type=str, help='stock ticker to be evaluated')
    args = argparser.parse_args()

    #stock ticker
    ticker = args.ticker 

    # ---- add functionality to get stock ticker from company name


    print('Ticker: ', ticker)

    parse(ticker)



