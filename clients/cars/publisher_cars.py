import paho.mqtt.client as mqtt 
from random import uniform
import time
import json
from datetime import datetime
import numpy as np
import sys, getopt

DEFAULT_NUMBER_OF_CARS = 3

def publishing(num_of_cars: int):

    # Povo Sommarive 5 address: lat 46.06680624453603, long 11.150220098559688
    ORIGINAL_LATITUDE = 46.06680624453603
    ORIGINAL_LONGITUDE = 11.150220098559688

    # NUM_OF_DRONES = int(sys.argv[1])
    NUM_OF_DRONES = num_of_cars
    DEVICE_TYPE = "CAR"
    DEVICE_NAME = "CarNo"


    NUM_OF_CIRCLE_POINTS = 150
    point_skip = int(NUM_OF_CIRCLE_POINTS / (NUM_OF_DRONES))

    RADIUS = 0.0001
    theta = np.linspace(0, 2 * np.pi, NUM_OF_CIRCLE_POINTS)
    a1 = ORIGINAL_LATITUDE + RADIUS * np.cos(theta)
    b1 = ORIGINAL_LONGITUDE + RADIUS * np.sin(theta)
    starting_point = 1
    skip_point_list = []
    for i in range(0, NUM_OF_DRONES):
        skip_point_list.append(starting_point)
        starting_point += point_skip

    def calculate_slope(x1, y1, x2, y2):
        return (float)(y2-y1)/(x2-x1)

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

    def updateDevicePosition(id: str, lat: float, lon: float):
        DEVICES_LIST[id]["gps_latitude"] = lat
        DEVICES_LIST[id]["gps_longitude"] = lon


    def to_json_packet(device_id: str):
        dt = str(datetime.now())
        dt = datetime.strptime(dt , '%Y-%m-%d %H:%M:%S.%f')
        dt = dt.strftime("%Y-%m-%d %H:%M:%S")

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

    skip = 0
    SKIP_JUMP = 0.0001 # original
    SKIP_JUMP = 0.00001 # original
    SLEEP_TIME = 1 # second
    while True:
        # for id in DEVICE_IDs:
        for i in range(0, NUM_OF_DRONES):

            x = a1[skip_point_list[i]]
            y = b1[skip_point_list[i]]
            slope = calculate_slope(ORIGINAL_LATITUDE, ORIGINAL_LONGITUDE, x, y)
            print(f"x = {x}, y = {y}, s = {slope}")

            device_id = DEVICE_IDs[i]
            x0 = ORIGINAL_LATITUDE
            y0 = ORIGINAL_LONGITUDE
            
            current_x = ORIGINAL_LATITUDE + skip
            current_y = slope * (current_x - x0) + y0

            updateDevicePosition(DEVICE_IDs[i], current_x, current_y)
            json_obj = to_json_packet(DEVICE_IDs[i])
            client.publish(PUBLISH_TO_TOPIC, json_obj)
            print(f"PUB: Just published {str(json_obj)} to topic {PUBLISH_TO_TOPIC}")
            time.sleep(0.1)

        skip += SKIP_JUMP
        time.sleep(SLEEP_TIME)

def main(argv):
   num_of_vehicle = DEFAULT_NUMBER_OF_CARS
   try:
      opts, args = getopt.getopt(argv,"hn:",["num="])
   except getopt.GetoptError:
      print ('publisher_cars.py -n <numberofvehicles>')
      print ('publisher_cars.py --num=numberofvehicles>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
            print ('publisher_cars.py -n <numberofvehicles>')
            print ('publisher_cars.py --num=numberofvehicles>')
            sys.exit()
      elif opt in ("-n", "--num"):
         num_of_vehicle = int(arg)
   return num_of_vehicle

if __name__ == "__main__":
   nCars = main(sys.argv[1:])
   print ('Number of cars ', nCars)
   publishing(nCars)
