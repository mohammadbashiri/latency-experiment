'''
Recording per frame display signal.
This code works with the Arduino code: per_frame.ino
'''

from struct import unpack
import serial
import numpy as np
import pandas as pd

# Set the port value
ARDUINO_PORT = 'COM9'
BAUDRATE = 250000

POINTS = 2000  # 2000
TOTAL_POINTS = 10000
data = []
print('Connecting...')

with serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2.) as device:
    print('Connection Successful.  Emptying Buffer and reading...')
    device.readline()

    while len(data) < TOTAL_POINTS * 2:
        data.extend(unpack('<' + 'H' * POINTS, device.read(2 * POINTS)))

# Save data
dd = np.array(data).reshape(-1, 1)
df = pd.DataFrame(data=dd, columns=["Chan1"])

filename = '-'
df.to_csv('../Measurements/per_frame/' + filename + '.csv', index=False)