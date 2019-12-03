import json

from main.data.pacing.PacingMode import PacingMode
from main.constants.PacingModes import to_pacing_mode_id
from main.utils.SerialUtils import flatten_to_26_bytearray


class AAI(PacingMode):
    NAME = "AAI"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width, arp, atrial_sensitivity):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width,
            arp=arp,
            atrial_sensitivity=atrial_sensitivity)

    def serialize(self) -> bytearray:
        serial_self = self.as_serial
        serial_bytes = [0 for x in range(7)]
        serial_bytes[0] = to_pacing_mode_id(self.NAME)
        serial_bytes[1] = serial_self.lower_rate_limit
        serial_bytes[2] = serial_self.upper_rate_limit
        serial_bytes[3] = serial_self.atrial_amplitude
        serial_bytes[4] = serial_self.atrial_pulse_width
        serial_bytes[5] = serial_self.arp
        serial_bytes[6] = serial_self.atrial_sensitivity
        return flatten_to_26_bytearray(serial_bytes)


class AAIBuilder:
    @staticmethod
    def from_string(string):
        aai_dict = json.loads(string)
        return AAI(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"], aai_dict["atrial_amplitude"],
                   aai_dict["atrial_pulse_width"], aai_dict["arp"], aai_dict["atrial_sensitivity"])

    @staticmethod
    def empty():
        return AAI(60, 120, 3.5, 1, 250, 5)
