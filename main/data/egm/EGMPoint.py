from main.data.pacing.PacingValueRange import PM_LIMIT
from main.data.serial.SerialUtils import to_serial_byte, flatten_to_26_bytearray


class EGMPoint:
    string_format = "EGM(A:{0}V, V:{1}V, Period:{2}ms)"

    def __init__(self, atrium, ventricle, period):
        self.atrium = atrium
        self.ventricle = ventricle
        self.period = period

    def __str__(self):
        return self.string_format.format(self.atrium, self.ventricle, self.period)

    def serialize(self):
        serial_atrium = to_serial_byte(self.atrium, PM_LIMIT.ATRIAL_AMPLITUDE["max"])
        serial_ventricle = to_serial_byte(self.ventricle, PM_LIMIT.VENTRICULAR_AMPLITUDE["max"])
        serial_period = to_serial_byte(self.period)
        return flatten_to_26_bytearray([serial_period, serial_atrium, serial_ventricle])


class EGMPointBuilder:

    @staticmethod
    def from_serial(serial_atrium, serial_ventricle, serial_period):
        atrium_voltage = (int(serial_atrium, 16) / int('ff', 16)) * PM_LIMIT.ATRIAL_AMPLITUDE["max"]
        ventricle_voltage = (int(serial_ventricle, 16) / int('ff', 16)) * PM_LIMIT.VENTRICULAR_AMPLITUDE["max"]
        period = int(serial_period, 16)
        return EGMPoint(atrium_voltage, ventricle_voltage, period)
