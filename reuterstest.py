import nltk.classify.util
from nltk.corpus import reuters
from nltk.classify import NaiveBayesClassifier

def word_feats(words):
    return dict([(word, True) for word in words])

train_docs = [(word_feats(reuters.words(fileid)), category)
             for category in reuters.categories()
             for fileid in reuters.fileids(category) 
if fileid.startswith("train")]

test_docs = [(word_feats(reuters.words(fileid)), category)
             for category in reuters.categories()
             for fileid in reuters.fileids(category) 
if fileid.startswith("test")]

classifier = NaiveBayesClassifier.train(train_docs)
print nltk.classify.util.accuracy(classifier, test_docs) 
