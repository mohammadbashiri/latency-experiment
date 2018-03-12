'''
This code works with the Arduino_switch_LED_by_python as an example.
In this code we are switching the points in the display, and sending a message to arduino to set LEDs.
The LED is just a feedback to make sure the code is working
'''

import pyglet
import serial
import numpy as np
import ratcave as rc
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
device = serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2.)
print("Emptying buffer")
device.readline()

trial = 0
last_trial = trial

@mywin.event
def on_draw():
    mywin.clear()
    with rc.default_shader:
        plane.draw()
        global last_trial
        if last_trial != trial:
            last_trial = trial
            device.write(b'S')
    fr.draw()


def start_next_trial(dt):
    global trial
    trial += 1
    plane.visible = True
    pyglet.clock.schedule_once(end_trial, .05)
pyglet.clock.schedule_once(start_next_trial, 0)

def end_trial(dt):
    plane.visible = False
    print(device.read_all())
    pyglet.clock.schedule_once(start_next_trial, np.random.random() / 5 + .05)

def update(dt):
    pass
pyglet.clock.schedule(update)

pyglet.app.run()
device.close()