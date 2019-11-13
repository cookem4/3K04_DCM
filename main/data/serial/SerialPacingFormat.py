from main.data.pacingmode.PacingModes import toSerial


def to_single_byte(val):
    if val is None:
        return 0xFF
    else:
        return val


def to_double_byte(val):
    if val is None:
        output = ["ff", "ff"]
    else:
        hex_val = hex(val)[2:]
        if len(hex_val) == 2:
            output = ['0', hex_val]
        elif len(hex_val) == 3:
            output = ['0' + hex_val[0], hex_val[1:]]
        elif len(hex_val) == 4:
            output = [hex_val[0:2], hex_val[2:]]
        else:
            raise IndexError("Value %d must be less than 65535")

    return [int(x, 16) for x in output]


class SerialPacingFormat():

    def __init__(self, pm):
        self.bytes = [0 for x in range(16)]
        self.bytes[0] = toSerial(pm.NAME)
        self.bytes[1] = to_single_byte(pm.lower_rate_limit)
        self.bytes[2] = to_single_byte(pm.upper_rate_limit)
        self.bytes[3] = to_single_byte(pm.atrial_amplitude)
        self.bytes[4] = to_single_byte(pm.atrial_pulse_width)
        self.bytes[5] = to_single_byte(pm.ventricular_amplitude)
        self.bytes[6] = to_single_byte(pm.ventricular_pulse_width)
        vrp = to_double_byte(pm.vrp)
        self.bytes[7] = vrp[0]
        self.bytes[8] = vrp[1]
        arp = to_double_byte(pm.arp)
        self.bytes[9] = arp[0]
        self.bytes[10] = arp[1]
        self.bytes[11] = to_single_byte(pm.sensor_rate)
        av_delay = to_double_byte(pm.av_delay)
        self.bytes[12] = av_delay[0]
        self.bytes[13] = av_delay[1]
        self.bytes[14] = to_single_byte(pm.atrial_sensitivity)
        self.bytes[15] = to_single_byte(pm.ventricular_sensitivity)

    def getBytes(self)->bytearray:
        return bytearray(self.bytes)
