import paho.mqtt.client as mqtt
import json
import time
from sense_hat import SenseHat
from datetime import datetime
from collections import deque
# from array import *
# import numpy as np
# import pandas
# from statistics import mean


sense = SenseHat()
# Initialize deque with 120 None values
# data_window = deque([], maxlen=120)
# data_week = deque([], maxlen=840)
# data_month = deque([], maxlen=3360)

# MQTT broker details
broker_address = "localhost"  # Use the address of your local MQTT broker
port = 1883                 # Default MQTT port
# temp1 = float()
# Create an MQTT client instance
client = mqtt.Client("csv_publisher")

# Connect to the MQTT broker
client.connect(broker_address, port)

# Define the topic to which you want to publish
topic = "test_data"

start_time = time.time()
duration = 400


def calculate_rolling_averagemean(data):
    total = sum(data)
    num1 = len(data)
    aveMean = total / num1
#   ave1 = mean([data_window])
#   print(ave)
    return aveMean


# Run the while loop for the specified duration
while (time.time() - start_time) < duration:
#    data_window.appendleft(temp())
#    data_week.appendleft(sense.get_temperature())
#    data_month.appendleft(sense.get_temperature())
    data1 = {"temp": str(sense.get_temperature()),
             "Humidity": str(sense.get_humidity()),
             "Date": str(datetime.now()),
#             "Ave1": str(calculate_rolling_averagemean(data_window)),
#             "AveWeek": str(calculate_rolling_averagemean(data_week)),
#             "AveMonth": str(calculate_rolling_averagemean(data_month)),
             }


# Convert dictionary to JSON string
    message = json.dumps(data1)
#   ave2 = calculate_rolling_averagemean(data_week)
# print(ave2)
#    ave3 = calculate_rolling_averagemean(data_month)
# print (ave3)
    client.publish(topic, message)
    print(f"Published: {message} to topic: {topic}")
# Sleep for a short duration if needed
    time.sleep(1)

#    rolling_avg = calculate_rolling_averagemean(data_window)
#    print(f"Calculted Rolling averages: {data1}")
# Disconnect from the MQTT broker
else:
    client.disconnect()
