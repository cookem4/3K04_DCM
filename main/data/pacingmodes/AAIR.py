import json

from main.data.PacingMode import PacingMode


class AAIR(PacingMode):
    NAME = "AAIR"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width, ventricular_amplitude, ventricular_pulse_width, arp, sensor_rate, atrial_sensitivity):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width,
            ventricular_amplitude=ventricular_amplitude,
            ventricular_pulse_width=ventricular_pulse_width,
            arp=arp,
            vrp=None,
            sensor_rate=sensor_rate,
            av_delay=None,
            atrial_sensitivity=atrial_sensitivity,
            ventricular_sensitivity=None)

    def validate(self) -> bool:
        return super().validate() and \
               self.ventricular_amplitude > 0 and \
               self.ventricular_pulse_width > 0 and \
               self.atrial_amplitude > 0 and \
               self.atrial_pulse_width > 0 and \
               self.arp > 0 and \
               self.sensor_rate > 0 and \
               self.atrial_sensitivity > 0


class AAIRBuilder:
    @staticmethod
    def from_string(string):
        aai_dict = json.loads(string)
        return AAIR(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"],aai_dict["atrial_amplitude"],aai_dict["atrial_pulse_width"], aai_dict["ventricular_amplitude"],
                   aai_dict["ventricular_pulse_width"], aai_dict["arp"], aai_dict["sensor_rate"], aai_dict["atrial_sensitivity"])

    @staticmethod
    def empty():
        return AAIR(60, 120, 3.5,1,3.5, 1, 320, 120, 0.75)
