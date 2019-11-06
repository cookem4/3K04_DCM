import json

from main.data.PacingMode import PacingMode


class VOOR(PacingMode):
    NAME = "VOOR"

    def __init__(self, lower_rate_limit, upper_rate_limit, ventricular_amplitude, ventricular_pulse_width, sensor_rate):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=None,
            atrial_pulse_width=None,
            ventricular_amplitude=ventricular_amplitude,
            ventricular_pulse_width=ventricular_pulse_width,
            arp=None,
            vrp=None,
            sensor_rate=sensor_rate,
            av_delay=None,
            atrial_sensitivity=None,
            ventricular_sensitivity=None)


class VOORBuilder:
    @staticmethod
    def from_string(string):
        pm_dict = json.loads(string)
        return VOOR(pm_dict["lower_rate_limit"], pm_dict["upper_rate_limit"], pm_dict["ventricular_amplitude"],
                    pm_dict["ventricular_pulse_width"], pm_dict["sensor_rate"])

    @staticmethod
    def empty():
        return VOOR(60, 120, 3.5, 1, 120)
