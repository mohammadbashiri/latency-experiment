import serial
import numpy as np
import pandas as pd
from time import sleep
from itertools import cycle
import natnetclient as natnet
from struct import unpack

# define (and start) the serial connection
ARDUINO_PORT = 'COM9'
BAUDRATE = 250000
print('Connecting...')
device = serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2.)
print("Emptying buffer")
device.readline()


TOTAL_POINTS = 100000 # 1000000
data = []

# initialize natnet object
client = natnet.NatClient()  # read_rate=1000
LED = client.rigid_bodies['LED']

# change the position of the LED
pos = cycle([b'L', b'R'])
state = cycle([0, 1])
while len(data) < TOTAL_POINTS:
    next_pos = next(pos)
    next_state = next(state)
    # print(len(data))
    for i in range(np.random.randint(50, 250)):
        device.write(next_pos)
        data.extend([client.timestamp, -10 * LED.position.x, next_state])
        # print(-10 * LED.position.x, client.timestamp, next_label)

dd = np.array(data).reshape(-1, 3)
df = pd.DataFrame(data=dd, columns=['Time', "Position", 'LED_State'])

filename = 'checking'
df.to_csv('../Measurements/tracking_latency/' + filename + '.csv', index=False)

device.close()