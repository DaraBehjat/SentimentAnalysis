
import string 


def positive_vocab_list():
    fin = open('sentiment/positive.rtf')

    positiveWords = []
    for line in fin:
        positiveWords.append(line.strip().split(' ')[0].lower())

    positive = ['positive'] * 2557
    pos_sntn3 = zip(positiveWords, positive)

    fin.close()

    return pos_sntn3

def negative_vocab_list():
    fin2 = open('sentiment/negative.txt')

    negativeWords = []
    for line in fin2:
        # if '*' in line:
        #     line.replace('*')('')
        negativeWords.append(line.strip().split(' ')[0].lower())

    negative = ['negative'] * 4661
    neg_sntn3 = zip(negativeWords, negative)

    fin2.close()

    return neg_sntn3


if __name__ == '__main__':
    neg_sntn3 = negative_vocab_list()
    print neg_sntn3
    pos_sntn3 = positive_vocab_list()

