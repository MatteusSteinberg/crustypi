from pyfirmata import Arduino, util
import time
from datetime import datetime

portname = "/dev/ttyACM1"

# https://pypi.org/project/pyFirmata/

def arduino_board():
    board = Arduino(portname)
    print("Arduino connection made!")

    analog_0 = board.get_pin('a:0:i')
    digital_7 = board.get_pin('d:7:i')

    it = util.Iterator(board)
    it.start()
    board.analog[0].enable_reporting()

    while True:
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        print(dt_string)

        print(f"board.analog[0].read(): {board.analog[0].read()}")

        time.sleep(10)
        print("Arduino loop")