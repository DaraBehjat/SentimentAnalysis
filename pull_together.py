from article_indices import *
from stock_reader import *
import numpy as np
import datetime
from pylab import *
import matplotlib.pyplot as plt


def find_company(rawinput, infoList):
    print rawinput
    for element in infoList:
        if element[0] == rawinput:
            current = element 
            return current
    return 'Sorry, your company is not available' 

# print find_company('facebook', infoList)
# 

def make_fundemental_dicts(infoList):
    print "Company Choices:"
    companyList =[]
    for i in infoList:
        print i[0]
        companyList.append(i[0])
    raw = raw_input("Please type the name of the company: ")
    current = find_company(str(raw), infoList)
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

    return article_dict, price_change_d

# print price_change_d

def make_filename_dict(article_dict, price_change_d):
# makes a dictionary that is {filename: (date, sentiment, stock price change)}
    actual_shit= {}
    # print article_dict
    for item in article_dict:
        if article_dict[item][0] != "Date Not Availible":
            # print article_dict[item][1]
            # print article_dict[item][0]
            try:
                actual_shit[item] = (article_dict[item][0],article_dict[item][1],price_change_d[article_dict[item][0]])
                
            except:
                # these were published on the weekend so change in price = $0
                actual_shit[item] = (article_dict[item][0],article_dict[item][1],0.0)
    return actual_shit



def stocks_plot(actual_shit):
    figure(1)
    for element in price_change_d:
        # turns stings of dates into date objects
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
     
    plt.title("Change in Stock and Published Articles")     
    plt.xlabel("Date")
    plt.ylabel("Change in Stock Price ($)")



def bar_chart(actual_shit):
    figure(2)
    plt.subplot(2, 1, 1) # rows, column, plot number
    sentimentCounter = {}
    # date: (avg sentiment, Delta $, total articles, positive articles, negative)
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

    print sentimentCounter
    
    year = 2013
    month = 11
    # print year, month, day
    start_date =datetime.datetime(year, month, 1)

    end_date =datetime.datetime(year, month, 17)
    # print current_date
    # plt.xlim([start_date, end_date])
    # plt.bar(current_date, 0,color='green')

    for count in sentimentCounter:
        element = count
        day = int(element[8:])
        year = int(element[:4])
        month = int(element[5:7])
        print year, month, day
        current_date =datetime.datetime(year, month, day)
        print current_date
        if sentimentCounter[count][0] > 0:
            plt.bar(current_date, sentimentCounter[count][1],color='green') # positive sentiment
        elif sentimentCounter[count][0] == 0:
            plt.bar(current_date, sentimentCounter[count][1],color='yellow') # neutral sentiment
        else:
            plt.bar(current_date, sentimentCounter[count][1],color='blue') # negative sentiment
        
    plt.title("Change in Stock Price and Average Sentiment")
    plt.xlabel("Time")
    plt.ylabel("Change in Price ($)")


    plt.subplot(2, 1, 2)
    date_hist =[]
    for count in sentimentCounter:
        element = count
        day = int(element[8:])
        year = int(element[:4])
        month = int(element[5:7])

        print sentimentCounter[count][3]
        print sentimentCounter[count][4]
        current_date = datetime.datetime(year, month, day)
        p1 = plt.bar( current_date, sentimentCounter[count][3], color='green', bottom= True)
        p2 = plt.bar( current_date, sentimentCounter[count][4], color='blue')
        plt.legend( (p1[0], p2[0]), ( 'Positive', 'Negative' ) )
    # plt.xlim([start_date, end_date])
    plt.xlabel("Time")
    plt.ylabel("Number of Articles")


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

    labels =  'Negative', 'Positive'
    #% of each sentiment category
    fracs = [neg/total, pos/total]

    ##  The highlights the FB wedge, pulling it out slightly from the pie.
    explode=(0, 0.05)
    pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
    title('Percent of Positive and Negative Articles', bbox={'facecolor':'0.8', 'pad':5})






if __name__ == "__main__":   

    infoList = [['ford','F'], ['facebook','FB'], ['cisco', 'CSCO'], ['microsoft', 'MSFT'],
            ['comcast','CMCSA'],['apple','AAPL'],['hewlett','HPQ'],['hp','HPQ'],['tesco','TSCDY'],
            ['ibm','IBM'],['bp','BP'],['coca','KO']]#, ('hilton','hltn'), ('qualcomm','qual')]#, ('bac',''), 'merrill', 'ge']
    # companyList = ['facebook','ford','microsoft','google'] ['ge','GE'], ['intel','INTC'], ,['hsbc','HSBC']['citigroup','C'],['jcpenney','JCP'],,['sirius', 'siri']['exxon','XOM'],['verizon','VZ'],['seimens','SI'],


    article_dict, price_change_d = make_fundemental_dicts(infoList)
    actual_shit = make_filename_dict(article_dict, price_change_d)
    stocks_plot(actual_shit)
    bar_chart(actual_shit)
    pie_chart(actual_shit)
    plt.show()
