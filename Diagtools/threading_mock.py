from diagnostic import Diagnose
from pyglet.gl import *
from threading import Thread
from collections import deque
import numpy as np
import time


def readdata_thread_func(interval=.001):
    global val
    val = deque(maxlen=1)
    while True:
        # read data
        time.sleep(interval)
        val.append(ana_obj.gen_data())
        print(val)


if __name__ == '__main__':

    readdata_thread = Thread(target=readdata_thread_func, daemon=True)
    readdata_thread.start()

    # create a diagnostic object
    ana_obj = Diagnose(mode='update')

    # create the update function, for pyglet to run!
    def update(dt):
        pass

    pyglet.clock.schedule(update)

    window = pyglet.window.Window()
    pyglet.gl.glClearColor(0.9, 0.9, 0.9, 1)

    dist = 5
    nsample = window.width // dist
    storeIt = ana_obj.data_for_display(nsample)

    # THIS IS THE WHILE LOOP IN A NORMAL MULTITHREADING WE NEED TO GET THE DATA FASTER!

    @window.event
    def on_draw():

        # # read data
        # val = ana_obj.gen_data()
        print(val, 'draw')
        # store data
        next(storeIt)
        stored = storeIt.send(val)

        # make the data ready to draw
        # make the data ready to draw
        x_offset = 3 * window.height / 4.
        y_offset = window.height / 4.
        datax, datay = ana_obj.ready_to_draw(stored, x_scale=50, x_offset=x_offset,
                                             y_scale=50, y_offset=y_offset, dist=dist)

        # draw
        glClear(GL_COLOR_BUFFER_BIT)
        ana_obj.draw(datax, color=(0, 255, 0))
        ana_obj.draw(datay, color=(255, 0, 0))

    pyglet.app.run()