from math import floor

from serial import SerialException

EXPECTED_RETURN_SIZE = 4  # bytes
EXPECTED_SEND_SIZE = 26


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


def single_byte_to_value(byte, max_value=255):
    byte_val = int(byte, 16)
    return round(max_value * byte_val / 255, 2)


def flatten_to_26_bytearray(list_of_lists) -> bytearray:
    flat_list = flatten_list(list_of_lists)
    length = len(flat_list)
    flat_list += [0] * (25 - length)
    return bytearray(flat_list)


def flatten_list(list_of_lists) -> list:
    flat_list = []
    for sublist in list_of_lists:
        if type(sublist) is not list:
            flat_list.append(sublist)
        else:
            for item in sublist:
                flat_list.append(item)
    return flat_list


def replace_nones_with_double_zero(alist: list):
    return [(x if x is not None else [0, 0]) for x in alist]
