import json

class PacingMode:
    NAME: str

    def __init__(self, lower_rate_limit: float, upper_rate_limit: float, atrial_amplitude: float,
                 atrial_pulse_width: float, ventricular_amplitude: float,
                 ventricular_pulse_width: float, arp: float, vrp: float):
        self.lower_rate_limit = lower_rate_limit
        self.upper_rate_limit = upper_rate_limit
        self.atrial_amplitude = atrial_amplitude
        self.atrial_pulse_width = atrial_pulse_width
        self.ventricular_amplitude = ventricular_amplitude
        self.ventricular_pulse_width = ventricular_pulse_width
        self.arp = arp
        self.vrp = vrp

    def to_string(self):
        return json.dumps(self.__dict__)
