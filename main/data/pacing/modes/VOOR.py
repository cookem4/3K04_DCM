import json

from main.data.pacing.PacingMode import PacingMode
from main.data.pacing.PacingModes import toSerial
from main.data.serial.SerialUtils import flatten_to_bytearray


class VOOR(PacingMode):
    NAME = "VOOR"

    def __init__(self, lower_rate_limit, upper_rate_limit, ventricular_amplitude, ventricular_pulse_width, sensor_rate):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            ventricular_amplitude=ventricular_amplitude,
            ventricular_pulse_width=ventricular_pulse_width,
            sensor_rate=sensor_rate)

    def serialize(self) -> bytearray:
        serial_self = self.as_serial
        serial_bytes = [0 for x in range(6)]
        serial_bytes[0] = toSerial(self.NAME)
        serial_bytes[1] = serial_self.lower_rate_limit
        serial_bytes[2] = serial_self.upper_rate_limit
        serial_bytes[3] = serial_self.ventricular_amplitude
        serial_bytes[4] = serial_self.ventricular_pulse_width
        serial_bytes[5] = serial_self.sensor_rate
        return flatten_to_bytearray(serial_bytes)


class VOORBuilder:
    @staticmethod
    def from_string(string):
        pm_dict = json.loads(string)
        return VOOR(pm_dict["lower_rate_limit"], pm_dict["upper_rate_limit"], pm_dict["ventricular_amplitude"],
                    pm_dict["ventricular_pulse_width"], pm_dict["sensor_rate"])

    @staticmethod
    def empty():
        return VOOR(60, 120, 3.5, 1, 120)
