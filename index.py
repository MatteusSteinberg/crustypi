from sense_hat import SenseHat
from datetime import datetime
from insertion import insert_data, create_table
import RPi.GPIO as GPIO
from arduino import arduino_board
import signal
from mqtt import mqtt_client
import paho.mqtt.client as paho
from threading import Thread

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# OUTPUT PIN FOR PIR SENSOR
GPIO.setup(10, GPIO.IN)

sense = SenseHat()

lastTime = ""

currentlyDetecting = False

create_table()

arduino = arduino_board()

mqtt = mqtt_client()

# ON PROGRAM CLOSE START
def on_shutdown():
    mqtt.close()

signal.signal(signal.SIGINT, on_shutdown)
# ON PROGRAM CLOSE END

while (True):
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    # Avoid duplicate data sets - No reason to log between milliseconds
    if lastTime == dt_string:
        continue
    lastTime = dt_string

    # Percentage of relative humidity
    humidity = sense.get_humidity()
    # Current temperature in degrees Celsius
    temp = sense.get_temperature()
    # Current pressure in Millibars
    pressure = sense.get_pressure()

    i = GPIO.input(10)

    motionDetected = i == 1

    if motionDetected:
        currentlyDetecting = True
    else:
        currentlyDetecting = False
    
    arduinoSensors = arduino.getSensorValues()
    analogGasSensorValue = arduinoSensors['analogGasSensorValue']

    data = {
        "timestamp": dt_string,
        "humidity": humidity,
        "temperature": temp,
        "pressure": pressure,
        "detectedMotion": motionDetected,
        "gas": analogGasSensorValue
    }

    insert_data(data)

    mqtt.publish("sensordata", data)

    