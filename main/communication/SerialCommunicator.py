import time
from datetime import datetime, timedelta

from serial import Serial, SerialException, SerialTimeoutException

from main.data.pacingmode.DOOR import DOOR
from main.data.pacingmode.PacingMode import PacingMode
from main.data.serial.SerialIdentifier import SerialIdentifier


class SerialCommunicator():
    baudrate = 115200

    def __init__(self, port: str):
        self.port = port
        self.ser = Serial(port, SerialCommunicator.baudrate)

    def reinit(self):
        self.ser = Serial(self.port, SerialCommunicator.baudrate)

    def send_pacing_data(self, data: PacingMode):
        self.reinit()
        output = [SerialIdentifier.SEND_DATA.value, data.serialize()]
        try:
            while not self.ser.is_open:
                self.ser.open()
            for x in output:
                self.ser.write(x + b'\r\n')
                time.sleep(1)
                out = ''
                while self.ser.inWaiting() > 0:
                    out += self.ser.read(1)
                if out != '':
                    print(out)

            while self.ser.is_open:
                self.ser.close()
        except (SerialException, SerialTimeoutException) as e:
            self.ser.close()
            print(e)
            print("FUCK")
            pass

    def is_connection_established(self):
        start_time = datetime.now()
        self.ser.open()
        self.ser.write(SerialIdentifier.CONNECT)
        tdata = self.ser.read()
        while datetime.now() - start_time > timedelta(seconds=5):
            if SerialIdentifier.CONNECT in tdata:
                return True
            tdata = self.ser.read()
            time.sleep(1)
            data_left = self.ser.inWaiting()
            tdata += self.ser.read(data_left)

        return False


def test():
    paceDOOR = DOOR(66, 200, 3, 3, 4, 4, 100, 225)
    com: SerialCommunicator = SerialCommunicator("COM12")
    com.send_pacing_data(paceDOOR)


if __name__ == '__main__':
    test()
