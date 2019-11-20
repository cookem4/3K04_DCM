from math import floor

from serial import SerialException


def to_serial_byte(val, max_value=65535):
    if val is None:
        return None
    if val > max_value:
        raise SerialException("to_serial_byte: val {0} must be less than max {1}".format(val, max_value))
    int_val = round(val * 65535 / max_value)
    msb = floor(int_val / 256)
    lsb = int_val % 256
    return [msb, lsb]


def double_byte_to_value(double_byte: list, max_value=65535):
    int_val = 256 * double_byte[0] + double_byte[1]
    return round(max_value * int_val / 65535, 2)


def flatten_to_26_bytearray(list_of_lists) -> bytearray:
    flat_list = []
    for sublist in list_of_lists:
        if type(sublist) is not list:
            flat_list.append(sublist)
        else:
            for item in sublist:
                flat_list.append(item)
    length = len(flat_list)
    flat_list += [0]*(25-length)
    return bytearray(flat_list)
