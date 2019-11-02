import json

from main.data.PacingMode import PacingMode
from main.data.RateAdjusted import RateAdjustedVentrical


class VVIR(PacingMode, RateAdjustedVentrical):
    NAME = "VVIR"

    def __init__(self, lower_rate_limit, upper_rate_limit, ventricular_amplitude, ventricular_pulse_width, vrp,
                 sensor_rate, ventricular_sensitivity):
        super(PacingMode).__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=None,
            atrial_pulse_width=None,
            ventricular_amplitude=ventricular_amplitude,
            ventricular_pulse_width=ventricular_pulse_width,
            arp=None,
            vrp=vrp)
        super(RateAdjustedVentrical).__init__(
            sensor_rate=sensor_rate,
            av_delay=None,
            ventricular_sensitivity=ventricular_sensitivity)

    def validate(self) -> bool:
        return super(PacingMode).validate() and super(RateAdjustedVentrical).validate()


class VVIRBuilder:
    @staticmethod
    def from_string(string):
        aai_dict = json.loads(string)
        return VVIR(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"], aai_dict["ventricular_amplitude"],
                    aai_dict["ventricular_pulse_width"], aai_dict["vrp"], aai_dict["sensor_rate"],
                    aai_dict["ventricular_sensitivity"])

    @staticmethod
    def empty():
        return VVIR(60, 120, 3.5, 1, 320, 120)
