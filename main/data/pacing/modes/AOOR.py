import json

from main.data.pacing.PacingMode import PacingMode
from main.constants.PacingModes import to_pacing_mode_id
from main.utils.SerialUtils import flatten_to_26_bytearray


class AOOR(PacingMode):
    NAME = "AOOR"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width, activity_threshold, reaction_time, recovery_time, max_sensor_rate, response_factor):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width,
            activity_threshold=activity_threshold,
            reaction_time=reaction_time,
            recovery_time=recovery_time,
            max_sensor_rate = max_sensor_rate,
            response_factor=response_factor
        )

    def serialize(self) -> bytearray:
        serial_self = self.as_serial
        serial_bytes = [0 for x in range(10)]
        serial_bytes[0] = to_pacing_mode_id(self.NAME)
        serial_bytes[1] = serial_self.lower_rate_limit
        serial_bytes[2] = serial_self.upper_rate_limit
        serial_bytes[3] = serial_self.atrial_amplitude
        serial_bytes[4] = serial_self.atrial_pulse_width
        serial_bytes[5] = serial_self.activity_threshold
        serial_bytes[6] = serial_self.reaction_time
        serial_bytes[7] = serial_self.recovery_time
        serial_bytes[8] = serial_self.max_sensor_rate
        serial_bytes[9] = serial_self.recovery_time
        return flatten_to_26_bytearray(serial_bytes)


class AOORBuilder:
    @staticmethod
    def from_string(string):
        aai_dict = json.loads(string)
        return AOOR(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"], aai_dict["atrial_amplitude"],
                    aai_dict["atrial_pulse_width"], aai_dict["activity_threshold"], aai_dict["reaction_time"], aai_dict["recovery_time"], aai_dict["max_sensor_rate"], aai_dict["response_factor"])

    @staticmethod
    def empty():
        return AOOR(60, 120, 3.5, 1, 3, 30, 5, 120, 8)
