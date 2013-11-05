
import csv
with open('Example.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader: 
        print row