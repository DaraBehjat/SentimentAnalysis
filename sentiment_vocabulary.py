
import string 


def positive_vocab_list():
    """Creates a list of tuples ('word', 'positive') from text file. 
    returns: list of tuples
    """
    fin = open('sentiment/positive.rtf')

    positiveWords = []
    for line in fin:
        positiveWords.append(line.strip().split(' ')[0].lower().replace('*', ''))
    
    # f = open('new_pos.txt','w')
    # f.write('[')
    # for word in positiveWords:
    #     f.write("(%s,'positive'),\n" % (word))
    # f.write(']')
    # f.close()
    positive = ['positive'] * 2557
    pos_sntn3 = zip(positiveWords, positive)

    fin.close()

    return pos_sntn3

def negative_vocab_list():
    """Creates a list of tuples from text file and matches each word to 
    negative.
    returns: list of tuples ('word' 'negative')
    """
    fin2 = open('sentiment/negative.txt')

    negativeWords = []
    for line in fin2:
        negativeWords.append(line.strip().split(' ')[0].lower().replace('*', ''))

    negative = ['negative'] * 4661
    neg_sntn3 = zip(negativeWords, negative)

    fin2.close()

    return neg_sntn3


if __name__ == '__main__':
    neg_sntn3 = negative_vocab_list()
    # print neg_sntn3
    pos_sntn3 = positive_vocab_list()
    # print pos_sntn3

