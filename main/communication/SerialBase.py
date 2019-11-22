import time
from datetime import timedelta, datetime

from serial import EIGHTBITS, Serial, to_bytes

from main.constants.SerialIdentifier import SerialIdentifier
from main.utils.SerialUtils import EXPECTED_RETURN_SIZE
from main.services.SerialTranslationService import SerialTranslationService as SerialTranslator


class SerialBase:
    RESPONSE_TIME_LIMIT = 10  # seconds
    TIMEOUT = 5  # minutes

    def __init__(self, port, baudrate=115200, bytesize=EIGHTBITS):
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.serial: Serial = None
        self.time_since_last_call = datetime.now()
        self.most_recent_data = None

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
        numToPad = 26 - 1 - len(data_bytearray)
        bytes_to_send = to_bytes(bytes([identifier.value]) + data_bytearray + bytearray([0] * numToPad))
        self.serial.write(bytes_to_send)

    def check_timeout(self):
        if self.time_since_last_call - datetime.now() > timedelta(minutes=SerialBase.TIMEOUT):
            return False
        else:
            return True

    def await_data(self):
        for i in range(SerialBase.RESPONSE_TIME_LIMIT):
            if self.serial.inWaiting() == EXPECTED_RETURN_SIZE:
                data = SerialTranslator.from_data(self.serial.read(EXPECTED_RETURN_SIZE))
                self.most_recent_data = data
                self.serial.flushInput()
                break
            time.sleep(1)
