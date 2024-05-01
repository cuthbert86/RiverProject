# subscriber.py
import paho.mqtt.client as mqtt
import json
import time

json_string = '{"temp": 39.27864456176758, "Humidity": 29.530689239501953, "Date": "2024-04-28T12:42:19.462117", "Ave1": 39.87668024698893, "AveWeek": 40.311465103260794, "AveMonth": 40.31132313804905}'
topic = "test_data"


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe, which need to put into on_connect
    # If reconnect after losing the connection with the broker, it will continue to subscribe to the raspberry/topic topic
    client.subscribe("test_data")


# The callback function, it will be triggered when receiving messages
def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload}")
    try:
       jstring =str(msg.payload.decode("utf-8","ignore"))
       print(jstring)
       process_json(jstring)
    except:
        print("oops")
    json_string = json.loads(jstring)
                
 #   data1 = jsondecode(json_string)
 #   print(json_string)
 #   json_string = msg.payload.decode("utf-8")
    #print("Received JSON string:", data1)



def process_json(d1):
    data = json.loads(d1)
    temp = data["temp"]
    humidity = data["Humidity"]
    timestamp = data["Date"]
    print("Temperature:", temp)
    print("Humidity:", humidity)
    print("Timestamp:", timestamp)


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
# Set the will message, when the Raspberry Pi is powered off, or the network is interrupted abnormally, it will send the will message to other clients
# client.will_set('raspberry/status', b'{"status": "Off"}')

# Create connection, the three parameters are broker address, broker port number, and keep-alive time respectively
client.connect("localhost", 1883, 60)
client.loop_start() 
# Set the network loop blocking, it will not actively end the program before calling disconnect() or the program crash

client.subscribe(topic)
client.loop_forever()
