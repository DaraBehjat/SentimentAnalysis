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


class RSSfeed(object):
    """Represents an RSS feed that will generate and store output files of 
    news articles."""

    def __init__(self, url=''):
        self.url = url


    def create_link_list(self):
        """Function that creates a list of links from RSS feed.
        
        returns: list of 25 most recent links given by RSS feed. 
        """
        feed = feedparser.parse(self.url)
        entries_feed = feed['entries']
        
        linkList = []
        for i in range(len(entries_feed)):
            temp_d = entries_feed[i]
        
            summary = temp_d['links']
            summary_d = summary[0]

            link = summary_d['href']
            linkList.append(link)
        
        return linkList

    def get_info(self, links):
        """Function that takes a list of links, will store the text from each link's 
        article into a separte .txt file with randomnly generated name. Will also 
        update the .csv file with information about each stored article. 

        self: specific news object
        links: list of links from specific news source 

        returns: none
        """
        article_d = {}

        with open('read_articles.csv', 'r') as f:
            for line in f:
                lineList = line.strip().split(',')
                article_d[lineList[0]] = [lineList[1], lineList[2], lineList[3]]

        f = open('read_articles.csv', 'a')

        for url in links:
            if url not in article_d:
                name = 'news/' + str(uuid.uuid1()) + '.txt'

                example = self.open_link(url)
                article = open(name, 'w')
                article.write(example)
                article.close()

                date = str(datetime.date.today())
                source = self.source 

                newLine = ('%s, %s, %s, %s \n') % (url, date, name, source)
                f.write(newLine)
        f.close()


class CNNfeed(RSSfeed):
    """Represents a CNN RSS feed."""

    def __init__(self, url='feed://rss.cnn.com/rss/money_latest.rss', source='cnn'):
        self.url = url
        self.source = source 

    def open_link(self, url):
        """Function that opens a CNN url and strips the HTML from text.

        url: link
        returns: parsed string of text 
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

class BBCfeed(RSSfeed):
    """Represents a BBC RSS feed."""

    def __init__(self, url='feed://feeds.bbci.co.uk/news/business/rss.xml', source='bbc'):
        self.url = url
        self.source = source

    def open_link(self, url):
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

class Reutersfeed(RSSfeed):
    """Represents a Reuters RSS feed."""

    def __init__(self, url='http://feeds.reuters.com/reuters/companyNews', source='reuters'):
        self.url = url
        self.source = source

    def open_link(self, url):
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

class Forbesfeed(RSSfeed):
    """Represents a Forbes RSS feed."""

    def __init__(self, url='http://www.forbes.com/business/index.xml', source='forbes'):
        self.url = url
        self.source = source 


    def open_link(self, url):
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



def main(self):
    links = self.create_link_list()
    self.get_info(links)


if __name__ == '__main__':

    cnnfeed = CNNfeed()
    bbcfeed = BBCfeed()
    reutersfeed = Reutersfeed()
    forbesfeed = Forbesfeed()

    main(forbesfeed)




