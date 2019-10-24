import json

from ..PacingMode import PacingMode


class AOO(PacingMode):
    NAME = "AOO"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width,
            ventricular_amplitude=None,
            ventricular_pulse_width=None,
            arp=None,
            vrp=None)

    def validate(self) -> bool:
        return super().validate() and \
               self.atrial_amplitude > 0 and \
               self.atrial_pulse_width > 0

class AOOBuilder:
    @staticmethod
    def from_string(string):
        pm_dict = json.loads(string)
        return AOO(pm_dict["lower_rate_limit"], pm_dict["upper_rate_limit"], pm_dict["atrial_amplitude"],
                   pm_dict["atrial_pulse_width"])

    @staticmethod
    def empty():
        return AOO(60, 120, 3.5, 1)