'''
Measuring the display latency. This code works with the Arduino code: per_frame.io, and with the stimulus: Stim_with_tracking.py
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


dd = np.array(data).reshape(-1, 1)  # change this to 5 if measring delay, otherwise set to 3 for frame analysis
df = pd.DataFrame(data=dd, columns=["Chan1"])

filename = 'frame_checking'
df.to_csv('../Measurements/' + filename + '.csv', index=False)

# RB stands for Rigid Body. So these are the settings that are under Rigid Body in Edit Layout