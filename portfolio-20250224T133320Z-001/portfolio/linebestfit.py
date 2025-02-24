from datetime import datetime
from collections import deque
from csv import DictWriter, writer, reader
import pandas as pd
from pandas import DataFrame as df
import csv
# Your data dictionary


# CSV file path
csvfile = "store1.csv"
# Write data to CSV file
data = pd.read_csv(csvfile, delimiter=',')
rowCount = data.shape[0]
colcount = data.shape[1]
temp = df(data, columns = ["temp"])
total = df.sum(temp)
print(total)
print(rowCount)

csvpath = 'store1.csv'

df = pd.read_csv(csvpath)

print(df)

# data_window = array([])
def get_last_value(csvpath):
    # Initialize the last value variable
    last_value = None

    # Open the CSV file
    with open(csvpath, 'r') as csvfile:
        reader = csv.reader(csvfile)

        # Iterate through each row in the CSV file
        for row in reader:
            # Update the last value with the current row's last element
            temp = df(data, columns = ["total"])
            last_value = temp(row[-1])
            print(last_value)
    # Return the last value found
    return last_value


def calculate_rolling_averagemean(newdf):
    total = df.sum(temp)
    num1 = rowCount
    aveMean = total / num1
#   ave1 = mean([data_window])cuthbert/Desktop/node-red testing folder/
    print(aveMean)
    return aveMean


csvpath(get_last_value)

# data_window.append(df())

#dftemp = df.Temperature
#print(dftemp)
#dfDO = df.PercentDO
#print(dfDO)
#avetemp = calculate_rolling_averagemean(dftemp)
#print("average temperature = ", avetemp)
#aveDOpercent = calculate_rolling_averagemean(dfDO)
#print("average DO percentage = ", aveDOpercent)
#bestfit = aveDOpercent - avetemp
#line = (bestfit / 2) + avetemp
#print("best fit =", line)
#coefficent = aveDOpercent / avetemp
#print("coefficient = ", coefficent)
