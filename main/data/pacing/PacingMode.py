import abc
import json

from main.data.pacing.PacingValueRange import PacingValueRange, PM_LIMIT
from main.data.serial.SerialUtils import to_serial_byte


class PacingMode():
    NAME: str

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude=None,
                 atrial_pulse_width=None, ventricular_amplitude=None,
                 ventricular_pulse_width=None, arp=None, vrp=None, activity_threshold=None, reaction_time=None, recovery_time=None,
                max_sensor_rate = None, response_factor = None, av_delay=None,
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
        self.activity_threshold=activity_threshold
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
        return SerialPacingMode(self)


class SerialPacingMode:

    def __init__(self, pm: PacingMode):
        self.lower_rate_limit = to_serial_byte(
            val=pm.lower_rate_limit,
            max_value=PM_LIMIT.LOWER_RATE_LIMIT["max"])
        self.upper_rate_limit = to_serial_byte(
            val=pm.upper_rate_limit,
            max_value=PM_LIMIT.UPPER_RATE_LIMIT["max"])
        self.atrial_amplitude = to_serial_byte(
            val=pm.atrial_amplitude,
            max_value=PM_LIMIT.ATRIAL_AMPLITUDE["max"])
        self.atrial_pulse_width = to_serial_byte(
            val=pm.atrial_pulse_width,
            max_value=PM_LIMIT.ATRIAL_PULSE_WIDTH["max"])
        self.ventricular_amplitude = to_serial_byte(
            val=pm.ventricular_amplitude,
            max_value=PM_LIMIT.VENTRICULAR_AMPLITUDE["max"])
        self.ventricular_pulse_width = to_serial_byte(
            val=pm.ventricular_pulse_width,
            max_value=PM_LIMIT.VENTRICULAR_PULSE_WIDTH["max"])
        self.arp = to_serial_byte(
            val=pm.arp,
            max_value=PM_LIMIT.ARP["max"])
        self.vrp = to_serial_byte(
            val=pm.vrp,
            max_value=PM_LIMIT.VRP["max"])
        self.activity_threshold = to_serial_byte(
            val=pm.activity_threshold,
            max_value=PM_LIMIT.ACTIVITY_THRESHOLD["max"])
        self.reaction_time = to_serial_byte(
            val=pm.reaction_time,
            max_value=PM_LIMIT.REACTION_TIME["max"])
        self.recovery_time = to_serial_byte(
            val=pm.recovery_time,
            max_value=PM_LIMIT.RECOVERY_TIME["max"])
        self.max_sensor_rate = to_serial_byte(
            val=pm.max_sensor_rate,
            max_value=PM_LIMIT.MAX_SENSOR_RATE["max"])
        self.response_factor = to_serial_byte(
            val=pm.response_factor,
            max_value=PM_LIMIT.RESPONSE_FACTOR["max"])
        self.av_delay = to_serial_byte(
            val=pm.av_delay,
            max_value=PM_LIMIT.AV_DELAY["max"])
        self.atrial_sensitivity = to_serial_byte(
            val=pm.atrial_sensitivity,
            max_value=PM_LIMIT.ATRIAL_SENSITIVITY["max"])
        self.ventricular_sensitivity = to_serial_byte(
            val=pm.ventricular_sensitivity,
            max_value=PM_LIMIT.VENTRICULAR_SENSITIVITY["max"])
