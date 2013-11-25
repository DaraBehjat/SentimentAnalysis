"""Code to read RSS feed and store it in database. 
"""

import feedparser
import urllib
import string
from HTMLParser import HTMLParser
import anydbm
import pickle 
import uuid
import datetime

class MLStripper(HTMLParser):
    """ This code was found at stackoverflow to strip the HTML from the text. 
    http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
    """
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ' '.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def create_link_list(t):
	"""Function that creates a list of links from RSS feed.
	
	t: list

	returns: list of 25 most recent links given by RSS feed. 
	"""
	link_list = []
	for i in range(len(t)):
		temp_d = entries_feed[i]
	
		summary = temp_d['links']
		summary_d = summary[0]

		link = summary_d['href']
		link_list.append(link)
	
	return link_list



def open_link_cnn(url):
	"""Function that takes a link from a list, opens the url and strips 
	the HTML from the CNN article where it says to start and finish. 

	t: list of links
	i: desired index of list

	returns: string of parsed article 
	"""
	t = "" 
	article = urllib.urlopen(url)
	start = False 
	for line in article: 
		# when to start parsing 
		if "cnnCol_main" in line:
			start = True 
		if start: 
			text = strip_tags(line)
			t += text 
		# when to stop parsing and return	 
		if "OB_div" in line: 
			return t


def open_link_bbc(url):
	t = "" 
	article = urllib.urlopen(url)
	start = False 
	for line in article: 
		# when to start parsing 
		if "<h1 class" in line:
			start = True 
		if start: 
			text = strip_tags(line)
			t += text 
		# when to stop parsing and return	 
		if "Related hypers" in line: 
			return t 


def open_link_reuters(t, i):
	url = t[i]
	print url
	t = "" 
	article = urllib.urlopen(url)
	start = False 
	for line in article: 
		# when to start parsing 
		# TODO -- FIND REUTERS START POINT 
		if "------" in line:
			start = True 
		if start: 
			text = strip_tags(line)
			t += text 
		# when to stop parsing and return	 
		if "FILED UNDER" in line: 
			return t 

class Article(object):
	"""Contains information about each article including date, source and 
	original URL."""


article_d = {}

def get_info(links):
	for url in links:
		if url not in article_d.keys():
			name = str(uuid.uuid1()) + '.txt'

			# change the open_link_ function to specific news source
			example = open_link_bbc(url)

			article = open(name, 'w')
			article.write(example)
			article.close()

			date = str(datetime.date.today())

			article_d[url] = (name, date)

	return article_d



def print_article(t, i):
	url = t[i]
	print url
	article = urllib.urlopen(url)
	for line in article:
		print line 


if __name__ == '__main__':
	cnn = "feed://rss.cnn.com/rss/money_latest.rss"
	bbc = "feed://feeds.bbci.co.uk/news/business/rss.xml"
	reuters = "http://feeds.reuters.com/reuters/companyNews"
	forbes = "http://www.forbes.com/business/index.xml"

	python_rss_url = bbc

	feed = feedparser.parse( python_rss_url )
	entries_feed = feed['entries']


	links = create_link_list(entries_feed)


	get_info(links)


	print len(article_d)


	# pickle.dump(article, open("reuters/11_19_1.p", "wb"))




