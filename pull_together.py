from article_indices import *
from stock_reader import *

infoList = [('ford','F'), ('facebook','FB'), ('comcast', 'CMST'), ('google','GOOG')]#, ('microsoft','msft'), ('hilton','hltn'), ('qualcomm','qual')]#, ('bac',''), 'merrill', 'ge']
companyList = ['facebook','ford','microsoft','google']


current = infoList[1]

ifile  = open('stocks/short_stock_datacsv.csv', "rU")
reader = csv.reader(ifile, dialect=csv.excel_tab)

ticker = current[1]
dates = create_dates(reader, ticker)
opening = create_open(reader, ticker)
closing = create_close(reader, ticker)


change = change_in_p_list(opening, closing)
# print change 
price_change_d = create_dictionary(dates, change)
# print d 

ifile.close()



t = os.listdir('news/')
shortList = t[1:]


nestedDict = freq_word_index(shortList)
# print nestedDict
d = company_index(companyList, nestedDict)
# print len(d['microsoft'])


# # store the articles about microsoft to a list
microsoft = (d[current[0]])
# print microsoft

# file_name maps to (date, sentiment)
article_dict = store_sentiment(microsoft)

print price_change_d

actual_shit= {}
for item in article_dict:
    if article_dict[item][0] != "Date Not Availible":
        print article_dict[item][0]
        print price_change_d[article_dict[item][0]]
