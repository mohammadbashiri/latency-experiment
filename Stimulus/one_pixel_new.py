import pyglet
import itertools
from stimulus import Stimulus
import numpy as np

platform = pyglet.window.get_platform()
display = platform.get_default_display()
screen = display.get_screens()[1]
mywin = pyglet.window.Window(fullscreen=True, screen=screen)

# initialize a stim object
mypoint = Stimulus(window=mywin, type='PLANE', x=mywin.width//2, y=mywin.height//2, width=4, height=4)

colors = (
    [255, 255, 255],
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255],
    [255, 255, 0],
    [255, 0, 255],
    [0, 255, 255],
)

@mywin.event
def on_draw():
    mywin.clear()
    for x, c in zip(np.linspace(950, 1050, len(colors)), colors):
        mypoint.x = int(x)
        mypoint.color = c
        mypoint.draw()

heights = itertools.cycle([mywin.height//2, mywin.height//2 + 100])
def update(dt, heights):
    mypoint.y = next(heights)

pyglet.clock.schedule(update, heights)

pyglet.app.run()
