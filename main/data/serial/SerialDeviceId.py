from serial import to_bytes


class SerialDeviceId:
    def __init__(self, data: bytearray):
        self.identifier = data[0]
        self.id = data[1:5]

    def get_raw_id(self):
        return self.id

    def get_str_id(self):
        return self.id.hex()

    def get_int_id(self):
        return int(self.get_str_id(), 16)


if __name__ == '__main__':
    data = to_bytes([1, 2, 3, 4, 5] + 29 * [0])
    sdi = SerialDeviceId(data)
    print(sdi.get_int_id())
    print(sdi.get_str_id())
