import numpy as np
from pyglet.gl import *
from collections import deque

# Direct OpenGL commands to this window.
window = pyglet.window.Window()
pyglet.gl.glClearColor(0.9, 0.9, 0.9, 1)

nsample = 11
t = 0
dd = deque(maxlen=nsample * 2)

def update(dt):

    global dd, t, nsample

    # TODO: Remove Store/Draw coupling
    if t >= nsample:  # reset the time and clear the deque
        t = 0
        dd.clear()

    # TODO: Read/Draw coupling
    x = np.round(np.random.random() * 2 - .5, 2) + window.height/2  # reading data serialy


    if t > 0:
        dd.append(t * 5)  # multiplied by 5 to increase the distance between two points horizontally
        dd.append(x)
        dd.append(t * 5)
        dd.append(x)
        t += 2  # we are adding two points so increment by 2
    else:
        dd.append(t * 5)
        dd.append(x)
        t += 1  # we are adding one point, so increment by 1

pyglet.clock.schedule(update)


@window.event
def on_draw():

    global dd, t
    color = ((0, 0, 255) * t)

    print(tuple(dd))

    glClear(GL_COLOR_BUFFER_BIT)
    pyglet.graphics.draw(t, pyglet.gl.GL_LINES,
                         ('v2f', tuple(dd)),
                         ('c3B', color))
    glLineWidth(3.0)

pyglet.app.run()
