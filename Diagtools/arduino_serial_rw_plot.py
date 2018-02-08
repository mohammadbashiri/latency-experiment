from struct import pack, unpack
import serial
import numpy as np
import matplotlib.pyplot as plt
import time
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

# plt.scatter(dd[:, 0] / 1000, dd[:, 1], .5)

df = pd.DataFrame(data=dd, columns=['Time', "Chan1", "Chan2", 'Trial', 'LED_State'], index=dd[:, 0])
df.to_csv('VR_latency_data.csv')
# df.plot(x='Time', y=["Chan1", "Chan2", 'LED_State'])

# df['TrialTime'] = 0
# for trial, dd in df.groupby('Trial'):
#     df.loc[df.Trial == trial, 'TrialTime'] = dd.Time - dd.Time.min()
#
# df.groupby('LED_State').plot(x='TrialTime', y=["Chan1", "Chan2", 'LED_State'])
# # plt.plot(dd[:, 0] / 1000, dd[:, 1:])
# plt.show()
