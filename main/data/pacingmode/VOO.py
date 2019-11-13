import json

from main.data.pacingmode.PacingMode import PacingMode


class VOO(PacingMode):
    NAME = "VOO"

    def __init__(self, lower_rate_limit, upper_rate_limit, ventricular_amplitude, ventricular_pulse_width):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            ventricular_amplitude=ventricular_amplitude,
            ventricular_pulse_width=ventricular_pulse_width)


class VOOBuilder:
    @staticmethod
    def from_string(string):
        pm_dict = json.loads(string)
        return VOO(pm_dict["lower_rate_limit"], pm_dict["upper_rate_limit"], pm_dict["ventricular_amplitude"],
                   pm_dict["ventricular_pulse_width"])

    @staticmethod
    def empty():
        return VOO(60, 120, 3.5, 1)
