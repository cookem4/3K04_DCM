from serial import to_bytes

from main.constants.PacingModes import to_pacing_mode_id
from main.data.pacing.PacingModeValidator import PM_LIMIT
from main.constants.SerialIdentifier import SerialIdentifier
from main.utils.SerialUtils import to_serial_byte, flatten_list, replace_nones_with_double_zero


class OutboundSerialPacingMode:

    def __init__(self, pm):
        self.pacing_mode_id = to_pacing_mode_id(pm.NAME)
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

    def as_inbound_data(self):
        out = [SerialIdentifier.SEND_DATA.value, self.pacing_mode_id, self.lower_rate_limit, self.upper_rate_limit,
               self.atrial_amplitude, self.atrial_pulse_width,
               self.ventricular_amplitude,
               self.ventricular_pulse_width, self.arp, self.vrp, self.activity_threshold, self.reaction_time,
               self.recovery_time, self.max_sensor_rate, self.response_factor, self.av_delay, self.atrial_sensitivity,
               self.ventricular_sensitivity]
        out = flatten_list(replace_nones_with_double_zero(out))
        return to_bytes(out)
