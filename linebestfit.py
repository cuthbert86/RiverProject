# from collections import deque
# from array import *
# import numpy as np
import pandas as pd

csv_file_path = '/home/cuthbert/Desktop/node-red testing folder/riverdatacsv.csv'

df = pd.read_csv(csv_file_path)

print(df)

# data_window = array([])


def calculate_rolling_averagemean(newdf):
    total = sum(newdf)
    num1 = 9457
    aveMean = total / num1
#   ave1 = mean([data_window])cuthbert/Desktop/node-red testing folder/
    print(aveMean)
    return aveMean


# data_window.append(df())

dftemp = df.Temperature
print(dftemp)
dfDO = df.PercentDO
print(dfDO)
avetemp = calculate_rolling_averagemean(dftemp)
print("average temperature = ", avetemp)
aveDOpercent = calculate_rolling_averagemean(dfDO)
print("average DO percentage = ", aveDOpercent)
bestfit = aveDOpercent - avetemp
line = (bestfit / 2) + avetemp
print("best fit =", line)
coefficent = aveDOpercent / avetemp
print("coefficient = ", coefficent)
