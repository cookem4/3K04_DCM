import json

from main.data.pacing.PacingModeValidator import PacingModeValidator
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
        return PacingModeValidator.form_pacing_mode(self).validate()

    @property
    def as_serial(self):
        return OutboundSerialPacingMode(self)

    def __eq__(self, other):
        validity_array = []
        validity_array[0] = self.lower_rate_limit == other.lower_rate_limit
        validity_array[1] = self.upper_rate_limit == other.upper_rate_limit
        validity_array[2] = value_match(self.atrial_amplitude, other.atrial_amplitude)
        validity_array[3] = value_match(self.atrial_pulse_width, other.atrial_pulse_width)
        validity_array[4] = value_match(self.ventricular_amplitude, other.ventricular_amplitude)
        validity_array[5] = value_match(self.ventricular_pulse_width, other.ventricular_pulse_width)
        validity_array[6] = value_match(self.arp, other.arp)
        validity_array[7] = value_match(self.vrp, other.vrp)
        validity_array[8] = value_match(self.activity_threshold, other.activity_threshold)
        validity_array[9] = value_match(self.reaction_time, other.reaction_time)
        validity_array[10] = value_match(self.recovery_time, other.recovery_time)
        validity_array[11] = value_match(self.max_sensor_rate, other.max_sensor_rate)
        validity_array[12] = value_match(self.response_factor, other.response_factor)
        validity_array[13] = value_match(self.av_delay, other.av_delay)
        validity_array[14] = value_match(self.atrial_sensitivity, other.atrial_sensitivity)
        validity_array[15] = value_match(self.ventricular_sensitivity, other.ventricular_sensitivity)


def value_match(val1, val2):
    if val1 is None and val2 is None:
        return True
    if val1 is None and val2 is not None:
        return False
    if val1 is not None and val2 is None:
        return False
    return val1 == val2
