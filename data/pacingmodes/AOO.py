from data.PacingMode import PacingMode
import json


class AOO(PacingMode):
    NAME = "AOO"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width,
            ventricular_amplitude=None,
            ventricular_pulse_width=None)


class AOOBuilder:
    def from_string(self, string):
        pm_dict = json.loads(string)
        return AOO(pm_dict["lower_rate_limit"], pm_dict["upper_rate_limit"], pm_dict["atrial_amplitude"],
                   pm_dict["atrial_pulse_width"])
