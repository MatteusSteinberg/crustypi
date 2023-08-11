from pyfirmata import Arduino
import time

portname = "/dev/ttyACM1"

# https://pypi.org/project/pyFirmata/

def arduino_board():
    board = Arduino(portname)
    print("Arduino connection made!")

    while True:
        time.sleep(10)
        print("Arduino loop")