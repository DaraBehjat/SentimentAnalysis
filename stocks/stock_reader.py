
import csv

ifile  = open('short_stock_datacsv.csv', "rU")
reader = csv.reader(ifile, dialect=csv.excel_tab)


def create_dates(reader, ticker):
    findDate = '%s Date' % ticker 
    for row in reader: 
        if findDate in row:
            datesList = list(row)
            del datesList[0]
        return datesList

def create_open(reader, ticker):
    findOpen = '%s PX_OPEN' % ticker 
    for row in reader: 
        if findOpen in row: 
            openList = list(row)
            del openList[0]
        return openList  

def create_close(reader, ticker):
    findClose = '%s PY_CLOSE' % ticker
    for row in reader: 
        if findClose in row:
            closing = list(row)
            del closing[0]
        return closing 



def change_in_p_list(t_open, t_close):
    """Function that creates a list of the percent change in price in a stock from
    a list of its opening price and its closing price.

    t_open: list of opening prices 
    t_close: list of closing prices

    returns: list of percent changes in stock for each company
    """

    price_change = []
    
    for i in range(len(t_open)):
        change = ((float(t_close[i]) - float(t_open[i])) / (float(t_open[i]))) * 100
        price_change.append(change)

    return price_change

def create_dictionary(t_date, t_change):
    """Function that creates a dictionary of date mapping to change in 
    stock price for a specific company. 

    t_date: list of dates
    t_change: list of price changes in stock

    returns: dictionary of dates (keys) to change in price (values)
    """
    temp = zip(t_date, t_change)

    d = {}
    for date, change in temp:
        d[date] = change 
    return d 



if __name__ == "__main__":

    # dates = create_dates(reader, 'BAC')
    opening = create_open(reader, 'BAC')
    # closing = create_close(reader, 'BAC')
    print opening 
    # print dates 
    # print closing 

    # change = change_in_p_list(opening, closing)
    # d = create_dictionary(dates, change)
    # print d 

    ifile.close()