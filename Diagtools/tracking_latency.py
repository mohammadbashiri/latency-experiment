import serial
import numpy as np
import pandas as pd
from time import sleep, time, perf_counter
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
for trial, next_pos in enumerate(pos):
    if len(data) > TOTAL_POINTS:
        break

    device.write(next_pos)
    start_time = perf_counter()
    while (perf_counter() - start_time) < .04:
        t, led_pos = perf_counter(), -10 * LED.position.x
        sleep(.001)
        if len(data) == 0 or data[-1][0] != client.timestamp:
            data.append([client.timestamp, t, led_pos, trial, 0 if next_pos == b'L' else 1])

    sleep(np.random.random() * .1 + .03)

df = pd.DataFrame(data=data, columns=['Timestamp', 'Time', "Position", 'Trial', 'LED_state'])

filename = 'checking'
df.to_csv('../Measurements/tracking_latency/' + filename + '.csv', index=False)

device.close()