import time
import paho.mqtt.client as paho
from decouple import config
import json

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker", rc)

class mqtt_client():
    client = paho.Client()

    broker_address = config("MQTT_ADDRESS")
    port = int(config("MQTT_PORT"))
    username = config("MQTT_USER")
    password = config("MQTT_PASSWORD")

    def __init__(self):
      self.client = paho.Client()
      self.client.on_connect = on_connect
      print(self.broker_address, self.port, self.username, self.password)

      self.client.username_pw_set(self.username, self.password)

      self.client.connect(self.broker_address, self.port, 60)

      self.client.loop_start()

    def close(self):
        self.client.loop_stop()

    def publish(self, topic, payload):
        if self.client.is_connected():
          self.client.publish(topic, json.dump(payload))
          print("Websocket data sent")
        else: 
           self.client.connect(self.broker_address, self.port, 60)

           if self.client.is_connected():
              self.client.loop_start()
              self.client.publish(topic, json.dump(payload))