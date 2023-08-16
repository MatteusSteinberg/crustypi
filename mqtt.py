import paho.mqtt.client as paho
from decouple import config
import json
import ssl

def on_connect(client, userdata, flags, rc):
    if rc == 0:
      print("Connected to MQTT Broker")
    else:
      print("Connection failed with code", rc)

class mqtt_client():
    client = paho.Client(client_id="pi", protocol=paho.MQTTv5)

    broker_address = "a91938236da5469ca7780ce25a489b8f.s2.eu.hivemq.cloud"
    port = int(config("MQTT_PORT"))
    username = config("MQTT_USER")
    password = config("MQTT_PASSWORD")

    def __init__(self):
      self.client = paho.Client()
      self.client.on_connect = on_connect

      self.client.tls_set(tls_version=ssl.PROTOCOL_TLS)  # Set the TLS version

      self.client.username_pw_set(self.username, self.password)

      self.client.connect(self.broker_address, self.port, 60)

      self.client.loop_start()

    def close(self):
      print("Closed MQTT Connection")
      self.client.loop_stop()

    def publish(self, topic, payload):
      if self.client.is_connected():
        self.client.publish(topic, json.dumps(payload))
        print("MQTT data sent")