import paho.mqtt.client as mqtt
import json
import time
from sense_hat import SenseHat
from datetime import datetime


sense = SenseHat()

# MQTT broker details
broker_address = "localhost"  # Use the address of your local MQTT broker
port = 1883         # Default MQTT port

# Create an MQTT client instance
client = mqtt.Client("csv_publisher")

# Connect to the MQTT broker
client.connect(broker_address, port)

# Define the topic to which you want to publish
topic = "test_data"

start_time = time.time()

# Define the duration of the loop in seconds (1 hour = 3600 seconds)
duration = 200

# Run the while loop for the specified duration
while (time.time() - start_time) < duration:
    # Your code here

# Create a dictionary for each row 
        data = {
        "temp": str(sense.get_temperature()),
        "DO": str(sense.get_temperature()),
        "Date": str(datetime.now())  
        }

# Convert dictionary to JSON string
        message = json.dumps(data)

# Publish the JSON data to the MQTT topic
        client.publish(topic, message)
        print(f"Published: {message} to topic: {topic}")

# Sleep for a short duration if needed
        time.sleep(1)
# Disconnect from the MQTT broker
else:
    client.disconnect()
