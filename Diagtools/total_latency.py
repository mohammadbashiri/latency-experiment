'''
Measuring the display latency.
This code works with the Arduino code: total_latency.ino, and with the stimulus: Stim_with_tracking.py
'''

from struct import unpack
import serial
import numpy as np
import pandas as pd

# Set the port value
ARDUINO_PORT = 'COM9'
BAUDRATE = 250000

POINTS = 2000
TOTAL_POINTS = 3000 #00
data = []
print('Connecting...')

with serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2.) as device:
    print('Connection Successful.  Emptying Buffer and reading...')
    device.readline()

    while len(data) < TOTAL_POINTS * 11:
        data.extend(unpack('<' + 'I3H?' * POINTS, device.read(11 * POINTS)))

# notify the user of finishing the data acquisition
# import pymsgbox
# pymsgbox.alert('Data Acquisition is finished.', title='VRLatency - Total Latency Measurement')


# Save data
dd = np.array(data).reshape(-1, 5)
df = pd.DataFrame(data=dd, columns=['Time', "Chan1", "Chan2", 'Trial', 'LED_State'])

filename = 'checking_msgbox'
df.to_csv('../Measurements/' + filename + '.csv', index=False)