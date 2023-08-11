from pyfirmata import Arduino

portname = 'dev/ttyACM0'

def arduino_board():
    board = Arduino(portname)
    print("Arduino connection made!")

    return