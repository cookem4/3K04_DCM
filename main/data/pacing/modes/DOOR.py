import json

from main.data.pacing.PacingMode import PacingMode
from main.data.pacing.PacingModes import toSerial
from main.data.serial.SerialUtils import flatten_to_bytearray


class DOOR(PacingMode):
    NAME = "DOOR"

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude, atrial_pulse_width, ventricular_amplitude,
                 ventricular_pulse_width, sensor_rate, av_delay):
        super().__init__(
            lower_rate_limit=lower_rate_limit,
            upper_rate_limit=upper_rate_limit,
            atrial_amplitude=atrial_amplitude,
            atrial_pulse_width=atrial_pulse_width,
            ventricular_amplitude=ventricular_amplitude,
            ventricular_pulse_width=ventricular_pulse_width,
            sensor_rate=sensor_rate,
            av_delay=av_delay)

    def serialize(self) -> bytearray:
        serial_self = self.as_serial
        serial_bytes = [0 for x in range(9)]
        serial_bytes[0] = toSerial(self.NAME)
        serial_bytes[1] = serial_self.lower_rate_limit
        serial_bytes[2] = serial_self.upper_rate_limit
        serial_bytes[3] = serial_self.atrial_amplitude
        serial_bytes[4] = serial_self.atrial_pulse_width
        serial_bytes[5] = serial_self.ventricular_amplitude
        serial_bytes[6] = serial_self.ventricular_pulse_width
        serial_bytes[7] = serial_self.sensor_rate
        serial_bytes[8] = serial_self.av_delay
        return flatten_to_bytearray(serial_bytes)


class DOORBuilder:
    @staticmethod
    def from_string(string):
        aai_dict = json.loads(string)
        return DOOR(aai_dict["lower_rate_limit"], aai_dict["upper_rate_limit"], aai_dict["atrial_amplitude"],
                    aai_dict["atrial_pulse_width"], aai_dict["ventricular_amplitude"],
                    aai_dict["ventricular_pulse_width"], aai_dict["sensor_rate"], aai_dict["av_delay"])

    @staticmethod
    def empty():
        return DOOR(60, 120, 3.5, 1, 3.5, 1, 120, 100)
