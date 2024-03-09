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
#   ave1 = mean([data_window])
    print(aveMean)
    return aveMean


# data_window.append(df())

newdf = df.Temperature
print(newdf)

calculate_rolling_averagemean(newdf)
newdfave = calculate_rolling_averagemean(newdf)
df2 = df.PercentDO
calculate_rolling_averagemean(df2)
df2 = calculate_rolling_averagemean(df2)

bestfit = df2 - newdfave
line = bestfit / 2
print(bestfit)
print(line)