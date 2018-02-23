from struct import unpack
import serial
import numpy as np
import pandas as pd

# Set the port value
ARDUINO_PORT = 'COM9'
BAUDRATE = 250000

POINTS = 2000
TOTAL_POINTS = 30000
data = []
print('Connecting...')

with serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2.) as device:
    print('Connection Successful.  Emptying Buffer and reading...')
    device.readline()

    while len(data) < TOTAL_POINTS * 11:
        data.extend(unpack('<' + 'I3H?' * POINTS, device.read(11 * POINTS)))


dd = np.array(data).reshape(-1, 5)
df = pd.DataFrame(data=dd, columns=['Time', "Chan1", "Chan2", 'Trial', 'LED_State'])
df.to_csv('../Measurements/s01_230218_white_randFreq_SegmentMode.csv')
