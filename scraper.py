#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

class Scraper:

	def __init__(self, url):
		self.url = url

	def scrape(self):
		r = requests.get(self.url)
		return BeautifulSoup(r.content)

'''scraper = Scraper('http://www.nasdaq.com/symbol/yhoo/after-hours')
html = scraper.scrape()

price = html.find_all(id='qwidget_lastsale')
print(price[0].string)'''
