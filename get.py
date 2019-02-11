#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase
from csv import writer  

class scrapper:
    def __init__(self, baseurl):
        self.baseurl = baseurl

class crawler:
	def __init__(self,baseurl,page):
		self.baseurl=baseurl
		self.page=page

class parent(scrapper,crawler):
    pass

    def scrap(self):
    	options=[];
    	response=requests.get(self.baseurl);
    	soup=BeautifulSoup(response.text,'html.parser')
    	options=soup.find_all(class_="_3ybBIU")
    	print(options)


p=parent('https://www.flipkart.com');
p.scrap()