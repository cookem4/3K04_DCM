import json

from main.data.PacingMode import PacingMode
from main.data.RateAdjusted import RateAdjustedAtrial


class AOOR(PacingMode, RateAdjustedAtrial):
    NAME = "AOOR"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width, sensor_rate):
        super(AOOR, self).__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width,
            ventricular_amplitude=None,
            ventricular_pulse_width=None,
            arp=None,
            vrp=None,
        )
        super(RateAdjustedAtrial, self).__init__(
            sensor_rate=sensor_rate,
            av_delay=None,
            atrial_sensitivity=None,
            ventricular_sensitivity=None
        )

    def validate(self) -> bool:
        return super(PacingMode, self).validate() and super(RateAdjustedAtrial, self).validate()


class AOORBuilder:
    @staticmethod
    def from_string(string):
        aai_dict = json.loads(string)
        return AOOR(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"], aai_dict["atrial_amplitude"],
                    aai_dict["atrial_pulse_width"], aai_dict["sensor_rate"])

    @staticmethod
    def empty():
        return AOOR(60, 120, 3.5, 1, 120)
