import paho.mqtt.client as mqtt
import json
import time
from sense_hat import SenseHat
from datetime import datetime
from collections import deque
import csv
# import pandas as pd
# from pandas import DataFrame as df
# from csv import writer, DictWriter
# from array import *
# import numpy as np
# from statistics import mean

csvfile = "store2.csv"
sense = SenseHat()
# Initialize deque with 120 None values
data_window = deque([], maxlen=120)
data_week = deque([], maxlen=840)
data_month = deque([], maxlen=3360)

# MQTT broker details
broker_address = "localhost"  # Use the address of your local MQTT broker
port = 1883                 # Default MQTT port
temp1 = float()
# Create an MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, port)

# Define the topic to which you want to publish
topic = "test_data"

start_time = time.time()
duration = 1000


def write_to_csv(file_name, var1, var2, var3, var4):
    # Open the CSV file in append mode
    with open(file_name, 'a', newline='') as csvfile:
        # Create a CSV writer object
        writer1 = csv.writer(csvfile)
        # Write the variables as a single line
        writer1.writerow([var1, var2, var3, var4])


def calculate_rolling_averagemean(data):
    total = sum(data)
    num1 = len(data)
    aveMean = total / num1
#   ave1 = mean([data_window])
#   print(ave)
    return aveMean


# Run the while loop for the specified duration
while (time.time() - start_time) < duration:
    data_window.appendleft(sense.get_temperature())
    data_week.appendleft(sense.get_temperature())
    data_month.appendleft(sense.get_temperature())
    data1 = {"temp": sense.get_temperature(),
             "Humidity": sense.get_humidity(),
             "Date": str(datetime.now()),
             "Ave1": calculate_rolling_averagemean(data_window),
             "AveWeek": calculate_rolling_averagemean(data_week),
             "AveMonth": calculate_rolling_averagemean(data_month),
             }


# Convert dictionary to JSON string
    message = json.dumps(data1)
    ave2 = calculate_rolling_averagemean(data_week)
    ave3 = calculate_rolling_averagemean(data_month)
    client.publish(topic, message)
    print(f"Published: {message} to topic: {topic}")
# Sleep for a short duration if needed
    time.sleep(1)
    rolling_avg = calculate_rolling_averagemean(data_window)
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    timestamp = datetime.now().isoformat()
    write_to_csv(csvfile, temperature, humidity, pressure, timestamp)
    print(f"Calculted Rolling averages: {data1}")
# Disconnect from the MQTT broker
else:
    client.disconnect()
