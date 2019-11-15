from math import floor


def to_serial_byte(val, max_value):
    if val is None:
        return None
    int_val = round(val * 65535 / max_value)
    msb = floor(int_val / 256)
    lsb = int_val % 256
    return [msb, lsb]


def double_byte_to_value(double_byte: list, max_value):
    int_val = 256 * double_byte[0] + double_byte[1]
    return max_value * int_val / 65535


def flatten_to_bytearray(list_of_lists) -> bytearray:
    flat_list = []
    for sublist in list_of_lists:
        if type(sublist) is not list:
            flat_list.append(sublist)
        else:
            for item in sublist:
                flat_list.append(item)

    return bytearray(flat_list)
