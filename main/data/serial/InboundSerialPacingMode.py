from main.data.pacing.PacingMode import PacingMode
from main.data.pacing.PacingModeValidator import PM_LIMIT
from main.utils.SerialUtils import double_byte_to_value


class InboundSerialPacingMode:
    def __init__(self, data: bytearray):
        self.identifier = data[0]
        self.pacingMode = data[1]
        self.lower_rate_limit = double_byte_to_value(data[2:4], PM_LIMIT.LOWER_RATE_LIMIT["max"])
        self.upper_rate_limit = double_byte_to_value(data[4:6], PM_LIMIT.UPPER_RATE_LIMIT["max"])
        self.atrial_amplitude = double_byte_to_value(data[6:8], PM_LIMIT.ATRIAL_AMPLITUDE["max"])
        self.atrial_pulse_width = double_byte_to_value(data[8:10], PM_LIMIT.ATRIAL_PULSE_WIDTH["max"])
        self.ventricular_amplitude = double_byte_to_value(data[10:12], PM_LIMIT.VENTRICULAR_AMPLITUDE["max"])
        self.ventricular_pulse_width = double_byte_to_value(data[12:14], PM_LIMIT.VENTRICULAR_PULSE_WIDTH["max"])
        self.arp = double_byte_to_value(data[14:16], PM_LIMIT.ARP["max"])
        self.vrp = double_byte_to_value(data[16:18], PM_LIMIT.VRP["max"])
        self.activity_threshold = double_byte_to_value(data[18:20], PM_LIMIT.ACTIVITY_THRESHOLD["max"])
        self.reaction_time = double_byte_to_value(data[20:22], PM_LIMIT.REACTION_TIME["max"])
        self.recovery_time = double_byte_to_value(data[22:24], PM_LIMIT.RECOVERY_TIME["max"])
        self.max_sensor_rate = double_byte_to_value(data[24:26], PM_LIMIT.MAX_SENSOR_RATE["max"])
        self.response_factor = double_byte_to_value(data[26:28], PM_LIMIT.RESPONSE_FACTOR["max"])
        self.av_delay = double_byte_to_value(data[28:30], PM_LIMIT.AV_DELAY["max"])
        self.atrial_sensitivity = double_byte_to_value(data[30:32], PM_LIMIT.ATRIAL_SENSITIVITY["max"])
        self.ventricular_sensitivity = double_byte_to_value(data[32:34], PM_LIMIT.VENTRICULAR_SENSITIVITY["max"])

    def to_pacing_mode(self):
        return PacingMode(
            lower_rate_limit=self.lower_rate_limit,
            upper_rate_limit=self.upper_rate_limit,
            atrial_amplitude=self.atrial_amplitude,
            atrial_pulse_width=self.atrial_pulse_width,
            ventricular_amplitude=self.ventricular_amplitude,
            ventricular_pulse_width=self.ventricular_pulse_width,
            arp=self.arp,
            vrp=self.vrp,
            activity_threshold=self.activity_threshold,
            reaction_time=self.reaction_time,
            recovery_time=self.recovery_time,
            max_sensor_rate=self.max_sensor_rate,
            response_factor=self.response_factor,
            av_delay=self.av_delay,
            atrial_sensitivity=self.atrial_sensitivity,
            ventricular_sensitivity=self.ventricular_sensitivity)
