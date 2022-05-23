import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import json

mqttBroker ="mqtt.eclipseprojects.io" 

client = mqtt.Client("Temperature_Inside")
client.connect("mqtt.eclipseprojects.io", 1883, 60)

PUBLISH_TO_TOPIC = "unitn/compcomp/temperature"

DEVICE_ID = "00:00:00:01"

def to_json_packet(device_id: str, temperature: float):
    values_to_parse = {
        "device_id": device_id,
        "temperature": temperature
    }
    json_object = json.dumps(values_to_parse, indent = 4)
    return json_object


while True:
    randNumber = uniform(20.0, 25.0)
    json_obj = to_json_packet(DEVICE_ID, randNumber)
    client.publish(PUBLISH_TO_TOPIC, json_obj)
    print(f"Just published {str(json_obj)} to topic {PUBLISH_TO_TOPIC}")
    time.sleep(3)