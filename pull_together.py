from article_indices import *
from stock_reader import *
import numpy as np
import datetime
from pylab import *
import matplotlib.pyplot as plt

infoList = [('ford','F'), ('facebook','FB'), ('comcast', 'CMST'), ('google','GOOG'), ('microsoft','MSFT')]#, ('hilton','hltn'), ('qualcomm','qual')]#, ('bac',''), 'merrill', 'ge']
companyList = ['facebook','ford','microsoft','google']


def find_company(rawinput, infoList):
    for element in infoList:
        if element[0] == rawinput:
            current = element 
            return current
    return 'Sorry, your company is not available' 

# print find_company('facebook', infoList)
# 
current = find_company('facebook', infoList)
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

# print actual_shit
# fig1 = plt.figure()

# what we need now:
# price_change_d for the whole picture of the stock market


def stocks_plot(actual_shit):
    figure(1)
    for element in price_change_d:
        day = int(element[8:])
        year = int(element[:4])
        month = int(element[5:7])
        current_date =datetime.datetime(year, month, day)
        plt.scatter(current_date,price_change_d[element])
     
    for article in actual_shit:
        element = actual_shit[article][0]
        day = int(element[8:])
        year = int(element[:4])
        month = int(element[5:7])
     
        current_date =datetime.datetime(year, month, day)
       
        if actual_shit[article][1] =='positive':
            plt.plot(current_date,1,'or')
            # print "positive"
        else:
            # print "neg"
            plt.plot(current_date,-1,'or')
     
     
    plt.xlabel("Date")
    plt.ylabel("Change in Stock Price")
    # plt.show()



def bar_chart(actual_shit):
    figure(2)
    plt.subplot(2, 1, 1)
    sentimentCounter = {}
    # date: (avg sentiment, Delta $)
    for article in actual_shit:
        if actual_shit[article][0] in sentimentCounter:
            if actual_shit[article][1] == 'positive':
                sentimentCounter[actual_shit[article][0]][0] +=1
                sentimentCounter[actual_shit[article][0]][2] +=1
                sentimentCounter[actual_shit[article][0]][3] +=1
            else:
                sentimentCounter[actual_shit[article][0]][0] -= 1
                sentimentCounter[actual_shit[article][0]][2] +=1
                sentimentCounter[actual_shit[article][0]][4] +=1
        else:
            if actual_shit[article][1] == 'positive':
                sentimentCounter[actual_shit[article][0]] = [1, actual_shit[article][2], 1, 1, 0]
            else:
                sentimentCounter[actual_shit[article][0]] = [-1, actual_shit[article][2], 1, 0, 1]

    for count in sentimentCounter:
        element = count
        day = int(element[8:])
        year = int(element[:4])
        month = int(element[5:7])
     
        current_date =datetime.datetime(year, month, day)
        if sentimentCounter[count][0] >0:
            p1 = plt.bar(current_date, sentimentCounter[count][1],color='green')
        elif sentimentCounter[count][0] ==0:
            p2 = plt.bar(current_date, sentimentCounter[count][1],color='yellow')
        else:
            p3 = plt.bar(current_date, sentimentCounter[count][1],color='blue')
        
    plt.xlabel("Time")
    plt.ylabel()


    plt.subplot(2, 1, 2)
    date_hist =[]
    for count in sentimentCounter:
        element = count
        day = int(element[8:])
        year = int(element[:4])
        month = int(element[5:7])

        current_date =datetime.datetime(year, month, day)
        p1 = plt.bar( current_date, sentimentCounter[count][3], color='green' )
        p2 = plt.bar( current_date, sentimentCounter[count][4], color='blue')
        plt.legend( (p1[0], p2[0]), ( 'Positive', 'Negative' ) )



def pie_chart(actual_shit):
    figure(4, figsize=(6,6))
    total = 0.0
    pos = 0
    neg = 0

    for article in actual_shit:
        if actual_shit[article][1]== 'positive':
            pos +=1
            total +=1
        else:
            neg+=1
            total+=1

    ax = axes([0.1, 0.1, 0.8, 0.8])

    print pos/total
    print neg/total

    labels =  'Negative', 'Positive'
    #% of each sentiment category
    fracs = [neg/total,pos/total]

    ##  The highlights the FB wedge, pulling it out slightly from the pie.
    explode=(0, 0.05)
    pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
    title('Percent of Positive and Negative articles', bbox={'facecolor':'0.8', 'pad':5})




    

# stocks_plot(actual_shit)
bar_chart(actual_shit)
pie_chart(actual_shit)
plt.show()




# def plot17():
#     #--- the two samples ---
#     samples1 = np.array([1, 1, 1, 3, 2, 5, 1, 10, 10, 8])
#     samples2 = np.array([6, 6, 6, 1, 2, 3, 9, 12 ] )
    
#     N = 12 # number of bins
#     hist1 = [0] * (N)
#     hist2 = [0] * (N)
   
#     #--- create two histogram. Values of 1 go in Bin 0 ---
#     for x in samples1:
#         hist1[x-1] += 1
#     for x in samples2:
#         hist2[x-1] += 1

#     #--- display the bar-graph ---        
#     width = 1
#     p1 = plt.bar( np.arange(0,N)+0.5, hist1, width, color='y' )
#     p2 = plt.bar( np.arange(0,N)+0.5, hist2, width, color='m', bottom=hist1 )
#     plt.legend( (p1[0], p2[0]), ( 'hist1', 'hist2' ) )

