from data.PacingMode import PacingMode
import json


class AAI(PacingMode):
    NAME = "AAI"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width,
            ventricular_amplitude=None,
            ventricular_pulse_width=None)


class AAIBuilder:
    def from_string(self, string):
        aai_dict = json.loads(string)
        return AAI(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"], aai_dict["atrial_amplitude"],
                   aai_dict["atrial_pulse_width"])