import time
from threading import Thread

from serial import EIGHTBITS

from main.communication.SerialBase import SerialBase
from main.communication.SerialDecorator import serial_safe_methods, leave_serial_open
from main.communication.interfaces.SerialInterface import SerialInterface
from main.data.egm.EGMPoint import EGMPoint
from main.data.pacing.PacingMode import PacingMode
from main.data.pacing.modes.DOOR import DOOR
from main.data.serial.SerialIdentifier import SerialIdentifier


@serial_safe_methods
class SerialCommunicator(SerialBase, SerialInterface):

    def __init__(self, port, baudrate=115200, bytesize=EIGHTBITS):
        super().__init__(port, baudrate, bytesize)
        self.run_serial_decorator = True  # This is neccessary to stop the decorator from going into an infinite loop
        self.device_id = bytes(0)
        self.listen_for_egm = False
        self.egm_thread = None
        self.egm_data = []

    def get_device_ID(self) -> int:
        print(len(self.device_id))
        if len(self.device_id) != 0:
            return int(self.device_id, 16)
        else:
            return 0

    def get_last_device_connected(self) -> str:
        if len(self.device_id) != 0:
            return int(self.device_id, 16)
        else:
            return 0

    def is_pacing_being_saved(self) -> bool:
        return self.listen_for_egm

    def connect_to_pacemaker(self):
        self.send(SerialIdentifier.CONNECT)
        # self.check_response(SerialIdentifier.CONNECT)
        self.device_id = self.await_data()

    def disconnect_from_pacemaker(self):
        self.send(SerialIdentifier.DISCONNECT)

    def send_pacing_data(self, data: PacingMode):
        self.send(SerialIdentifier.SEND_DATA, data.serialize())
        return self.check_response(SerialIdentifier.RECEIVED_DATA)

    def is_connection_established(self):
        self.send(SerialIdentifier.PING)
        return self.await_data()
        # return self.check_response(SerialIdentifier.PING)

    def egm_loop(self):
        while self.listen_for_egm:
            if self.serial.inWaiting() >= 26:
                raw_egm_data = self.serial.read(26)
                time_byte = int(raw_egm_data[:4], 16)
                atrium_byte = int(raw_egm_data[4:8], 16)
                ventricle_byte = int(raw_egm_data[8:12], 16)
                egm_point = EGMPoint(atrium_byte, ventricle_byte, time_byte)
                self.egm_data.append(egm_point)
        time.sleep(.1)

    @leave_serial_open
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
    paceDOOR = DOOR(lower_rate_limit=33,
                    upper_rate_limit=200,
                    atrial_amplitude=3,
                    atrial_pulse_width=3,
                    ventricular_amplitude=4,
                    ventricular_pulse_width=4,
                    activity_threshold=5,
                    reaction_time=20,
                    recovery_time=12,
                    av_delay=225)
    com = SerialCommunicator("COM1")
    com.request_EGM_data()
    time.sleep(30)
    com.end_egm_data()

