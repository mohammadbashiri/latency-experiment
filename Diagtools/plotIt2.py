import numpy as np
from pyglet.gl import *
from collections import deque

def gen_data():
    x = round(np.random.random() * 2 - .5, 2)
    y = round(np.random.random() * 2 - .5, 2)
    return x, y


# def store_data(nsample):
#     dd = deque(maxlen=nsample)
#     while True:
#         data = yield
#         dd.append(data)
#         yield dd


def store_data(nsample):
    dd = deque(maxlen=nsample)
    ind = 0
    while True:
        data = yield
        if len(dd) < nsample:
            dd.append(data)
        else:
            dd[ind] = data
        ind += 1
        if ind == nsample:
            ind = 0

        yield dd


def record_data():
    ss = []
    while True:
        data = yield
        ss.append(data)
        yield ss

def ready_to_draw(dd, x_scale=1., x_offset=0., y_scale=1., y_offset=0., dist=1):  # gets a deque and
    # separate x and y and add t to every component
    ddxt = [(t*dist, dd[x][0]*x_scale+x_offset) for t, x in enumerate(range(len(dd)))]
    ddyt = [(t*dist, dd[x][1]*y_scale+y_offset) for t, x in enumerate(range(len(dd)))]
    # repeat the elements, except the first and the last ones
    ddxtr = tuple([e for ell in zip(ddxt[:-1], ddxt[1:]) for el in ell for e in el])
    ddytr = tuple([e for ell in zip(ddyt[:-1], ddyt[1:]) for el in ell for e in el])

    return ddxtr, ddytr


def draw(data, color=(0, 0, 0), line_width=3.):
    color = (color * int(len(data) / 2))

    pyglet.graphics.draw(int(len(data) / 2), pyglet.gl.GL_LINES,
                         ('v2f', data),
                         ('c3B', color))
    glLineWidth(line_width)


window = pyglet.window.Window()
pyglet.gl.glClearColor(0.9, 0.9, 0.9, 1)

dist = 3
nsample = window.width // dist
storeIt = store_data(nsample)
record = False

if record:
    recordIt = record_data()

def update(dt):
    pass

pyglet.clock.schedule(update)


@window.event
def on_draw():

    # read data
    data = gen_data()

    # store data for display
    next(storeIt)
    stored = storeIt.send(data)

    if record:
        next(recordIt)
        recordIt.send(data)

    # make the data ready to draw
    x_offset = 3 * window.height / 4.
    y_offset = window.height / 4.
    datax, datay = ready_to_draw(stored, x_scale=50, x_offset=x_offset,
                                 y_scale=50, y_offset=y_offset, dist=dist)

    # draw
    glClear(GL_COLOR_BUFFER_BIT)
    draw(datax, (0, 0, 255))
    draw(datay, (0, 0, 255))

pyglet.app.run()

if record:
    next(recordIt)
    print(recordIt.send('end'))
    # here goes the saving stuff!
