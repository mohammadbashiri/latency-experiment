import sys
sys.path.append("../Diagtools") # Adds higher directory to python modules path.
from diagnostic import Diagnose
from pyglet.gl import *
from threading import Thread
from collections import deque
import numpy as np
import time
import serial
import time

# set the frequency of data reading - this is in terms of
def readdata_thread_func(interval=.01): # interval is in second

    global data_buffer
    data_buffer = deque(maxlen=5) # data buffer - specifies how much data you wanna store (this case latest 5 data)
    data_read = deque(maxlen=2) # what is coming from arduino(one value for two channels at a time -> so two values)

    # Set the port value
    ARDUINO_PORT = 'COM9'
    print('Connecting...')

    with serial.Serial(ARDUINO_PORT, timeout=2.) as device:

        print('Connection Successful.  Emptying Buffer...')
        print(device.readlines())
        print('Buffer Empty.  Testing Signal...')

        # Ping Test
        device.write(b'D')
        msg = device.readline()
        print(msg)
        if not b'Confirmation' in msg:
            raise ValueError("word 'Confirmation' not in message.  Ping test not successful.")
        else:
            print('Signaling Successful!')

        while True:
            time.sleep(interval) # give some space to other programs to run (in this case image rendering)
            # read data - this is a loop that read two data
            for sensor in (b'A', b'B'):
                device.write(sensor)
                data_val = device.readline().strip()
                # change data from string to float
                data_read.append(float(data_val))

            data_buffer.append(tuple(data_read))
            # print(data_buffer, 'Buffer!')


if __name__ == '__main__':

    readdata_thread = Thread(target=readdata_thread_func, daemon=True)
    readdata_thread.start()

    # create a diagnostic object
    ana_obj = Diagnose(mode='slide')

    window = pyglet.window.Window(600, 300, resizable=True, vsync=True)
    fps_display = pyglet.window.FPSDisplay(window)

    pyglet.gl.glClearColor(0.9, 0.9, 0.9, 1)  # background color

    i = 0
    label = pyglet.text.Label(str(i),
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

    dist = 1  # this is the distance between each data point on the graph!
    nsample = window.width // dist
    storeIt = ana_obj.data_for_display(nsample)

    # Create the update function, for pyglet to run!
    def update(dt):
        pass

    pyglet.clock.schedule(update)


    @window.event
    def on_draw():

        # store data
        next(storeIt)
        stored = storeIt.send(data_buffer)

        if len(stored) != 0:
            x_val, y_val = np.round(np.mean(stored, axis=0), 2)
        else:
            x_val, y_val = 0, 0

        # make the data ready to draw
        x_offset = 2.5 * window.height / 4.
        y_offset = window.height / 4.
        datax, datay = ana_obj.ready_to_draw(stored, x_scale=10, x_offset=x_offset,
                                             y_scale=10, y_offset=y_offset, dist=dist)

        # draw
        glClear(GL_COLOR_BUFFER_BIT)
        ana_obj.draw(datax, color=(0, 0, 0))
        ana_obj.draw(datay, color=(0, 0, 0))

        x_val_label = pyglet.text.Label(str(x_val), font_size=36,
                                        x=window.width//2, y=x_offset + 80,
                                        anchor_x='center', anchor_y='center',
                                        color=(0, 0, 0, 100))
        y_val_label = pyglet.text.Label(str(y_val), font_size=36,
                                        x=window.width//2, y=y_offset - 40,
                                        anchor_x='center', anchor_y='center',
                                        color=(0, 0, 0, 100))
        x_val_label.draw()
        y_val_label.draw()
        fps_display.draw()

    pyglet.app.run()