import json

from main.data.pacingmode.PacingMode import PacingMode


class AOOR(PacingMode):
    NAME = "AOOR"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width, sensor_rate):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width,
            sensor_rate=sensor_rate,
        )


class AOORBuilder:
    @staticmethod
    def from_string(string):
        aai_dict = json.loads(string)
        return AOOR(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"], aai_dict["atrial_amplitude"],
                    aai_dict["atrial_pulse_width"], aai_dict["sensor_rate"])

    @staticmethod
    def empty():
        return AOOR(60, 120, 3.5, 1, 120)