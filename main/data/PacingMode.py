import json

class PacingMode:
    NAME: str

    def __init__(self, lower_rate_limit, upper_rate_limit, atrial_amplitude,
                 atrial_pulse_width, ventricular_amplitude,
                 ventricular_pulse_width, arp, vrp, sensor_rate, av_delay, atrial_sensitivity,
                 ventricular_sensitivity):
        self.lower_rate_limit = lower_rate_limit
        self.upper_rate_limit = upper_rate_limit
        self.atrial_amplitude = atrial_amplitude
        self.atrial_pulse_width = atrial_pulse_width
        self.ventricular_amplitude = ventricular_amplitude
        self.ventricular_pulse_width = ventricular_pulse_width
        self.arp = arp
        self.vrp = vrp
        self.sensor_rate = sensor_rate
        self.av_delay = av_delay
        self.atrial_sensitivity = atrial_sensitivity
        self.ventricular_sensitivity = ventricular_sensitivity

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
               (self.arp is None or 150 <= self.arp <= 500) and \
                (self.sensor_rate is None or 50 <= self.sensor_rate <= 175) and \
               (self.av_delay is None or 70 <= self.av_delay <= 300) and \
               (self.atrial_sensitivity is None or 1 <= self.atrial_sensitivity <= 10) and \
               (self.ventricular_sensitivity is None or 1 <= self.ventricular_sensitivity <= 10)
