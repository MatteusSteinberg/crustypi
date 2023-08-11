from pyfirmata import Arduino

portname = "/dev/ttyACM1"

# https://pypi.org/project/pyFirmata/

def arduino_board():
    board = Arduino(portname)
    print("Arduino connection made!")

    while True:
        print("Arduino loop")