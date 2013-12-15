from article_indices import *
from stock_reader import *
import numpy as np
# import matplotlib as plt

infoList = [('ford','F'), ('facebook','FB'), ('comcast', 'CMST'), ('google','GOOG')]#, ('microsoft','msft'), ('hilton','hltn'), ('qualcomm','qual')]#, ('bac',''), 'merrill', 'ge']
companyList = ['facebook','ford','microsoft','google']


current = infoList[0]
ifile  = open('stocks/stock_data_12_14.csv', "rU")
reader = csv.reader(ifile, dialect=csv.excel_tab)

ticker = current[1]
# print ticker
dates = create_dates(reader, ticker)
opening = create_open(reader, ticker)
closing = create_close(reader, ticker)



change = change_in_p_list(opening, closing)
# print change 
price_change_d = create_dictionary(dates, change)

ifile.close()



t = os.listdir('news/')
shortList = t[1:]


nestedDict = freq_word_index(shortList)
# print nestedDict
d = company_index(companyList, nestedDict)
# print len(d['microsoft'])


# # store the articles about microsoft to a list
relatedArticles = (d[current[0]])
# print relatedArticles

# file_name maps to (date, sentiment)
article_dict = store_sentiment(relatedArticles)

# print price_change_d

# makes a dictionary that is {filename: (date, sentiment, change)}
actual_shit= {}
# print article_dict
for item in article_dict:
    if article_dict[item][0] != "Date Not Availible":
        # print article_dict[item][1]
        # print article_dict[item][0]
        try:
            actual_shit[item] = (article_dict[item][0],article_dict[item][1],price_change_d[article_dict[item][0]])
            
        except:
            pass 
            # print "On weekend"
            # DO THIS 
            # date = article_dict[item][0]
            # new_date = date[:8] + str(int(date[8:])+1)
            # second_date = date[:8] + str(int(date[8:])+2)
            # print date, new_date
            # try:
            #     print price_change_d[new_date]
            # except:
            #     print price_change_d[second_date]

print actual_shit
# fig1 = plt.figure()

# what we need now:
# price_change_d for the whole picture of the stock market