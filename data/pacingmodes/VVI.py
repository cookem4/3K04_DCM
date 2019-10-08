from data.PacingMode import PacingMode
import json


class VVI(PacingMode):
    NAME = "VVI"

    def __init__(self, lower_rate_limit, upper_rate_limit, ventricular_amplitude, ventricular_pulse_width, vrp):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=None,
            atrial_pulse_width=None,
            ventricular_amplitude=ventricular_amplitude,
            ventricular_pulse_width=ventricular_pulse_width,
            arp = None,
            vrp = vrp)


class VVIBuilder:
    @staticmethod
    def from_string(string):
        aai_dict = json.loads(string)
        return VVI(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"], aai_dict["ventricular_amplitude"],
                   aai_dict["ventricular_pulse_width"], aai_dict["vrp"])

    @staticmethod
    def empty():
        return VVI(0, 0, 0, 0)
