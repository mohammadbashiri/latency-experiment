from collections import deque
import serial
import time

# Set the port value
ARDUINO_PORT = 'COM9'
BAUDRATE = 115200
print('Connecting...')


def compTimeDiff(two_times):

    if len(two_times) > 1:
        time_diff = two_times[1] - two_times[0]
        freq = 1000 / (time_diff + .001)
        return round(freq), two_times[1] - two_times[0]

    else:
        return 0, 0

with serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2.) as device:

    print('Connection Successful.  Emptying Buffer...')
    # print(device.read())
    # print('Buffer Empty.  Testing Signal...')

    init_time = round(time.time()*1000)  # time in microsecond
    two_times = deque(maxlen=2)

    while True:

        data_val = device.readline().strip()
        # data_val = data_val.split(sep=b',')
        curr_time = round(time.time()*1000)
        time_passed_ms = curr_time - init_time
        two_times.append(time_passed_ms)
        freq, time_diff = compTimeDiff(two_times)

        print(time_passed_ms, time_diff, data_val)  # tuple(map(int, data_val))


        # empty buffer
        # data_val = device.flush()
