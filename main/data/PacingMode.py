import json


class PacingMode:
    NAME: str

    def __init__(self, lower_rate_limit: float, upper_rate_limit: float, atrial_amplitude: float,
                 atrial_pulse_width: float, ventricular_amplitude: float,
                 ventricular_pulse_width: float, arp: float, vrp: float, sensor_rate:float, av_delay:float, atrial_sensitivity:float, ventricular_sensitivity:float):
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
        self.ventricular_sensitivity  = ventricular_sensitivity

    def to_string(self):
        return json.dumps(self.__dict__)

    def validate(self) -> bool:
    
        return (self.lower_rate_limit >= 40) and \
               (self.upper_rate_limit <= 220) and \
               (self.upper_rate_limit > self.lower_rate_limit) and \
               (self.atrial_amplitude is None or self.atrial_amplitude > 0 and self.atrial_amplitude <= 5) and \
               (self.atrial_pulse_width is None or self.atrial_pulse_width > 0 and self.atrial_pulse_width <= 5) and \
               (self.ventricular_amplitude is None or self.ventricular_amplitude > 0 and self.ventricular_amplitude <= 5) and \
               (self.ventricular_pulse_width is None or self.ventricular_pulse_width > 0 and self.ventricular_pulse_width <= 5) and \
               (self.vrp is None or self.vrp >= 150 and self.vrp <= 500) and \
               (self.arp is None or self.arp >= 150 and self.arp <= 500) and \
               (self.sensor_rate is None or self.sensor_rate >= 50 and self.sensor_rate <= 175) and \
               (self.av_delay is None or self.av_delay >= 70 and self.av_delay <= 300) and \
               (self.atrial_sensitivity is None or self.atrial_sensitivity >= 1 and self.atrial_sensitivity <= 10) and \
               (self.ventricular_sensitivity is None or self.ventricular_sensitivity >= 1 and self.ventricular_sensitivity <= 10)
