
import os 
import string 
import csv 
import json
import pprint 

from analyzer1 import *


def freq_word_index(t):
    """Creates word frequency histogram of each article and stores it to 
    a csv file. 

    t: list of article filenames
    returns: dictionary of filenames mapping to a tuple (word, freq)
    """
    nestedDict = {}

    for article in t:
        if article not in nestedDict:
            hist = process_file(article)
            nestedDict[article] = hist

    return nestedDict


def company_index(stocks, nestedDict):
    """Creates a dictionary of company name mapping to filenames 
    containing the company.

    t: list of company names 
    d: list of dictionaries with each mapping from word to frequency
    returns: 
    """

    companies = {}
    for c in stocks:
        for f in nestedDict:
            if c in nestedDict[f]:
                # need to find it when word count of it is greater than 1
                if nestedDict[f][c] > 1:
                    try:
                        companies[c].append(f)
                    except KeyError:
                        companies[c] = [f]
    return companies


def process_file(filename):
    """Makes a histogram that contains the words from a file.

    filename: string   
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    pathName = 'news/' + filename 
    fp = file(pathName)

    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: histogram (map from word to frequency)
    """
    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    
    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        # update the histogram
        hist[word] = hist.get(word, 0) + 1


def read_sentiment(filename):
    """Evaluates the sentiment of one article
    filename: text file name
    returns: string 
    """
    pathName = 'news/' + filename
    with open(pathName, 'r') as f:
        s = ''
        for line in f:
            s += line 
        return classifier.classify(extract_features(s.split())) 


def store_sentiment(t):
    """Creates dictionary mapping from filname to tuple of (date, sentiment)
    filename_date: dictionary mapping from filename to date
    returns: sentiments dictionary mapping from filname to (date, sentiment) 
    """
    filename_date = {}
    with open('read_articles.csv', 'r') as f:
        for line in f:
            lineList = line.strip().split(', ')
            filename_date[lineList[2]] = lineList[1]

    sentiments = {}
    for element in t:
        sent = read_sentiment(element)
        try:
            sentiments[element] = (filename_date[element], sent)
        except:
            sentiments[element] = ("Date Not Availible", sent)
    return sentiments



if __name__ == '__main__':
    t = os.listdir('news/')
    shortList = t[1:]

    companyList = ['rite', 'ford', 'facebook', 'comcast', 'google', 'microsoft', 'hilton', 'qualcomm', 'bac', 'merrill', 'ge']

    nestedDict = freq_word_index(shortList)

    # print nestedDict
    d = company_index(companyList, nestedDict)
    # print len(d['microsoft'])


    # # store the articles about microsoft to a list
    company = (d['facebook'])
    # print company

    # store_sentiment(company)



