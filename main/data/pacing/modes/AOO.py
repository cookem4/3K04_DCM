import json

from main.data.pacing.PacingMode import PacingMode
from main.data.pacing.PacingModes import toSerial
from main.data.serial.SerialUtils import flatten_to_bytearray


class AOO(PacingMode):
    NAME = "AOO"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width)

    def serialize(self) -> bytearray:
        serial_self = self.as_serial
        serial_bytes = [0 for x in range(5)]
        serial_bytes[0] = toSerial(self.NAME)
        serial_bytes[1] = serial_self.lower_rate_limit
        serial_bytes[2] = serial_self.upper_rate_limit
        serial_bytes[3] = serial_self.atrial_amplitude
        serial_bytes[4] = serial_self.atrial_pulse_width
        return flatten_to_bytearray(serial_bytes)


class AOOBuilder:
    @staticmethod
    def from_string(string):
        pm_dict = json.loads(string)
        return AOO(pm_dict["lower_rate_limit"], pm_dict["upper_rate_limit"], pm_dict["atrial_amplitude"],
                   pm_dict["atrial_pulse_width"])

    @staticmethod
    def empty():
        return AOO(60, 120, 3.5, 1)
