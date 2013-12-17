
"""Module that evaluates positive or negative sentiment of string. 

Parts of code sourced from NLTK examples and comparable sentiment analysis codes:
http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/
"""

from sentiment_vocabulary import *


import nltk
from nltk import bigrams
from nltk.probability import ELEProbDist, FreqDist
from nltk import NaiveBayesClassifier
from collections import defaultdict

# variables below represent vocab for assessing positive/negative sentiment

pos_sntn = [('the company reported better than expected profit', 'positive'),
	          ('the company experienced growth', 'positive'),
	          ('the company reported positive EBITDA', 'positive'),
	          ('the beat analyst expectations', 'positive'),
	          ('the company accomplished clever durability', 'positive'),
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

# test sentences that train the model
tst_sntn = [('Bank of America reported better than expected EPS', 'positive'),
			  ('JCPenney saw a boost in holiday sales', 'positive'),
			  ('RadioShack expects to begin closing stores', 'negative'),
			  ('General Electric announced it will be laying off employees', 'negative'),
			  ('Microsoft faces corrpution probe', 'negative')]


# variables that create extensive vocab list but makes program too slow to run 
pos_sntn2 = positive_vocab_list()
neg_sntn2 = negative_vocab_list()


sentinces = []

# aggregates vocab into list called 'sentinces' and makes sure len(word) greater than 3 characters 
for (words, sentiment) in pos_sntn + pos_sntn1 + neg_sntn + neg_sntn1 + tst_sntn :#+ pos_sntn2 + neg_sntn2:
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
	"""Runs test sentences back through the model to train the model.
	"""
	# Create the P(label) distribution
	label_probdist = esitmator(label_freqdist)
	
	#Create the P(fval | label, fname) distribution
	feature_probdist = {}
	
	return NaiveBayesClassifier (label_probdist, feature_probdist)



if __name__ == "__main__":

	sentence = 'Apple stock soars after better than expected earnings'
	sentence2 = 'Apple loses shareholders as revenues fall. '

	print classifier.classify(extract_features(sentence.split()))
	print classifier.classify(extract_features(sentence2.split()))
