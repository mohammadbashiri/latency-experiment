from struct import pack, unpack
import serial
import time
import numpy as np
import matplotlib.pyplot as plt


# Set the port value
ARDUINO_PORT = 'COM9'
BAUDRATE = 250000

POINTS = 1000
print('Connecting...')

with serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2.) as device:
    print('Connection Successful.  Emptying Buffer and reading...')
    device.readline()
    data = unpack('<' + 'I2h' * POINTS, device.read(8 * POINTS))

dd = np.array(data).reshape(-1, 3)
plt.plot(dd[:, 0], dd[:, 1:])
plt.show()
