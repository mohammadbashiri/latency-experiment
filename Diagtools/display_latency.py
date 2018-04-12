'''
Measuring the display latency.
This code works with the Arduino code: display_latency.ino
'''

import pyglet
pyglet.options['debug_gl'] = False
pyglet.options['debug_gl_trace'] = False
import serial
import numpy as np
import pandas as pd
import ratcave as rc
from struct import unpack

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

# define (and start) the serial connection
ARDUINO_PORT = 'COM9'
BAUDRATE = 250000
print('Connecting...')
device = serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2.)
print("Emptying buffer")
device.readline()

trial = 0
last_trial = trial
POINTS = 240
TOTAL_POINTS = 1000000
data = []

@mywin.event
def on_draw():
    mywin.clear()
    with rc.default_shader:
        plane.draw()
        global last_trial
        if last_trial != trial:
            last_trial = trial
            device.write(b'S')
    # fr.draw()


def save_data(data):
    dd = np.array(data).reshape(-1, 3)
    df = pd.DataFrame(data=dd, columns=['Time', "Chan1", 'Trial'])
    filename = 'testing'
    df.to_csv('../Measurements/disp_latency/' + filename + '.csv', index=False)


def start_next_trial(dt):
    global trial
    trial += 1
    plane.visible = True
    pyglet.clock.schedule_once(end_trial, .05)
pyglet.clock.schedule_once(start_next_trial, 0)


def end_trial(dt):
    global data
    plane.visible = False
    dd = unpack('<' + 'I2H' * POINTS, device.read(8 * POINTS))
    data.extend(dd)
    if len(data) > TOTAL_POINTS:
        save_data(data)
        pyglet.app.exit()
    pyglet.clock.schedule_once(start_next_trial, np.random.random() / 5 + .1)


def update(dt):
    pass
pyglet.clock.schedule(update)

pyglet.app.run()
device.close()