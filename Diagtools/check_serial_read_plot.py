from struct import pack, unpack
import serial
import numpy as np
import matplotlib.pyplot as plt
import time

# Set the port value
ARDUINO_PORT = 'COM9'
BAUDRATE = 250000

POINTS = 400
print('Connecting...')

with serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2.) as device:
    print('Connection Successful.  Emptying Buffer and reading...')
    device.readline()
    # time.sleep(.5)
    data = unpack('<' + 'I2H' * POINTS, device.read(8 * POINTS))


dd = np.array(data).reshape(-1, 3)
plt.plot(dd[:, 0] / 1000, dd[:, 1:])
# plt.scatter(dd[:, 0] / 1000, dd[:, 1], .5)
plt.show()
