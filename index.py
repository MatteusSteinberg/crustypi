from sense_hat import SenseHat
from datetime import datetime
from insertion import insert_data, delete_data
import RPi.GPIO as GPIO
from threading import Thread
from camera import capture_video

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# OUTPUT PIN FOR PIR SENSOR
GPIO.setup(10, GPIO.IN)

sense = SenseHat()

lastTime = ""

currentlyDetecting = False

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
    print(f"__________________________________________")
    # dd/mm/YY H:M:S
    print(f"Timestamp: {dt_string}")

    print(f"Humidity: {humidity}%")
    print(f"Temperature: {temp}°C")
    print(f"Pressure: {pressure} mb")

    motionDetected = i == 1

    if motionDetected and not currentlyDetecting:
        Thread(target=capture_video, args=(3, 'test'))

    if motionDetected:
        print("Motion detected")
        currentlyDetecting = True
    else:
        print("No motion detected")
        currentlyDetecting = False

    # To be removed
    delete_data()

    insert_data({
        "timestamp": dt_string,
        "humidity": humidity,
        "temperature": temp,
        "pressure": pressure,
        "detectedMotion": motionDetected
    })

    