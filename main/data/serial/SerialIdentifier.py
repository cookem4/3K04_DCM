import enum


class SerialIdentifier(enum.Enum):
    CONNECT = 255
    SEND_DATA = 1
    RECEIVED_DATA = SEND_DATA
    REQUEST_EGM = 2
    STOP_EGM = 3
    PING = 4
    DISCONNECT = 5



