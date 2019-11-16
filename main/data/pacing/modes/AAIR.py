import json

from main.data.pacing.PacingMode import PacingMode
from main.data.pacing.PacingModes import toSerial
from main.data.serial.SerialUtils import flatten_to_bytearray


class AAIR(PacingMode):
    NAME = "AAIR"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width, arp, activity_threshold, reaction_time, recovery_time,
                 atrial_sensitivity):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width,
            arp=arp,
            activity_threshold=activity_threshold,
            reaction_time = reaction_time,
            recovery_time = reacovery_time,
            atrial_sensitivity=atrial_sensitivity)

    def serialize(self) -> bytearray:
        serial_self = self.as_serial
        serial_bytes = [0 for x in range(10)]
        serial_bytes[0] = toSerial(self.NAME)
        serial_bytes[1] = serial_self.lower_rate_limit
        serial_bytes[2] = serial_self.upper_rate_limit
        serial_bytes[3] = serial_self.atrial_amplitude
        serial_bytes[4] = serial_self.atrial_pulse_width
        serial_bytes[5] = serial_self.arp
        serial_bytes[6] = serial_self.activity_threshold
        serial_bytes[7] = serial_self.reaction_time
        serial_bytes[8] = serial_self.reacovery_time
        serial_bytes[9] = serial_self.atrial_sensitivity
        return flatten_to_bytearray(serial_bytes)


class AAIRBuilder:
    @staticmethod
    def from_string(string):
        aai_dict = json.loads(string)
        return AAIR(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"], aai_dict["atrial_amplitude"],
                    aai_dict["atrial_pulse_width"], aai_dict["arp"], aai_dict["activity_threshold"], aai_dict["reaction_time"], aai_dict["recovery_time"],
                    aai_dict["atrial_sensitivity"])

    @staticmethod
    def empty():
        return AAIR(60, 120, 3.5, 1, 250, 3, 30, 5, 0.75)
