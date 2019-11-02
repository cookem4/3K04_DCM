import json

from main.data.PacingMode import PacingMode
from main.data.RateAdjusted import RateAdjustedAtrial


class AAIR(PacingMode, RateAdjustedAtrial):
    NAME = "AAIR"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width, arp, sensor_rate,
                 atrial_sensitivity):
        super(PacingMode).__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width,
            ventricular_amplitude=None,
            ventricular_pulse_width=None,
            arp=arp,
            vrp=None)
        super(RateAdjustedAtrial).__init__(sensor_rate=sensor_rate, av_delay=None,
                                           atrial_sensitivity=atrial_sensitivity)

    def validate(self) -> bool:
        return super(PacingMode).validate() and super(RateAdjustedAtrial).validate()


class AAIRBuilder:
    @staticmethod
    def from_string(string):
        aai_dict = json.loads(string)
        return AAIR(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"], aai_dict["atrial_amplitude"],
                    aai_dict["atrial_pulse_width"], aai_dict["arp"], aai_dict["sensor_rate"],
                    aai_dict["atrial_sensitivity"])

    @staticmethod
    def empty():
        return AAIR(60, 120, 3.5, 1, 250, 120, 0.75)
