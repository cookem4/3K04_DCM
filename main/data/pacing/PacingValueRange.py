
error_messages = {
    "LRL": "Lower rate limit must be below 40",
    "URL": "Lower rate limit must be above 220",
    "URL_gt_LRL": "Upper rate limit must be greater than lower rate limit",
    "AA": "Atrial Amplitude must be between 0-5",
    "APW": "Atrial pulse width must be between 0-5",
    "VA": "Ventricular Amplitude must be between 0-5",
    "VPW": "Ventricular pulse width must be between 0-5",
    "VRP": "VRP must be between 150-500",
    "ARP": "ARP must be between 150-500",
    "SR": "Sensor rate must be between 50-175",
    "AV": "AV delay must be between 70-300",
    "AS": "Atrial Sensitivity must be between 1-10",
    "VS": "Ventricular Sensitivity must be between 1-10"
}


class PacingValidationResult:
    def __init__(self, success: bool, error: str = ""):
        self.success = success
        self.error = error


class PacingValueRange:

    def __init__(self, pm):
        self.constraints = {
            "LRL": pm.lower_rate_limit >= 40,
            "URL": pm.upper_rate_limit <= 220,
            "URL_gt_LRL": pm.upper_rate_limit > pm.lower_rate_limit,
            "AA": pm.atrial_amplitude is None or 0 < pm.atrial_amplitude <= 5,
            "APW": pm.atrial_pulse_width is None or 0 < pm.atrial_pulse_width <= 5,
            "VA": pm.ventricular_amplitude is None or 0 < pm.ventricular_amplitude <= 5,
            "VPW": pm.ventricular_pulse_width is None or 0 < pm.ventricular_pulse_width <= 5,
            "VRP": pm.vrp is None or 150 <= pm.vrp <= 500,
            "ARP": pm.arp is None or 150 <= pm.arp <= 500,
            "SR": pm.sensor_rate is None or 50 <= pm.sensor_rate <= 175,
            "AV": pm.av_delay is None or 70 <= pm.av_delay <= 300,
            "AS": pm.atrial_sensitivity is None or 1 <= pm.atrial_sensitivity <= 10,
            "VS": pm.ventricular_sensitivity is None or 1 <= pm.ventricular_sensitivity <= 10
        }

    def validate(self):
        for x in self.constraints.keys():
            if not self.constraints[x]:
                return PacingValidationResult(False, error_messages[x])

        return PacingValidationResult(True)
