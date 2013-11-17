
import csv
 
ifile  = open('short_stock_datacsv.csv', "rb")
reader = csv.reader(ifile)

for row in reader: 
    if "BAC Date" in row:
        bac_dates = list(row)
        del bac_dates[0]
    if "BAC PX_OPEN" in row:
        bac_open = list(row)
        del bac_open[0]
    if "BAC PY_CLOSE" in row:
        bac_close = list(row)
        del bac_close[0]


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

    bac_change = change_in_p_list(bac_open, bac_close)
    bac_dictionary = create_dictionary(bac_dates, bac_change)

    print bac_dictionary

    # print bac_dates
    # print bac_open
    # print bac_close
 
ifile.close()