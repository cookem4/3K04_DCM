from threading import Thread

from serial import EIGHTBITS

from main.communication.SerialBase import SerialBase
from main.communication.SerialDecorator import serial_safe_methods, serial_ignore
from main.communication.interfaces.SerialInterface import SerialInterface
from main.data.egm.EGMPoint import EGMPoint
from main.data.pacing.PacingMode import PacingMode
from main.data.pacing.modes.DOOR import DOOR
from main.data.serial.SerialIdentifier import SerialIdentifier


@serial_safe_methods
class SerialCommunicator(SerialBase, SerialInterface):

    def __init__(self, port, baudrate=115200, bytesize=EIGHTBITS):
        super().__init__(port, baudrate, bytesize)
        self.device_id = bytes(0)
        self.listen_for_egm = False
        self.egm_thread = None
        self.egm_data = []

    @property
    def run_serial_decorator(self):
        return True

    def get_device_ID(self) -> int:
        return self.device_id

    def get_last_device_connected(self) -> str:
        return self.device_id

    def is_pacing_being_saved(self) -> bool:
        return self.listen_for_egm

    def connect_to_pacemaker(self):
        self.send(SerialIdentifier.CONNECT)
        self.check_response(SerialIdentifier.CONNECT)
        self.device_id = self.await_data(6)

    def disconnect_from_pacemaker(self):
        self.send(SerialIdentifier.DISCONNECT)

    def send_pacing_data(self, data: PacingMode):
        self.send(SerialIdentifier.SEND_DATA, data.serialize())
        return self.check_response(SerialIdentifier.RECEIVED_DATA)

    def is_connection_established(self):
        self.send(SerialIdentifier.PING)
        return self.check_response(SerialIdentifier.PING)

    @serial_ignore
    def egm_loop(self):
        while self.listen_for_egm:
            if self.serial.inWaiting() == 14:
                raw_egm_data = self.serial.read(self.serial.inWaiting())
                atrium_byte = int(raw_egm_data[:2], 16)
                atrium_time_byte = int(raw_egm_data[2:6], 16)
                ventricle_byte = int(raw_egm_data[6:8], 16)
                ventricle_time_byte = int(raw_egm_data[8:12], 16)
                egm_point = EGMPoint(atrium_byte, ventricle_byte, atrium_time_byte, ventricle_time_byte)
                self.egm_data.append(egm_point)

    def request_EGM_data(self):
        self.send(SerialIdentifier.REQUEST_EGM)
        self.listen_for_egm = True
        self.egm_thread = Thread(target=self.egm_loop)
        self.egm_thread.start()

    def end_egm_data(self):
        self.send(SerialIdentifier.STOP_EGM)
        self.listen_for_egm = False
        self.egm_thread.join()

    def get_graphing_data(self) -> list:
        return self.egm_data


if __name__ == '__main__':
    paceDOOR = DOOR(33, 200, 3, 3, 4, 4, 100, 225)
    com = SerialCommunicator("COM1")
    result = com.send_pacing_data(paceDOOR)
    print("woo" if result else "nards")
