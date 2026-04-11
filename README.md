# The River Project Brief Summary of Key Points

This project was ideally suited for me, I have a passion for the environment and it also gave me a great opportunity to learn about some aspects of IOT that I wasn't very knowledgeable about e.g. Mqtt and also work on improving my ability to use Python to collect live sensor data and produce live calcultions with it for my node-red dashboard.

[Raspberry Pi Sense Hat](https://github.com/astro-pi/python-sense-hat)


I used node-red to subscribe to the mqtt broker and get display data being published by the raspberry pi.  I added an event logging feature that will allow users to
input things via the data dashboard that they have seen in the field and help us understand the different data that the sensors are detecting from the environment.

[Node-red](https://nodered.org/)


Collect array is my program that runs on a raspberry pie (with senseHat attachement), it collect sensor data from your sense hat and create a rolling average with that data then send it via json to another platform too be displayed.  When I discovered the python object “deque” I immediately asked everyone I know who works with python  if they have ever used a “deque” but nobody I know has ever heard of it!  It is the ideal type of object to use when trying to calculate a rolling average of live data because when each new data point gets submitted it automatically pops out the oldest one.

[deque](https://www.geeksforgeeks.org/python/deque-in-python/)


