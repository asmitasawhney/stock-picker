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
    
    alldata = soup.find_all("tbody")

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



