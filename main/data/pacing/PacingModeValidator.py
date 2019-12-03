error_messages = {
    "LRL": "Lower rate limit must be above 40",
    "URL": "Upper rate limit must be below 220",
    "URL_gt_LRL": "Upper rate limit must be greater than lower rate limit",
    "AA": "Atrial Amplitude must be between 0-5",
    "APW": "Atrial pulse width must be between 0-5",
    "VA": "Ventricular Amplitude must be between 0-5",
    "VPW": "Ventricular pulse width must be between 0-5",
    "VRP": "VRP must be between 150-500",
    "ARP": "ARP must be between 150-500",
    "AT": "Activity threshold must be between 0-6",
    "REACT": "Reaction time must be between 10-50",
    "RECT": "Recovery time must be between 2-16",
    "SR": "Max sensor rate must be between 50-175",
    "RF": "Response factor must be between 1-16",
    "AV": "AV delay must be between 70-300",
    "AS": "Atrial Sensitivity must be between 1-5",
    "VS": "Ventricular Sensitivity must be between 1-5"
}


class PacingValidationResult:
    def __init__(self, success: bool, error: str = ""):
        self.success = success
        self.error = error


class PM_LIMIT:
    LOWER_RATE_LIMIT = {"min": 40, "max": 220}
    UPPER_RATE_LIMIT = {"min": 40, "max": 220}
    ATRIAL_AMPLITUDE = {"min": 0, "max": 5}
    ATRIAL_PULSE_WIDTH = {"min": 0, "max": 5}
    VENTRICULAR_AMPLITUDE = {"min": 0, "max": 5}
    VENTRICULAR_PULSE_WIDTH = {"min": 0, "max": 5}
    VRP = {"min": 150, "max": 500}
    ARP = {"min": 150, "max": 500}
    ACTIVITY_THRESHOLD = {"min": 0, "max": 6}
    REACTION_TIME = {"min": 10, "max": 50}
    RECOVERY_TIME = {"min": 2, "max": 16}
    MAX_SENSOR_RATE = {"min": 50, "max": 175}
    RESPONSE_FACTOR = {"min": 1, "max": 16}
    AV_DELAY = {"min": 70, "max": 300}
    ATRIAL_SENSITIVITY = {"min": 1, "max": 5}
    VENTRICULAR_SENSITIVITY = {"min": 1, "max": 5}


class PacingModeValidator:
    constraints = {}

    @staticmethod
    def form_pacing_mode(pm):
        PacingModeValidator.constraints = {
            "LRL": pm.lower_rate_limit >= PM_LIMIT.LOWER_RATE_LIMIT["min"],
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
            "AT": pm.activity_threshold is None or \
                  PM_LIMIT.ACTIVITY_THRESHOLD["min"] <= pm.activity_threshold <= PM_LIMIT.ACTIVITY_THRESHOLD["max"],
            "REACT": pm.activity_threshold is None or \
                     PM_LIMIT.REACTION_TIME["min"] <= pm.reaction_time <= PM_LIMIT.REACTION_TIME["max"],
            "RECT": pm.recovery_time is None or \
                    PM_LIMIT.RECOVERY_TIME["min"] <= pm.recovery_time <= PM_LIMIT.RECOVERY_TIME["max"],
            "SR": pm.max_sensor_rate is None or \
                  PM_LIMIT.MAX_SENSOR_RATE["min"] <= pm.max_sensor_rate <= PM_LIMIT.MAX_SENSOR_RATE["max"],
            "RF": pm.response_factor is None or \
                  PM_LIMIT.RESPONSE_FACTOR["min"] <= pm.response_factor <= PM_LIMIT.RESPONSE_FACTOR["max"],
            "AS": pm.atrial_sensitivity is None or \
                  PM_LIMIT.ATRIAL_SENSITIVITY["min"] <= pm.atrial_sensitivity <= PM_LIMIT.ATRIAL_SENSITIVITY["max"],
            "VS": pm.ventricular_sensitivity is None or \
                  PM_LIMIT.VENTRICULAR_SENSITIVITY["min"] <= pm.ventricular_sensitivity <=
                  PM_LIMIT.VENTRICULAR_SENSITIVITY["max"],
            "AV": pm.av_delay is None or \
                  PM_LIMIT.AV_DELAY["min"] <= pm.av_delay <=
                  PM_LIMIT.AV_DELAY["max"]
        }
        return PacingModeValidator

    @staticmethod
    def validate():
        for x in PacingModeValidator.constraints.keys():
            if not PacingModeValidator.constraints[x]:
                return PacingValidationResult(False, error_messages[x])

        return PacingValidationResult(True)
