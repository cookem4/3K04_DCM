class RateAdjusted:
    def __init__(self, sensor_rate: float, av_delay: float, atrial_sensitivity: float, ventricular_sensitivity: float):
        self.sensor_rate = sensor_rate
        self.av_delay = av_delay
        self.atrial_sensitivity = atrial_sensitivity
        self.ventricular_sensitivity = ventricular_sensitivity

    def validate(self):
        return (self.sensor_rate is None or 50 <= self.sensor_rate <= 175) and \
               (self.av_delay is None or 70 <= self.av_delay <= 300) and \
               (self.atrial_sensitivity is None or 1 <= self.atrial_sensitivity <= 10) and \
               (
                       self.ventricular_sensitivity is None or 1 <= self.ventricular_sensitivity <= 10)


class RateAdjustedVentrical(RateAdjusted):
    def __init__(self, sensor_rate: float, av_delay: float, ventricular_sensitivity: float):
        super(RateAdjusted, self).__init__(
            sensor_rate=sensor_rate,
            av_delay=av_delay,
            ventricular_sensitivity=ventricular_sensitivity,
            atrial_sensitivity=None
        )


class RateAdjustedAtrial(RateAdjusted):
    def __init__(self, sensor_rate: float, av_delay: float, atrial_sensitivity: float):
        super(RateAdjusted, self).__init__(
            sensor_rate=sensor_rate,
            av_delay=av_delay,
            ventricular_sensitivity=None,
            atrial_sensitivity=atrial_sensitivity
        )
