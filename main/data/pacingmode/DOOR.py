import json

from main.data.pacingmode.PacingMode import PacingMode


class DOOR(PacingMode):
    NAME = "DOOR"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width, ventricular_amplitude,
                 ventricular_pulse_width, sensor_rate, av_delay):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width,
            ventricular_amplitude=ventricular_amplitude,
            ventricular_pulse_width=ventricular_pulse_width,
            sensor_rate=sensor_rate,
            av_delay=av_delay)


class DOORBuilder:
    @staticmethod
    def from_string(string):
        aai_dict = json.loads(string)
        return DOOR(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"], aai_dict["atrial_amplitude"],
                    aai_dict["atrial_pulse_width"], aai_dict["ventricular_amplitude"],
                    aai_dict["ventricular_pulse_width"], aai_dict["sensor_rate"], aai_dict["av_delay"])

    @staticmethod
    def empty():
        return DOOR(60, 120, 3.5, 1, 3.5, 1, 120, 100)
