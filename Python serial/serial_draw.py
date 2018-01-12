import sys
sys.path.append("../Diagtools") # Adds higher directory to python modules path.
from diagnostic import Diagnose
from collections import deque
from pyglet.gl import *
from threading import Thread
import serial
import time

ARDUINO_PORT = 'COM9'

# ///////////////////////////////////////////// FOR DRAWING ///////////////////////////////////////////////
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
# ///////////////////////////////////////////// FOR DRAWING ///////////////////////////////////////////////

print('Connecting...')
with serial.Serial(ARDUINO_PORT, timeout=2.) as device:
	print('Connection Successful.  Emptying Buffer...')
	print(device.readlines())
	print('Buffer Empty.  Testing Signal...')

	# Ping Test
	device.write(b'D')
	msg = device.readline()
	print(msg)
	if not 'Confirmation' in msg:
		raise ValueError("word 'Confirmation' not in message.  Ping test not successful.")
	else:
		print('Signaling Successful!')


	# read sensor value
	val_read = deque(maxlen=2)
	val_buffer = deque(maxlen=1)

	@window.event
	def on_draw(): # DOES THE SAME JOB AS WHILE TRUE

		# DOES THE SAME JOB AS gen_data()
		for sensor in (b'A', b'B'):
			device.write(sensor)
			data_val = device.readline().strip()
			# change data from string to float
			val_read.append(float(data_val))
			# time.sleep(.05)

		val_buffer.append(tuple(val_read))
		print(val_buffer)

		# store data
		next(storeIt)
		stored = storeIt.send(val_buffer)

		# make the data ready to draw
		# make the data ready to draw
		x_offset = 3 * window.height / 4.
		y_offset = window.height / 4.
		datax, datay = ana_obj.ready_to_draw(stored, x_scale=10, x_offset=x_offset,
											 y_scale=10, y_offset=y_offset, dist=dist)

		# draw
		glClear(GL_COLOR_BUFFER_BIT)
		ana_obj.draw(datax, color=(0, 255, 0))
		ana_obj.draw(datay, color=(255, 0, 0))

	pyglet.app.run()