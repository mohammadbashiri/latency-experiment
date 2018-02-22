from threading import Thread
import time

def named_verbose_loop(name='A', interval=.1):
    old_time = time.time()
    global i
    while True:
        i += 1
        time.sleep(interval)
        curr_time = time.time()
        actual_interval = curr_time - old_time
        old_time = curr_time
        print(name, interval, actual_interval)

if __name__ == '__main__':

    global i
    i = 0

    thread_a = Thread(target=named_verbose_loop, args=('A', .1), daemon=True)
    thread_a.start()

    thread_b = Thread(target=named_verbose_loop, args=('B', .05), daemon=True)
    thread_b.start()

    while True:

        print(i)
        pass

    # thread_a.join()
    # thread_b.join()

