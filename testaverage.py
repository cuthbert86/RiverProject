import paho.mqtt.client as mqtt
import json
import time
from sense_hat import SenseHat
from datetime import datetime
from collections import deque
from array import *
import numpy as np
#import pandas
import array as arr
from statistics import mean


sense = 8
# Initialize deque with 120 None values
data_window = deque([], maxlen=120)

# MQTT broker details
broker_address = "localhost"  # Use the address of your local MQTT broker
port = 1883                 # Default MQTT port
temp1 = float()
# Create an MQTT client instance
client = mqtt.Client("csv_publisher")

# Connect to the MQTT broker
client.connect(broker_address, port)

# Define the topic to which you want to publish
topic = "test_data"

start_time = time.time()


duration = 300

def calculate_rolling_averagemean(data_window):
    total = sum(data_window)
    num1 = len(data_window)
    
    ave1 = total / 120
    
    #ave1 = mean([data_window])
    print(ave1)
    return ave1


# Run the while loop for the specified duration
while (time.time() - start_time) < duration: 
    data_window.appendleft(sense)
    data1 = {
    "temp": str(sense),
    "DO": str(sense),
    "Date": str(datetime.now()),  # assuming date is in column 1 (index 0)
    "Ave1" : str(calculate_rolling_averagemean(data_window))
    }
    

# Convert dictionary to JSON string
    message = json.dumps(data1)
    ave2 = calculate_rolling_averagemean
    print() 
    client.publish(topic, message)
    print(f"Published: {message} to topic: {topic}")
# Sleep for a short duration if needed
    time.sleep(1)

    rolling_avg = calculate_rolling_averagemean(data_window)
    print(f"Rolling average of the last 24 hours: {rolling_avg}")
# Disconnect from the MQTT broker
else:
    client.disconnect()



