import re
import time
from datetime import timedelta, datetime

from serial import EIGHTBITS, Serial, to_bytes

from main.data.serial.SerialIdentifier import SerialIdentifier


class SerialBase:
    RESPONSE_TIME_LIMIT = 10  # seconds
    TIMEOUT = 5  # minutes

    def __init__(self, port, baudrate=115200, bytesize=EIGHTBITS):
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.serial: Serial = None
        self.time_since_last_call = datetime.now()

    def open(self):
        if self.serial is None:
            self.serial = Serial(
                port=self.port,
                baudrate=self.baudrate,
                write_timeout=0,
                bytesize=self.bytesize)
        elif not self.serial.is_open:
            self.serial.open()

    def close(self):
        if self.serial is not None and self.serial.is_open:
            self.serial.close()

    def send(self, identifier: SerialIdentifier, data_bytearray: bytearray = bytearray(0)):
        bytes_to_send = to_bytes(bytes([identifier.value]) + data_bytearray)
        self.serial.write(bytes_to_send)

    def check_timeout(self):
        if self.time_since_last_call - datetime.now() > timedelta(minutes=SerialBase.TIMEOUT):
            return False
        else:
            return True

    def await_data(self, response_size):
        for i in range(SerialBase.RESPONSE_TIME_LIMIT):
            if self.serial.inWaiting() >= response_size:
                out = self.serial.read(self.serial.inWaiting()).decode()
                out = re.sub('\r\n', '', out)
                if len(out) == response_size:
                    return out
            time.sleep(1)
        return []

    def check_response(self, expected_response: SerialIdentifier):
        for i in range(SerialBase.RESPONSE_TIME_LIMIT):
            if self.serial.inWaiting() >= 2:
                reading = self.serial.read(2)
                identifier = int(reading,16)
                if identifier == expected_response.value:
                    return True
            time.sleep(1)
        return False
