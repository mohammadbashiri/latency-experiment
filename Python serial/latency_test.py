import itertools
import serial
import time

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
	if not 'Confirmation' in msg:
		raise ValueError("word 'Confirmation' not in message.  Ping test not successful.")
	else:
		print('Signaling Successful!')
		

	# read sensor value
	val = {}
	while True:
		for sensor in (b'A', b'B'):
			device.write(sensor)
			val[sensor] = device.readline().strip()
			time.sleep(.05)
		print(val)
		time.sleep(.2)
		