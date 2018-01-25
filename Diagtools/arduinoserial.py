import serial
import time

# Set the port value
ARDUINO_PORT = 'COM9'
BAUDRATE = 9600
print('Connecting...')

with serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2.) as device:

    print('Connection Successful.  Emptying Buffer...')
    print(device.readline())
    print('Buffer Empty.  Testing Signal...')

    while True:
        data_val = device.readline().strip()
        data_val = data_val.split(sep=b',')
        print(tuple(map(int, data_val)))