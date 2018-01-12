# from diagnostic import Visualize
#
# vis_obj = Visualize(mode='update')

from diagnostic import Diagnose
from pyglet.gl import *

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

