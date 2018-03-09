import pyglet
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

@mywin.event
def on_draw():
    mywin.clear()
    with rc.default_shader:
        plane.draw()

        # fr.draw()

pos = cycle([0, .09])
def update(dt):

    sleep_time = np.random.random() / 5 + .05  # random numbers between 50 and 250 ms
    sleep(sleep_time)
    plane.position.x = next(pos)

pyglet.clock.schedule(update)

pyglet.app.run()