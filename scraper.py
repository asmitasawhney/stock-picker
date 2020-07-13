#!/usr/bin/python3

from lxml import html
import requests
import json
import argparse
from collections import OrderedDict
from bs4 import BeautifulSoup

def get_headers():

    return {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
            "cache-control": "max-age=0",
            "dnt": "1",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0"}


def parse(ticker):
    
    url = "http://finance.yahoo.com/quote/%s?p=%s" % (ticker, ticker)
    response = requests.get(url, headers={"User-agent": "Mozilla/5.0"}).text
    soup = BeautifulSoup(response, "html.parser")   
    


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



