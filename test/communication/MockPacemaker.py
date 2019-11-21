import time
from threading import Thread

from serial import Serial, EIGHTBITS

from main.data.egm.EGMPoint import EGMPoint
from main.data.serial.SerialIdentifier import SerialIdentifier


class MockPacemaker:

    def __init__(self, port):
        self.deviceId = "12345678"
        self.running = False
        self.sending_egm_data = False
        self.pacingMode = None
        self.pm_data = None
        self.a_val = 0
        self.v_val = 0
        self.p_val = 300

        self.serial = Serial(port=port, baudrate=115200, bytesize=EIGHTBITS)
        self.main_thread = Thread(target=self.main_loop)
        self.egm_thread = Thread(target=self.egm_loop)

    def start(self):
        if not self.serial.is_open:
            self.serial.open()
        self.running = True
        self.main_thread.start()

    def stop(self):
        self.running = False
        self.main_thread.join()
        if self.serial is not None and self.serial.is_open:
            self.serial.close()

    def main_loop(self):
        while self.running:
            if self.serial.inWaiting() > 0:
                reading = self.serial.read(1)
                print("Mock Pacemaker Received: " + reading.hex())
                identifier = int.from_bytes(reading, "big")
                if identifier == SerialIdentifier.CONNECT.value:
                    self.connect_response()
                elif identifier == SerialIdentifier.SEND_DATA.value:
                    self.recieve_pacing_mode()
                elif identifier == SerialIdentifier.REQUEST_EGM.value:
                    self.start_sending_egm_data()
                elif identifier == SerialIdentifier.STOP_EGM.value:
                    self.stop_sending_egm_data()
                elif identifier == SerialIdentifier.PING.value:
                    self.ping()
                elif identifier == SerialIdentifier.DISCONNECT.value:
                    self.disconnect()
            time.sleep(.1)

    def egm_loop(self):
        while self.sending_egm_data:
            self.a_val += .1
            self.v_val += .1
            data = EGMPoint(self.a_val % 5, self.v_val % 5, self.p_val).serialize()
            self.serial.write(data)
            time.sleep(self.p_val / 1000)

    def ping(self):
        self.serial.write(bytearray([SerialIdentifier.PING.value]))

    def connect_response(self):
        print("sending id")
        self.serial.write(bytearray([0xff]))
        self.serial.write(bytearray(self.deviceId, "ASCII"))

    def recieve_pacing_mode(self):
        i = 0
        while self.serial.inWaiting() == 0 or i < 30:
            i += 1
            time.sleep(1)
        self.pm_data = self.serial.read(self.serial.inWaiting())
        self.serial.write(bytearray(SerialIdentifier.RECEIVED_DATA.value))

    def disconnect(self):
        self.serial.write(bytearray([SerialIdentifier.DISCONNECT.value]))
        self.stop()

    def start_sending_egm_data(self):
        self.serial.write(bytearray([SerialIdentifier.REQUEST_EGM.value]))
        self.sending_egm_data = True
        self.egm_thread.start()

    def stop_sending_egm_data(self):
        self.sending_egm_data = False
        self.egm_thread.join()


if __name__ == '__main__':
    mock_pacemaker = MockPacemaker("COM1")
    mock_pacemaker.start()
