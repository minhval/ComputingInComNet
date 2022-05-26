# ComputingInComNet

1. Prerequisite

python: paho-mqtt
javascript: node, things to able to run html

2. Introduction
Server: containing a webpage for GPS tracker subscribing to an MQTT broker.
Clients: containing several kinds of emulations (cars, drones, ships, helicopters, etc) publishing GPS data to the MQTT broker.

Clients ----publish----> MQTT Broker <----subscribe---- Server

Clients ----GPS data----> MQTT Broker ----GPS data----> Server

3. How to run
3.1. Running the server
The only thing to do is run index.html using a browser.

3.2. Running the clients
Run commands as follows:

python3 publisher_moving_linearly.py 
python3 publisher_cars.py

to publish GPS data to the MQTT broker.
