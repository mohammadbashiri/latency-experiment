import pyglet
import itertools
from stimulus import Stimulus
import numpy as np

from pyglet.window import key

platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_screens()[1]
mywin = pyglet.window.Window(fullscreen=True, screen=screen)


# get keyboard input
keys = key.KeyStateHandler()
mywin.push_handlers(keys)


# initialize a stim object
mypoint = Stimulus(window=mywin, type='PLANE', x=mywin.width//2, y=mywin.height//2, width=4, height=4)

colors = [
    [255, 255, 255],
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255],
    [255, 255, 0],
    [255, 0, 255],
    [0, 255, 255],
]

@mywin.event
def on_draw():
    mywin.clear()
    for x, c in zip(np.linspace(950, 1050, len(colors)), colors):
        mypoint.x = int(x)
        mypoint.color = c
        mypoint.draw()

heights = itertools.cycle([mywin.height//2, mywin.height//2 + 43])
def update(dt, heights):
    mypoint.y = next(heights)

    if keys[key.UP] and colors[0][0] < 255:
      colors[0][0] += 1
      colors[0][1] += 1
      colors[0][2] += 1
    elif keys[key.DOWN] and colors[0][0] > 0:
      colors[0][0] -= 1
      colors[0][1] -= 1
      colors[0][2] -= 1

    # print('red value is:', colors[0][0])


pyglet.clock.schedule(update, heights)

pyglet.app.run()
