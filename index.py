from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

while (True):

    # Percentage of relative humidity
    humidity = sense.get_humidity()
    # Current temperature in degrees Celsius
    temp = sense.get_temperature()
    # Current pressure in Millibars
    pressure = sense.get_pressure()

    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Timestamp: {dt_string}")

    print(f"Humidity: {humidity}%")
    print(f"Temperature: {humidity}°C")
    print(f"Pressure: {pressure} mb")