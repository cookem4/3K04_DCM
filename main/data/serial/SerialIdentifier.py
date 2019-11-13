import enum

class SerialIdentifier(enum.Enum):
    CONNECT = bytes([0xFF])
    SEND_DATA = bytes([0x01])
    REQUEST_EGM = bytes([0x02])
    STOP_EGM = bytes([0x03])
    PING = bytes([0x04])
    DISCONNECT = bytes([0x05])