import json

from main.data.PacingMode import PacingMode


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
            arp=None,
            vrp=vrp,
            sensor_rate=None,
            av_delay=None,
            atrial_sensitivity=None,
            ventricular_sensitivity=None)

    def validate(self) -> bool:
        return super().validate() and \
               self.ventricular_amplitude > 0 and \
               self.ventricular_pulse_width > 0 and \
               self.vrp > 0


class VVIBuilder:
    @staticmethod
    def from_string(string):
        aai_dict = json.loads(string)
        return VVI(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"], aai_dict["ventricular_amplitude"],
                   aai_dict["ventricular_pulse_width"], aai_dict["vrp"])

    @staticmethod
    def empty():
        return VVI(60, 120, 3.5, 1, 320)
