class Serial():

    def __init__(self, PORT='COM1', baudrate=19200):

        self.port = PORT
        self.baudrate = baudrate


    def write(self, msg):
        return msg

    def read(self, msg):
        pass

    def readline(self, msg):
        pass


if __name__ == "__main__":

    ser = Serial()
    msg = ser.write('Hello')

    print(ser.baudrate)