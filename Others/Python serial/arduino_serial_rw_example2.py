'''
This code works with the "Arduini_switch_LED_by_python.ino" in the Arduino example folder
'''

import serial
import numpy as np
from time import sleep

ARDUINO_PORT = 'COM9'
BAUDRATE = 250000

print('Connecting...')
with serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2.) as device:

    print("Emptying buffer")
    device.readline()

    while True:
        device.write(b'H')
        print(device.readline())