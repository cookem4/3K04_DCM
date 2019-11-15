import json

from main.data.pacing.PacingValueRange import PacingValueRange
from main.data.serial.SerialPacingFormat import SerialPacingFormat


class PacingMode:
    NAME: str

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude=None,
                 atrial_pulse_width=None, ventricular_amplitude=None,
                 ventricular_pulse_width=None, arp=None, vrp=None, sensor_rate=None, av_delay=None,
                 atrial_sensitivity=None,
                 ventricular_sensitivity=None):
        self.lower_rate_limit = lower_rate_limit
        self.upper_rate_limit = upper_rate_limit
        self.atrial_amplitude = atrial_amplitude
        self.atrial_pulse_width = atrial_pulse_width
        self.ventricular_amplitude = ventricular_amplitude
        self.ventricular_pulse_width = ventricular_pulse_width
        self.arp = arp
        self.vrp = vrp
        self.sensor_rate = sensor_rate
        self.av_delay = av_delay
        self.atrial_sensitivity = atrial_sensitivity
        self.ventricular_sensitivity = ventricular_sensitivity


    def to_string(self):
        return json.dumps(self.__dict__)

    def serialize(self) -> bytearray:
        return SerialPacingFormat(self).getBytes()

    @property
    def validation_result(self):
        return PacingValueRange(self).validate()
