import json

from data.PacingMode import PacingMode


class AAI(PacingMode):
    NAME = "AAI"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width, arp):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width,
            ventricular_amplitude=None,
            ventricular_pulse_width=None,
            arp=arp,
            vrp=None)

    def validate(self) -> bool:
        return super().validate() and \
               self.atrial_amplitude > 0 and \
               self.atrial_pulse_width > 0 and \
               self.arp > 0


class AAIBuilder:
    @staticmethod
    def from_string(string):
        aai_dict = json.loads(string)
        return AAI(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"], aai_dict["atrial_amplitude"],
                   aai_dict["atrial_pulse_width"], aai_dict["arp"])

    @staticmethod
    def empty():
        return AAI(60, 120, 3.5, 1, 250)
