# from collections import deque
# import serial
# import time
#
# # Set the port value
# ARDUINO_PORT = 'COM9'
# BAUDRATE = 115200
# print('Connecting...')
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
# with serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2.) as device:
#
#     print('Connection Successful.  Emptying Buffer...')
#     print(device.readline())
#     print('Buffer Empty.  Testing Signal...')
#
#     init_time = round(time.time()*1000)  # time in microsecond
#     two_times = deque(maxlen=2)
#
#     while True:
#         data_val = device.readline().strip()
#         data_val = data_val.split(sep=b',')
#
#         curr_time = round(time.time()*1000)
#         time_passed_ms = curr_time - init_time
#         two_times.append(time_passed_ms)
#         freq, time_diff = compTimeDiff(two_times)
#
#         print(time_passed_ms, time_diff, tuple(map(int, data_val)))

from struct import pack, unpack
import serial
import time

# Set the port value
ARDUINO_PORT = 'COM9'
BAUDRATE = 250000
print('Connecting...')

with serial.Serial(ARDUINO_PORT, baudrate=BAUDRATE, timeout=2.) as device:

    print('Connection Successful.  Emptying Buffer...')
    device.flush()
    device.readline()
    device.readline()
    print('Buffer Empty.  Testing Signal...')

    old_time = 0
    packet_len = 7
    buff_len = 4  # 4 * 16  # why these values? seems we read four packets per ms and each frame is being drawn every 16 ms!
    while True:
        data = unpack('>'+'IBBc'*buff_len, device.read(packet_len*buff_len))
        # print(data[0]-old_time, data[0], data[2], data[4], '\n')
        # old_time = data[0]
        print(data)
