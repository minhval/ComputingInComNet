import paho.mqtt.client as mqtt

SUBSCRIBE_TO_TOPIC = "unitn/compcomp/gps"
BROKER_URL = "test.mosquitto.org"
PORT = 8080
KEEP_ALIVE = 60

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(SUBSCRIBE_TO_TOPIC)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload.decode("utf-8")))
    print(f"SUB: From topic {str(msg.topic)} received message {str(msg.payload.decode('utf-8'))}")

client = mqtt.Client(transport='websockets')
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER_URL, PORT, KEEP_ALIVE)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()