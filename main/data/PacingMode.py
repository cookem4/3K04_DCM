import json

from main.data.RateAdjusted import RateAdjusted


class PacingMode:
    NAME: str

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude,
                 atrial_pulse_width, ventricular_amplitude,
                 ventricular_pulse_width, arp, vrp):
        self.lower_rate_limit = lower_rate_limit
        self.upper_rate_limit = upper_rate_limit
        self.atrial_amplitude = atrial_amplitude
        self.atrial_pulse_width = atrial_pulse_width
        self.ventricular_amplitude = ventricular_amplitude
        self.ventricular_pulse_width = ventricular_pulse_width
        self.arp = arp
        self.vrp = vrp

    def add_rate_adjustment(self, rate_adjustment: RateAdjusted):
        self.__dict__.update(rate_adjustment.__dict__);

    def to_string(self):
        return json.dumps(self.__dict__)

    def validate(self) -> bool:
        return (self.lower_rate_limit >= 40) and \
               (self.upper_rate_limit <= 220) and \
               (self.upper_rate_limit > self.lower_rate_limit) and \
               (self.atrial_amplitude is None or 0 < self.atrial_amplitude <= 5) and \
               (self.atrial_pulse_width is None or 0 < self.atrial_pulse_width <= 5) and \
               (self.ventricular_amplitude is None or 0 < self.ventricular_amplitude <= 5) and \
               (self.ventricular_pulse_width is None or 0 < self.ventricular_pulse_width <= 5) and \
               (self.vrp is None or 150 <= self.vrp <= 500) and \
               (self.arp is None or 150 <= self.arp <= 500)
