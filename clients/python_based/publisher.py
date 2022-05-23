import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import json
from datetime import datetime

NUM_OF_DRONES = 5
DEVICE_TYPE = "DRONE"
DEVICE_NAME = "Drone"

mqttBroker ="mqtt.eclipseprojects.io" 

client = mqtt.Client("Drones")
client.connect("mqtt.eclipseprojects.io", 1883, 60)

PUBLISH_TO_TOPIC = "unitn/compcomp/gps"

DEVICE_IDs = [str(DEVICE_NAME  + str(i)) for i in range(0, NUM_OF_DRONES)]

def to_gps(longtitude: float, latitude: float):
    position = {
        "longitude": longtitude,
        "latitude": latitude
    }
    # json_object = json.dumps(position, indent = 4)
    json_object = str(position)
    return json_object

def to_json_packet(device_id: str, position: str):
    dt = str(datetime.now())
    values_to_parse = {
        "device_type": DEVICE_TYPE,
        "device_id": device_id,
        "gps_position": position,
        "datetime": dt
    }
    json_object = json.dumps(values_to_parse, indent = 4)
    return json_object


while True:
    for i in range(0, NUM_OF_DRONES):
        randNumber = uniform(20.0, 25.0)
        json_obj = to_json_packet(DEVICE_IDs[i], to_gps(randNumber, randNumber))
        client.publish(PUBLISH_TO_TOPIC, json_obj)
        print(f"Just published {str(json_obj)} to topic {PUBLISH_TO_TOPIC}")
        time.sleep(0.1)
    time.sleep(5)