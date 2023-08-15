from pyfirmata import Arduino, util
from datetime import datetime
from threading import Thread

portname = "/dev/ttyACM1"

# https://pypi.org/project/pyFirmata/

class arduino_board():
    board: Arduino = None
    it = None
    
    def __init__(self):
        self.board = Arduino(portname)
        print("Arduino connection made!")
        self.it = util.Iterator(self.board)
        self.it.start()
        self.board.analog[0].enable_reporting()

    def getSensorValues(self):
        return {
            "analogGasSensorValue": self.board.analog[0].read()
        }


