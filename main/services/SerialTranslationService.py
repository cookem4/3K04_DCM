from datetime import datetime

from main.data.serial.InboundSerialPacingMode import InboundSerialPacingMode
from main.data.serial.SerialDeviceId import SerialDeviceId
from main.data.serial.SerialEGMPoint import SerialEGMPoint
from main.constants.SerialIdentifier import SerialIdentifier
from main.utils.SerialUtils import EXPECTED_RETURN_SIZE
from main.exceptions.InvalidSerialPacingModeException import InvalidSerialPacingModeException


class SerialPing:
    def __init__(self):
        self.ping_time = datetime.now()


class SerialTranslationService:
    last_data_type: SerialIdentifier

    @staticmethod
    def from_data(data: bytearray):
        if len(data) != EXPECTED_RETURN_SIZE:
            raise InvalidSerialPacingModeException("Inbound pacing mode arrays must be of length 34")
        else:
            identifier = data[0]
            if identifier == SerialIdentifier.SEND_DATA.value:
                SerialTranslationService.last_data_type = SerialIdentifier.SEND_DATA
                return True
            elif identifier == SerialIdentifier.CONNECT.value:
                SerialTranslationService.last_data_type = SerialIdentifier.CONNECT
                return SerialDeviceId(data)
            elif identifier == SerialIdentifier.PING.value:
                SerialTranslationService.last_data_type = SerialIdentifier.PING
                return SerialPing()
            elif identifier == SerialIdentifier.REQUEST_EGM.value:
                SerialTranslationService.last_data_type = SerialIdentifier.REQUEST_EGM
                return SerialEGMPoint(data)
