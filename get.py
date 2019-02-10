#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase
from csv import writer  

class scrapper:
    def __init__(self, baseurl):
        self.baseurl = baseurl

# s=scrapper('https://www.flipkart.com')

class crawler:
	def __init__(self,baseurl,page):
		self.baseurl=baseurl
		self.page=page

class parent(scrapper,crawler):
    pass

    def scrap(self):
    	print(self.baseurl)


p=parent('https://www.flipkart.com');
p.scrap()