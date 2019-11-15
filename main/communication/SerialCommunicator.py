import time
from datetime import datetime, timedelta

from serial import SerialTimeoutException, SerialException, EIGHTBITS, Serial, to_bytes

from main.data.pacing.modes.DOOR import DOOR
from main.data.pacing.PacingMode import PacingMode
from main.data.serial.SerialIdentifier import SerialIdentifier

RESPONSE_TIME_LIMIT = 15  # seconds
TIMEOUT = 5  # minutes

serial = None
port: str = "COM1"
baudrate = 115200
time_since_last_usage = 0


def set_port(new_port: str):
    global port
    port = new_port


def serial_safe(serial_using_function):
    def new_function(*args, **kwargs):
        global time_since_last_usage
        time_since_last_usage = datetime.now()
        output = None
        try:
            open_serial()
            output = serial_using_function(*args, **kwargs)
            close_serial()
        except (SerialException, SerialTimeoutException, Exception) as e:
            close_serial()
            print(e)
        return output

    return new_function


def open_serial():
    global serial
    if serial is None:
        serial = Serial(
            port=port,
            baudrate=baudrate,
            write_timeout=0,
            bytesize=EIGHTBITS)
    else:
        if not serial.is_open:
            serial.open()


def close_serial():
    global serial
    if serial is not None and serial.is_open:
        serial.close()


def check_response(expected_response: SerialIdentifier):
    for i in range(RESPONSE_TIME_LIMIT):
        out = serial.read(2)
        if out != '':
            print(out)
        if int(out) == int(expected_response.value.hex()):
            return True
        time.sleep(1)
    return False


def await_data(response_size):
    for i in range(RESPONSE_TIME_LIMIT):
        out = serial.read(response_size)
        if len(out) == response_size:
            return out
    return []


def send(identifier: SerialIdentifier, data_bytearray: bytearray = bytearray(0)):
    bytes_to_send = to_bytes(identifier.value + data_bytearray)
    serial.write(bytes_to_send)


class SerialCommunicator:

    def __init__(self, com_port: str):
        set_port(com_port)

    @serial_safe
    def connect_to_pacemaker(self):
        send(SerialIdentifier.CONNECT)
        check_response(SerialIdentifier.CONNECT)
        id = await_data(6)
        print(id)

    @serial_safe
    def send_pacing_data(self, data: PacingMode):
        send(SerialIdentifier.SEND_DATA, data.serialize())
        return check_response(SerialIdentifier.RECEIVED_DATA)

    @serial_safe
    def is_connection_established(self):
        send(SerialIdentifier.PING)
        return check_response(SerialIdentifier.PING)

    def check_timeout(self):
        global time_since_last_usage
        if time_since_last_usage - datetime.now() > timedelta(minutes=TIMEOUT):
            return False
        else:
            return True


def test():
    paceDOOR = DOOR(66, 200, 3, 3, 4, 4, 100, 225)
    com: SerialCommunicator = SerialCommunicator("COM1")
    com.connect_to_pacemaker()


if __name__ == '__main__':
    test()
