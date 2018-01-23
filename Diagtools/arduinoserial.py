import serial
import time

# Set the port value
ARDUINO_PORT = 'COM9'
print('Connecting...')

with serial.Serial(ARDUINO_PORT, timeout=2.) as device:

    print('Connection Successful.  Emptying Buffer...')
    print(device.read())
    print('Buffer Empty.  Testing Signal...')

    while True:
        data_val = device.readline().strip()
        print(data_val)