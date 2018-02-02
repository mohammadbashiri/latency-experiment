from struct import pack, unpack
import serial

# Set the port value
ARDUINO_PORT = 'COM9'
BAUDRATE = 250000
print('Connecting...')

with serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2.) as device:
    print('Connection Successful.  Emptying Buffer and reading...')

    device.readline()

    # for el in range(500):
    while True:
        packet = device.read(9)
        data = unpack('<I2hc', packet)
        print(data)
