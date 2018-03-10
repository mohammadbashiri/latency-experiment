'''
This code works with the Arduino_switch_LED_by_python as an example.
In this code we are switching the points in the display, and sending a message to arduino to set LEDs.
The LED is just a feedback to make sure the code is working
'''

import pyglet
import serial
import numpy as np
import pandas as pd
import ratcave as rc
from time import sleep
from struct import unpack
from itertools import cycle

# create a window and project it on the display of your choice
platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_screens()[1]
mywin = pyglet.window.Window(fullscreen=True, screen=screen, vsync=False)
fr = pyglet.window.FPSDisplay(mywin)

# initialize a stim object
plane = rc.WavefrontReader(rc.resources.obj_primitives).get_mesh('Plane', drawmode=rc.POINTS)
plane.point_size = 10.
plane.position.xyz = 0, 0, -3
plane.rotation.x = 0
plane.scale.xyz = .2

# initialize data for receording
trial = 0.5
no_of_trials = 200
# POINTS = 2000
# TOTAL_POINTS = 10000  # 300000
data = []

# define (and start) the serial connection
ARDUINO_PORT = 'COM9'
BAUDRATE = 250000
print('Connecting...')
device = serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2)
print("Emptying buffer")
device.readline()

# ping test
dd = [78, 0]
while chr(dd[0]) != 'P':
    device.write(b'P')
    dd = unpack('<HI', device.read(6))
    print(chr(dd[0]))

print('init time from arduino is', dd[1]/1000, 'ms')


@mywin.event
def on_draw():
    mywin.clear()
    with rc.default_shader:
        plane.draw()
        # fr.draw()


pos = cycle([0, .09])
def update(dt):


    global trial, no_of_trials, data

    sleep_time = np.random.random() / 5 + .05  # random numbers between 50 and 250 ms
    sleep(sleep_time)
    plane.position.x = next(pos)

    dd = device.read_all()
    if (len(dd) == 11):
        print(trial, unpack('<I3H?', dd), len(dd))
        data.extend(unpack('<I3H?', dd))
        trial += 1
    # while len(data) < TOTAL_POINTS * 11:
    #     data.extend(unpack('<' + 'I3H?' * POINTS, device.read(11 * POINTS)))

    if trial > no_of_trials:
        # data.extend(unpack('<' + 'I3H?' * 2 * no_of_trials, device.read(11 * 2 * no_of_trials)))
        print('size of data for', trial - .5, 'trials is', len(data))
        pyglet.app.exit()

        # dd = np.array(data).reshape(-1, 5)
        # df = pd.DataFrame(data=dd, columns=['Time', "Chan1", "Chan2", 'Trial', 'LED_State'])
        #
        # filename = 's01_090318'
        # df.to_csv('../Measurements/' + filename + '.csv', index=False)


pyglet.clock.schedule(update)

pyglet.app.run()
device.close()