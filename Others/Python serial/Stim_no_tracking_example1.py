'''
This code works with the Arduino_switch_LED_by_python as an example.
In this code we are switching the points in the display, and sending a message to arduino to set LEDs.
The LED is just a feedback to make sure the code is working
'''

import pyglet
import serial
import numpy as np
import ratcave as rc
from time import sleep
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

# define (and start) the serial connection
ARDUINO_PORT = 'COM9'
BAUDRATE = 250000
print('Connecting...')
device = serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=1.)
print("Emptying buffer")
device.readline()

@mywin.event
def on_draw():
    mywin.clear()
    with rc.default_shader:
        plane.draw()
        # fr.draw()

pos = cycle([0, .09])
ch = cycle([b'A', b'B'])
def update(dt):
    sleep_time = np.random.random() / 5 + .05  # random numbers between 50 and 250 ms
    sleep(sleep_time)
    device.write(next(ch))
    plane.position.x = next(pos)

pyglet.clock.schedule(update)

pyglet.app.run()
device.close()