from pyfirmata import Arduino, util
from datetime import datetime
from threading import Thread

portname = "/dev/ttyACM1"

# https://pypi.org/project/pyFirmata/

def arduino_board_test():
    board = Arduino(portname)
    print("Arduino connection made!")

    # analog_0 = board.get_pin('a:0:i')
    # digital_7 = board.get_pin('d:7:i')

    lastTime = ""

    it = util.Iterator(board)
    it.start()
    board.analog[0].enable_reporting()

    while True:
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        if lastTime == dt_string:
            continue
        lastTime = dt_string
        print(dt_string)

        print(f"board.analog[0].read(): {board.analog[0].read()}")

        print("Arduino loop")

class arduino_board():
    analogGasSensorValue: int = None
    board: Arduino = None
    it = None
    
    def __init__(self):
        self.board = Arduino(portname)
        self.it = util.Iterator(self.board)
        self.it.start()
        self.board.analog[0].enable_reporting()

        Thread(target=self.loop, args=(self))

    def loop(self):

        lastTime = ""
        
        while True:
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%dT%H:%M:%S.000Z")
            if lastTime == dt_string:
                continue
            lastTime = dt_string
            print(dt_string)

            reading: int = self.board.analog[0].read()

            print(f"board.analog[0].read(): {reading}")

            self.analogGasSensorValue = reading

            print("Arduino loop")


