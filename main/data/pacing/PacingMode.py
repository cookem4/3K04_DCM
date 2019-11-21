import json

from main.data.pacing.PacingValueRange import PacingValueRange
from main.data.serial.OutboundSerialPacingMode import OutboundSerialPacingMode


class PacingMode:
    NAME: str

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude=None,
                 atrial_pulse_width=None, ventricular_amplitude=None,
                 ventricular_pulse_width=None, arp=None, vrp=None, activity_threshold=None, reaction_time=None,
                 recovery_time=None,
                 max_sensor_rate=None, response_factor=None, av_delay=None,
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
        self.activity_threshold = activity_threshold
        self.reaction_time = reaction_time
        self.recovery_time = recovery_time
        self.max_sensor_rate = max_sensor_rate
        self.response_factor = response_factor
        self.av_delay = av_delay
        self.atrial_sensitivity = atrial_sensitivity
        self.ventricular_sensitivity = ventricular_sensitivity

    def to_string(self):
        return json.dumps(self.__dict__)

    @property
    def validation_result(self):
        return PacingValueRange(self).validate()

    @property
    def as_serial(self):
        return OutboundSerialPacingMode(self)
