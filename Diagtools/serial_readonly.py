import sys
sys.path.append("../Diagtools") # Adds higher directory to python modules path.
from diagnostic import Diagnose
from pyglet.gl import *
from struct import unpack
# from threading import Thread
from collections import deque
import numpy as np
import serial
import time
#
#
# def compTimeDiff(two_times):
#
#     if len(two_times) > 1:
#         time_diff = two_times[1] - two_times[0]
#         freq = 1000 / (time_diff + .001)
#         return round(freq), two_times[1] - two_times[0]
#
#     else:
#         return 0, 0
#
# # set the frequency of data reading - this is in terms of
# def readdata_thread_func(interval=.001): # interval is in second
#
#     global data_buffer
#     data_buffer = deque(maxlen=10) # data buffer - specifies how much data you wanna store (this case latest 10 data)
#     data_read = deque(maxlen=2) # what is coming from arduino(one value for two channels at a time -> so two values)
#
#     # Set the port value
#     ARDUINO_PORT = 'COM9'
#     BAUDRATE = 115200
#     print('Connecting...')
#
#     with serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2.) as device:
#
#         print('Connection Successful.  Emptying Buffer...')
#         print(device.readline())
#         print('Buffer Empty.  Testing Signal...')
#
#         init_time = round(time.time()*1000)  # time in microsecond
#         two_times = deque(maxlen=2)
#
#         while True:
#             time.sleep(interval)
#             data_val = device.readline().strip()
#             data_val = data_val.split(sep=b',')
#
#             curr_time = round(time.time()*1000)
#             time_passed_ms = curr_time - init_time
#             # two_times.append(time_passed_ms)
#             # freq, time_diff = compTimeDiff(two_times)
#
#             # receiving something like [b'105', b'0\r0', b'0']
#
#             print(data_val, len(data_val))
#             if len(data_val) > 2 or len(data_val) < 1:
#                 data_val == [b'0', b'0']
#
#             print(time_passed_ms, tuple(map(int, data_val)), interval)
#
#
#             data_buffer.append(tuple(map(int, data_val)))


if __name__ == '__main__':

    # readdata_thread = Thread(target=readdata_thread_func, daemon=True)
    # readdata_thread.start()

    # create a diagnostic object
    ana_obj = Diagnose(mode='slide')

    window = pyglet.window.Window(1500, 300, resizable=True, vsync=True)
    fps_display = pyglet.window.FPSDisplay(window)

    pyglet.gl.glClearColor(0.9, 0.9, 0.9, 1)  # background color

    dist = 1  # this is the distance between each data point on the graph!
    nsample = 192  # window.width // dist
    storeIt = ana_obj.data_for_display(nsample)

    # Create the update function, for pyglet to run!
    def update(dt):
        pass

    pyglet.clock.schedule(update)


    @window.event
    def on_draw():

        # store data
        packet = device.read(4)
        data_buffer = unpack('<2h', packet)
        next(storeIt)
        stored = storeIt.send(data_buffer)

        # TODO: sometimes one value is only received from serial. It gives and error!

        if len(stored) != 0:
            x_val, y_val = np.round(np.mean(stored, axis=0), 2)
        else:
            x_val, y_val = 0, 0

        # make the data ready to draw
        x_offset = 2.5 * window.height / 4.
        y_offset = window.height / 4.
        datax, datay = ana_obj.ready_to_draw(stored, x_scale=.1, x_offset=x_offset,
                                             y_scale=.1, y_offset=y_offset, dist=dist)

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