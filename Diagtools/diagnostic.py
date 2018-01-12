import numpy as np
from pyglet.gl import *
from collections import deque

class Diagnose:

    def __init__(self, mode='sliding'):
        self.mode = mode

    def gen_data(self):
        x = round(np.random.random() * 2 - .5, 2)
        y = round(np.random.random() * 2 - .5, 2)
        return x, y

    def data_for_display(self, nsample):

        dd = deque(maxlen=nsample)

        if self.mode == 'sliding':
            while True:
                data = yield
                for el in data:
                    dd.append(el)
                yield dd

        elif self.mode == 'update':
            ind = 0
            while True:
                data = yield
                for el in data:
                    if len(dd) < nsample:
                        dd.append(el)
                    else:
                        dd[ind] = el
                    ind += 1
                    if ind == nsample:
                        ind = 0

                yield dd

    def ready_to_draw(self, dd, x_scale=1., x_offset=0., y_scale=1., y_offset=0., dist=1):  # gets a deque and
        # separate x and y and add t to every component
        ddxt = [(t * dist, dd[x][0] * x_scale + x_offset) for t, x in enumerate(range(len(dd)))]
        ddyt = [(t * dist, dd[x][1] * y_scale + y_offset) for t, x in enumerate(range(len(dd)))]
        # repeat the elements, except the first and the last ones
        ddxtr = tuple([e for ell in zip(ddxt[:-1], ddxt[1:]) for el in ell for e in el])
        ddytr = tuple([e for ell in zip(ddyt[:-1], ddyt[1:]) for el in ell for e in el])

        return ddxtr, ddytr

    def draw(self, data, color=(0, 0, 0), line_width=3.):
        color = (color * int(len(data) / 2))

        pyglet.graphics.draw(int(len(data) / 2), pyglet.gl.GL_LINES,
                             ('v2f', data),
                             ('c3B', color))
        glLineWidth(line_width)


class Visualize:

    def __init__(self, mode='sliding'):

        # create a diagnostic object
        ana_obj = Diagnose(mode)

        # create the update function, for pyglet to run!
        def update(dt):
            pass

        pyglet.clock.schedule(update)

        window = pyglet.window.Window()
        pyglet.gl.glClearColor(0.9, 0.9, 0.9, 1)

        dist = 5
        nsample = window.width // dist
        storeIt = ana_obj.data_for_display(nsample)

        @window.event
        def on_draw():

            # read data
            data = ana_obj.gen_data()

            # store data
            next(storeIt)
            stored = storeIt.send(data)

            # make the data ready to draw
            # make the data ready to draw
            x_offset = 3 * window.height / 4.
            y_offset = window.height / 4.
            datax, datay = ana_obj.ready_to_draw(stored, x_scale=50, x_offset=x_offset,
                                                 y_scale=50, y_offset=y_offset, dist=dist)

            # draw
            glClear(GL_COLOR_BUFFER_BIT)
            ana_obj.draw(datax)
            ana_obj.draw(datay)

        pyglet.app.run()

