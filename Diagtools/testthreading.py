from threading import Thread
import time

def named_verbose_loop(name='A', interval=.1):
    old_time = time.time()
    while True:
        time.sleep(interval)
        curr_time = time.time()
        actual_interval = curr_time - old_time
        old_time = curr_time
        print(name, interval, actual_interval)


if __name__ == '__main__':
    thread_a = Thread(target=named_verbose_loop, args=('A', .1), daemon=True)
    thread_a.start()

    thread_b = Thread(target=named_verbose_loop, args=('B', .05), daemon=True)
    thread_b.start()

    while True:
        pass

    # thread_a.join()
    # thread_b.join()

