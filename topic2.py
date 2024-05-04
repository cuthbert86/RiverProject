import paho.mqtt.client as mqtt
import json
import time
from datetime import datetime
from collections import deque
from csv import DictWriter, writer, reader
#import pandas as pd
#from pandas import DataFrame as df
import csv


# CSV file path
csvfile = "store1.csv"




# Define MQTT broker details
broker_address = "192.168.1.11"  # Change this to the IP address of your Pi if it's running on a different machine
port = 1883
topic = "test_data"
topic2 = "newtopic"

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

    return


def on_message(client, userdata, msg):
    # Decode the message payload from JSON
    data = json.loads(msg.payload)
    print("Received message:", data)
 #   json_string = '{"temp": "36.24469757080078", "Humidity": "37.3743380737305", "Date": "2024-03-22 00:13:27.122036"}'
 #   data1 = json.loads(json_string)
    temp = float(data["temp"])
    humidity = float(data['Humidity'])
    date = data["Date"]
    time.sleep(1)
    global data_window
    data_window.appendleft(temp)
    global data_week
    data_week.appendleft(temp)
    global data_month
    data_month.appendleft(temp)
    temp = truncate_float(temp)
    humidity = truncate_float(humidity)
    print("Temperature:", str(temp)[:4])
    print("Humidity:", str(humidity)[:4])
    print("Date:", date)
    day = float(calculate_rolling_averagemean(data_window))
    print("Day:", day)
    week = float(calculate_rolling_averagemean(data_week))
    print("Week:", week)
    month = float(calculate_rolling_averagemean(data_month))
    print("Month:", month)
    write_to_csv(csvfile, temp, humidity, date)
    message = {"temp": float(temp),
               "Humidity": float(humidity),
               "Date": str(date),
               "day": float(day),
               "week": float(week),
               "month": float(month)}
    sent1 = json.dumps(message)
    print({topic2}, {sent1})
    client.subscribe(topic2)
    client.publish(topic2, sent1)


def calculate_rolling_averagemean(data):
    total = sum(data)
    num1 = len(data)
    aveMean = total / num1
#   ave1 = mean([data_window])
#    print(aveMean)
    return aveMean


def write_to_csv(file_name, var1, var2, var3):
    # Open the CSV file in append mode
    with open(file_name, 'a', newline='') as csvfile:
        # Create a CSV writer object
        writer = csv.writer(csvfile)
        # Write the variables as a single line
        writer.writerow([var1, var2, var3])
    # Read the data point from the CSV file


def truncate_float(value, digits_after_point=4):
    pow_10 = 10 ** digits_after_point
    return (float(int(value * pow_10))) / pow_10

# Create an MQTT client instance
client = mqtt.Client()
# Set callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, port)
client.loop_forever()
