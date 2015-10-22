import serial


class Comms(object):

    def __init__(self):
        self._serial = serial.Serial()
        self.port = '/dev/ttyUSB0'
        self.baudrate = 115200

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        print "setter of port called:", value
        self._serial.port = value
        self._port = value

    @property
    def baudrate(self):
        return self._baudrate

    @baudrate.setter
    def baudrate(self, value):
        print "setter of baudrate called:", value
        self._serial.baudrate = value
        self._baudrate = value

    def open(self):
        self._serial.open()
        return self._serial.isOpen()

    def close(self):
        self._serial.close()
        return not self._serial.isOpen()

    def write(self, char):
        return self._serial.write(chr(char))

    def read(self):
        if self._serial.inWaiting():
            return self._serial.read()

    def read_line(self):
        if self._serial.inWaiting():
            return self._serial.readline()
