import json

from main.data.PacingMode import PacingMode
from main.data.RateAdjusted import RateAdjusted


class DOOR(PacingMode, RateAdjusted):
    NAME = "DOOR"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width, ventricular_amplitude,
                 ventricular_pulse_width, sensor_rate, av_delay):
        super(DOOR, self).__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width,
            ventricular_amplitude=ventricular_amplitude,
            ventricular_pulse_width=ventricular_pulse_width,
            arp=None,
            vrp=None)
        super(RateAdjusted).__init__(
            sensor_rate=sensor_rate,
            av_delay=av_delay,
            atrial_sensitivity=None,
            ventricular_sensitivity=None)

    def validate(self) -> bool:
        return super(PacingMode, self).validate() and super(RateAdjusted, self).validate()


class DOORBuilder:
    @staticmethod
    def from_string(string):
        aai_dict = json.loads(string)
        return DOOR(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"], aai_dict["atrial_amplitude"],
                    aai_dict["atrial_pulse_width"], aai_dict["ventricular_amplitude"],
                    aai_dict["ventricular_pulse_width"], aai_dict["sensor_rate"], aai_dict["av_delay"])

    @staticmethod
    def empty():
        return DOOR(60, 120, 3.5, 1, 3.5, 1, 120, 100)
