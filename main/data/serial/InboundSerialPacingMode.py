from main.data.pacing.PacingMode import PacingMode
from main.data.serial.SerialUtils import EXPECTED_RETURN_SIZE, double_byte_to_value
from main.exceptions.InvalidSerialPacingModeException import InvalidSerialPacingModeException


class InboundSerialPacingMode:
    def __init__(self, data: bytearray):
        if len(data) != EXPECTED_RETURN_SIZE:
            raise InvalidSerialPacingModeException("Inbound pacing mode arrays must be of length 34")
        else:
            self.identifier = data[0]
            self.pacingMode = data[1]
            self.lower_rate_limit = double_byte_to_value(data[2:4])
            self.upper_rate_limit = double_byte_to_value(data[4:6])
            self.atrial_amplitude = double_byte_to_value(data[6:8])
            self.atrial_pulse_width = double_byte_to_value(data[8:10])
            self.ventricular_amplitude = double_byte_to_value(data[10:12])
            self.ventricular_pulse_width = double_byte_to_value(data[12:14])
            self.arp = double_byte_to_value(data[14:16])
            self.vrp = double_byte_to_value(data[16:18])
            self.activity_threshold = double_byte_to_value(data[18:20])
            self.reaction_time = double_byte_to_value(data[20:22])
            self.recovery_time = double_byte_to_value(data[22:24])
            self.max_sensor_rate = double_byte_to_value(data[24:26])
            self.response_factor = double_byte_to_value(data[26:28])
            self.av_delay = double_byte_to_value(data[28:30])
            self.atrial_sensitivity = double_byte_to_value(data[30:32])
            self.ventricular_sensitivity = double_byte_to_value(data[32:34])

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
