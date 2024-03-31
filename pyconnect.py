import paho.mqtt.client as mqtt
import time
import json
# import time
# from datetime import datetime
from collections import deque
import csv
# from csv import DictWriter, writer, reader
import pandas as pd
from pandas import DataFrame as df


broker_address = "86.24.78``.58"
hostname = "raspberrypi"
broker_port = 80
topic = "data1"
client = mqtt.Client("raspberrypi")

# CSV file path
csvfile = "store1.csv"
# Write data to CSV file


data_window = deque([], maxlen=120)
data_week = deque([], maxlen=840)
data_month = deque([], maxlen=3360)
data_3month = deque([], maxlen=10020)
json_string = '{"temp": "36.24469757080078", "Humidity": "37.37043380737305", "Date": "2024-03-22 00:13:27.122036"}'
data1 = json.loads(json_string)


# Now you can access the data fields individually
# temp = float()
humidity = float()
date = data1["Date"]
day = float()
week = float()
month = float()


# Define callback functions for MQTT events
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)
    global data5
    data5 = pd.read_csv(csvfile, delimiter=',')
    global rowCount
    rowCount = data5.shape[0] + 1
    colcount = data5.shape[1]
    global temp5
    temp5 = df(data5, columns=["temp"])
    global total
    total = df.sum(temp5)
    return data5, rowCount, temp5, total


def on_message(client, userdata, msg):
    # Decode the message payload from JSON
    data = json.loads(msg.payload)
    print("Received message:", data)
    json_string = '{"temp": "36.24469757080078", "Humidity": "37.37043380737305", "Date": "2024-03-22 00:13:27.122036"}'
    data1 = json.loads(json_string)
    temp = float(data["temp"])
    humidity = float(data["Humidity"])
    date = data1["Date"]
    time.sleep(1)
    global data_window
    data_window.appendleft(temp)
    global data_week
    data_week.appendleft(temp)
    global data_month
    data_month.appendleft(temp)
    print("Temperature:", temp)
    print("Humidity:", humidity)
    print("Date:", date)
    day = float(calculate_rolling_averagemean(data_window))
    print("Day:", day)
    week = float(calculate_rolling_averagemean(data_week))
    print("Week:", week)
    month = float(calculate_rolling_averagemean(data_month))
    print("Month:", month)
    global data5
    data5 = pd.read_csv(csvfile, delimiter=',')
    global rowCount
    rowCount = data5.shape[0]
    colcount = data5.shape[1]
    global temp5
    temp5 = df(data5, columns=['temp'])
    total = df.sum(temp5)
    t2 = total
    row2 = rowCount + 1
    write_to_csv(csvfile, temp, humidity, date, total, rowCount)


def calculate_rolling_averagemean(data):
    total = sum(data)
    num1 = len(data)
    aveMean = total / num1
#   ave1 = mean([data_window])
#    print(aveMean)
    return aveMean


def write_to_csv(file_name, var1, var2, var3, var4, var5):
    # Open the CSV file in append mode
    with open(file_name, 'a', newline='') as csvfile:
        # Create a CSV writer object
        writer1 = csv.writer(csvfile)
        # Write the variables as a single line
        writer1.writerow([var1, var2, var3, var4, var5])
    # Read the data point from the CSV file


client.on_connect = on_connect
client.on_message = on_message


client.connect(hostname, broker_port, 60)

client.connect(broker_address, broker_port, 60)
client.loop_start()
