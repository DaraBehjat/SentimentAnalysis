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
	"""Function that opens url and strips the HTML from the CNN article 
	where it says to start and stop and then returns parsed block of text. 

	url: link 

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
			t += str(url)
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
			t += str(url)
			return t 


def open_link_reuters(url):
	t = "" 
	article = urllib.urlopen(url)
	start = False 
	for line in article: 
		# when to start parsing 
		if "midArticle_start" in line:
			start = True 
		if start: 
			text = strip_tags(line)
			t += text 
		# when to stop parsing and return	 
		if "FILED UNDER" in line: 
			t += str(url)
			return t 

def open_link_nytimes(t, i):
	url = t[i]
	t = "" 
	article = urllib.urlopen(url)
	start = False 
	for line in article: 
		# when to start parsing 
		if "midArticle_start" in line:
			start = True 
		if start: 
			text = strip_tags(line)
			t += text 
		# when to stop parsing and return	 
		if "FILED UNDER" in line: 
			t += str(url)
			return t 

def open_link_forbes(url):
	t = "" 
	article = urllib.urlopen(url)
	start = False 
	for line in article: 
		# when to start parsing 
		if "End User Block Article Head" in line:
			start = True 
		if start: 
			text = strip_tags(line)
			t += text 
		# when to stop parsing and return	 
		if "end div.body" in line: 
			t += str(url)
			return t 


class RSSfeed(object):
	"""Contains information about each article including date, source and 
	original URL."""



def get_info(links):
	article_d = {}

	with open('read_articles.csv', 'r') as f:
		for line in f:
			lineList = line.strip().split(',')
			article_d[lineList[0]] = [lineList[1], lineList[2], lineList[3]]

	f = open('read_articles.csv', 'a')

	for url in links:
		if url not in article_d:
			name = str(uuid.uuid1()) + '.txt'
			# change the open_link_ function to specific news source
			example = open_link_reuters(url)
			article = open(name, 'w')
			article.write(example)
			article.close()

			date = str(datetime.date.today())
			# placeholder until article classes are created
			source = 'source'

			newLine = ('%s, %s, %s, %s \n') % (url, date, name, source)
			f.write(newLine)
	f.close()


def print_article(t, i):
	url = t[i]
	print url
	article = urllib.urlopen(url)
	print type(article)
	for line in article:
		print line 

def print_url(url):
	print url
	article = urllib.urlopen(url)
	print type(article)
	for line in article:
		print line 


if __name__ == '__main__':
	cnn = "feed://rss.cnn.com/rss/money_latest.rss"
	bbc = "feed://feeds.bbci.co.uk/news/business/rss.xml"
	reuters = "http://feeds.reuters.com/reuters/companyNews"
	forbes = "http://www.forbes.com/business/index.xml"
	nytimes = "feed://rss.nytimes.com/services/xml/rss/nyt/Business.xml"

	python_rss_url = reuters

	feed = feedparser.parse( python_rss_url )
	entries_feed = feed['entries']


	links = create_link_list(entries_feed)

	# print links

	# print_article(links, 0)
	# print_article(links, 5)

	# url = links[0]
	# print open_link_forbes(url)
	# url = links[0]
	# print open_link_forbes(url)

	get_info(links)




