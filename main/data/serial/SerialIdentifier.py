import enum


class SerialIdentifier(enum.Enum):
    CONNECT = bytes([255])
    SEND_DATA = bytes([1])
    RECEIVED_DATA = SEND_DATA
    REQUEST_EGM = bytes([2])
    STOP_EGM = bytes([3])
    PING = bytes([4])
    DISCONNECT = bytes([5])



