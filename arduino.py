from pyfirmata import Arduino
import time

portname = "/dev/ttyACM1"

# https://pypi.org/project/pyFirmata/

def arduino_board():
    board = Arduino(portname)
    print("Arduino connection made!")

    while True:
        analog_0 = board.get_pin('a:0:i')
        digital_7 = board.get_pin('d:7:i')

        time.sleep(10)
        print("Arduino loop")