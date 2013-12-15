import nltk
from nltk import bigrams
from nltk.probability import ELEProbDist, FreqDist
from nltk import NaiveBayesClassifier
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from pylab import *


pos_sntn = [('the company reported better than expected profit', 'positive'),
	          ('the company experienced growth', 'positive'),
	          ('the company reported positive EBITDA', 'positive'),
	          ('the beat analyst expectations', 'positive'),
			  ('the company is a dominant player in the market', 'positive')]
pos_sntn1 = [('the company stock gained 10 percent last quarter', 'positive'),
			 ('the company bought back shares last quarter', 'positive'),
			 ('the company reported better than expected EBITDA last quarter', 'positive'),
			 ('shares soared after beating analyst expexctations', 'positive')]
neg_sntn = [('the company filed for bankruptcy', 'negative'),
			  ('the employees went on strike', 'negative'),
			  ('the company reported weak earnings', 'negative'),
			  ('the company performed poorly', 'negative'),
			  ('the company underperformed within its sector', 'negative')]
neg_sntn1 = [('the company is broke', 'negative'),
			 ('the company stock fell 10 percent last quarter', 'negative'),
			 ('the company saw EBITDA figures fall', 'negative'),
			 ('the company is being investigated', 'negative'),
			 ('EBITDA growth slowed last quarter', 'negative'),
			 ('Earnings per share were down as compared to last quarter', 'negative'),
			 ('the company downgraded estimates for the coming year', 'negative'),
			 ('the company stock falls after new product release', 'negative'),
			 ('the company stock price fell during trading', 'negative')]


tst_sntn = [('Bank of America reported better than expected EPS', 'positive'),
			  ('JCPenney saw a boost in holiday sales', 'positive'),
			  ('RadioShack expects to begin closing stores', 'negative'),
			  ('General Electric announced it will be laying off employees', 'negative'),
			  ('Microsoft faces corrpution probe', 'negative')]



print 'Welcome to the Stock Sentiment Analyzer!' 
original = raw_input ("What company are you interested in learning more about? \n")
if len(original) >3 : 
    pass
else: 
    print 'Please enter a valid company name'



sentinces = []

for (words, sentiment) in pos_sntn + pos_sntn1 + neg_sntn + neg_sntn1 + tst_sntn:
	words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
	sentinces.append((words_filtered, sentiment))


	
def get_words_in_sentinces(sentinces):
	all_words = []
	for (words, sentiment) in sentinces:
		all_words.extend(words)
	return all_words
def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features

word_features = get_word_features(get_words_in_sentinces(sentinces))


#print word_features


def extract_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

#print extract_features(['love','this','car'])

training_set = nltk.classify.apply_features(extract_features , sentinces)

#print training_set


classifier = nltk.NaiveBayesClassifier.train(training_set)

def train(labeled_featuresets, estimator=ELEProbDist):
	
	# Create the P(label) distribution
	label_probdist = esitmator(label_freqdist)
	
	#Create the P(fval | label, fname) distribution
	feature_probdist = {}
	
	return NaiveBayesClassifier (label_probdist, feature_probdist)

"""print feature_probdist('positive')
print feature_probdist[('negative', 'contains(best)')].prob(True)"


print classifier.show most_informative_features(32)"""

sentence = 'Twitter shares soared on new product release.'

#print classifier.classify(extract_features(sentence.split()))




"""Visulization segment"""

"""Pie Chart"""

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = 'Positive', 'Negative', 'Neutral', 'Irrelevant'
fracs = [15,30,45, 10]

##  The highlights the FB wedge, pulling it out slightly from the pie.
explode=(0, 0.05, 0, 0)
pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
title('Sentiment Analysis', bbox={'facecolor':'0.8', 'pad':5})




"""Distribution graph"""
figure(2)
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Sentece Count Count')
plt.ylabel('Sentiment')
plt.title('Grammer Analysis')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)


"""Correlation Graph"""
figure(3)
ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

#plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            #arrowprops=dict(facecolor='black', shrink=0.05),
            #)

plt.ylim(-2,2)

show()

