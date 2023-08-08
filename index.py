from sense_hat import SenseHat

while (True):
    sense = SenseHat()

    # Percentage of relative humidity
    humidity = sense.get_humidity()
    # Current temperature in degrees Celsius
    temp = sense.get_temperature()
    # Current pressure in Millibars
    pressure = sense.get_pressure()

    print(f"Humidity: {humidity}%")
    print(f"Temperature: {humidity}°C")
    print(f"Pressure: {pressure} mb")