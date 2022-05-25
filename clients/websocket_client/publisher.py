import paho.mqtt.client as mqtt 
from random import uniform
import time
import json
from datetime import datetime

# Povo Sommarive 5 address: lat 46.06680624453603, long 11.150220098559688
ORIGINAL_LATITUDE = 46.06680624453603
ORIGINAL_LONGITUDE = 11.150220098559688

NUM_OF_DRONES = 10
DEVICE_TYPE = "DRONE"
DEVICE_NAME = "DroneNo"

PUBLISH_TO_TOPIC = "unitn/compcomp/gps"
BROKER_URL = "test.mosquitto.org"
PORT = 8080
KEEP_ALIVE = 60

client = mqtt.Client(transport='websockets')
client.connect(BROKER_URL, PORT, KEEP_ALIVE)

DEVICE_IDs = [str(DEVICE_NAME  + str(i)) for i in range(0, NUM_OF_DRONES)]

DEVICES_LIST = {}
for id in DEVICE_IDs:
    device = {
        "device_id": id,
        "device_type": DEVICE_TYPE,
        "gps_latitude": ORIGINAL_LATITUDE,
        "gps_longitude": ORIGINAL_LONGITUDE
    }
    DEVICES_LIST[id] = device

def updateDevicePosition(id, lat, lon):
    DEVICES_LIST[id]["gps_latitude"] += lat
    DEVICES_LIST[id]["gps_longitude"] += lon


def to_json_packet(device_id: str):
    dt = str(datetime.now())

    device = DEVICES_LIST[device_id]

    values_to_parse = {
        "device_type": device["device_type"],
        "device_id": device["device_id"],
        "gps_latitude": device["gps_latitude"],
        "gps_longitude": device["gps_longitude"],
        "datetime": dt
    }
    json_object = json.dumps(values_to_parse, indent = 4)
    return json_object

while True:
    for id in DEVICE_IDs:
        randLat = uniform(-1, 1)
        randLon = uniform(-1, 1)
        updateDevicePosition(id, randLat, randLon)
        json_obj = to_json_packet(id)
        client.publish(PUBLISH_TO_TOPIC, json_obj)
        print(f"PUB: Just published {str(json_obj)} to topic {PUBLISH_TO_TOPIC}")
        time.sleep(0.1)
    time.sleep(3)