import json

from main.data.pacing.PacingMode import PacingMode


class DOO(PacingMode):
    NAME = "DOO"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width, ventricular_amplitude,
                 ventricular_pulse_width, av_delay):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width,
            ventricular_amplitude=ventricular_amplitude,
            ventricular_pulse_width=ventricular_pulse_width)


class DOOBuilder:
    @staticmethod
    def from_string(string):
        aai_dict = json.loads(string)
        return DOO(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"], aai_dict["atrial_amplitude"],
                   aai_dict["atrial_pulse_width"], aai_dict["ventricular_amplitude"],
                   aai_dict["ventricular_pulse_width"], aai_dict["av_delay"])

    @staticmethod
    def empty():
        return DOO(60, 120, 3.5, 1, 3.5, 1, 100)