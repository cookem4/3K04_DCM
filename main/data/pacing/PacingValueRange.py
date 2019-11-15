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


class PM_LIMIT:
    LOWER_RATE_LIMIT = {"min": 0, "max": 40}
    UPPER_RATE_LIMIT = {"min": 0, "max": 220}
    ATRIAL_AMPLITUDE = {"min": 0, "max": 5}
    ATRIAL_PULSE_WIDTH = {"min": 0, "max": 5}
    VENTRICULAR_AMPLITUDE = {"min": 0, "max": 5}
    VENTRICULAR_PULSE_WIDTH = {"min": 0, "max": 5}
    VRP = {"min": 150, "max": 500}
    ARP = {"min": 150, "max": 500}
    SENSOR_RATE = {"min": 50, "max": 175}
    AV_DELAY = {"min": 70, "max": 300}
    ATRIAL_SENSITIVITY = {"min": 1, "max": 10}
    VENTRICULAR_SENSITIVITY = {"min": 1, "max": 10}


class PacingValueRange:

    def __init__(self, pm):
        self.constraints = {
            "LRL": pm.lower_rate_limit >= PM_LIMIT.LOWER_RATE_LIMIT["max"],
            "URL": pm.upper_rate_limit <= PM_LIMIT.UPPER_RATE_LIMIT["max"],
            "URL_gt_LRL": pm.upper_rate_limit > pm.lower_rate_limit,
            "AA": pm.atrial_amplitude is None or \
                  PM_LIMIT.ATRIAL_AMPLITUDE["min"] < pm.atrial_amplitude <= PM_LIMIT.ATRIAL_AMPLITUDE["max"],
            "APW": pm.atrial_pulse_width is None or \
                   PM_LIMIT.ATRIAL_PULSE_WIDTH["min"] < pm.atrial_pulse_width <= PM_LIMIT.ATRIAL_PULSE_WIDTH["max"],
            "VA": pm.ventricular_amplitude is None or \
                  PM_LIMIT.VENTRICULAR_AMPLITUDE["min"] <= pm.ventricular_amplitude <= \
                  PM_LIMIT.VENTRICULAR_AMPLITUDE["max"],
            "VPW": pm.ventricular_pulse_width is None or \
                   PM_LIMIT.VENTRICULAR_PULSE_WIDTH["min"] < pm.ventricular_pulse_width <= \
                   PM_LIMIT.VENTRICULAR_PULSE_WIDTH["max"],
            "VRP": pm.vrp is None or \
                   PM_LIMIT.VRP["min"] <= pm.vrp <= PM_LIMIT.VRP["max"],
            "ARP": pm.arp is None or \
                   PM_LIMIT.ARP["min"] <= pm.arp <= PM_LIMIT.ARP["max"],
            "SR": pm.sensor_rate is None or \
                  PM_LIMIT.SENSOR_RATE["min"] <= pm.sensor_rate <= PM_LIMIT.SENSOR_RATE["max"],
            "AV": pm.av_delay is None or \
                  PM_LIMIT.AV_DELAY["min"] <= pm.av_delay <= PM_LIMIT.AV_DELAY["max"],
            "AS": pm.atrial_sensitivity is None or \
                  PM_LIMIT.ATRIAL_SENSITIVITY["min"] <= pm.atrial_sensitivity <= PM_LIMIT.ATRIAL_SENSITIVITY["max"],
            "VS": pm.ventricular_sensitivity is None or \
                  PM_LIMIT.VENTRICULAR_SENSITIVITY["min"] <= pm.ventricular_sensitivity <=
                  PM_LIMIT.VENTRICULAR_SENSITIVITY["max"]
        }

    def validate(self):
        for x in self.constraints.keys():
            if not self.constraints[x]:
                return PacingValidationResult(False, error_messages[x])

        return PacingValidationResult(True)
