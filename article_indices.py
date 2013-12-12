
import os 
import string 
import csv 
import json



def freq_word_index(t):
    """Creates word frequency histogram of each article and stores it to 
    a csv file. 

    t: list of article filenames
    returns: dictionary of filenames mapping to a tuple (word, freq)
    """

    article_words = {}

    # TODO: how to open the json file as a dictionary so that it can be modified
    # with open('freq_word_index.json', 'w') as f:
    #     x = json.loads(f)
    #     print x 

    f = open('freq_word_index.json', 'a')
    # data = json.load(f)
    # for line in data:
    #     print line 

    for article in t:
        if article not in article_words:
            hist = process_file(article)
            article_words[article] = hist

    f.write(json.dumps(article_words))
    f.close()

    return article_words


def company_index(index, companyList):
    """Creates a dictionary index of company name mapping to filenames 
    containing the company.

    index: json object of word_freq_index
    companyList: list of company names 
    returns: 
    """

    # json_data = open('freq_word_index.json', 'r')
    # data = json.load(json_data)

    company_d = {}
    for company in companyList:
        if company in data.items():
            # TODO: figure out how to find specific filename of where company is mentioned
            filename = ''
            company_d[company].append(filename) 


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


def most_common(hist):
    """Makes a list of the key-value pairs from a histogram and
    sorts them in descending order by frequency.

    hist: map from word to the number of times it appears
    returns: list of (word, frequency) pairs, sorted by frequency
    """
    t = []
    # create list of tuples with (frequency, word) sorted in descending order
    for word in hist:
        t.append((hist[word], word))

    t.sort(reverse=True)
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    
    hist: histogram (map from word to frequency
    num: number of words to print
    """
    t = most_common(hist)
    print 'The most common words are:'
    for freq, word in t[:num]:
        print word, '\t', freq





if __name__ == '__main__':

    t = os.listdir('news/')
    shortList = t[50:51]

    freq_word_index(shortList)