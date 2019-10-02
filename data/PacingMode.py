import json
from enum import Enum
from data.pacingmodes.AOO import AOOBuilder
from data.pacingmodes.AAI import AAIBuilder
from data.pacingmodes.VOO import VOOBuilder
from data.pacingmodes.VVI import VVIBuilder


class PacingMode:
    NAME: str

    def __init__(self, lower_rate_limit: float, upper_rate_limit: float, atrial_amplitude: float,
                 atrial_pulse_width: float, ventricular_amplitude: float,
                 ventricular_pulse_width: float):
        self.lower_rate_limit = lower_rate_limit
        self.upper_rate_limit = upper_rate_limit
        self.atrial_amplitude = atrial_amplitude
        self.atrial_pulse_width = atrial_pulse_width
        self.ventricular_amplitude = ventricular_amplitude
        self.ventricular_pulse_width = ventricular_pulse_width

    def to_string(self):
        return json.dumps(self.__dict__)


class PacingModeBuilder:
    @staticmethod
    def from_string(pacing_mode_name: str, pacing_mode_settings: str):
        if pacing_mode_name == PacingModes.AOO:
            return AOOBuilder.from_string(pacing_mode_settings)
        if pacing_mode_name == PacingModes.AAI:
            return AAIBuilder.from_string(pacing_mode_settings)
        if pacing_mode_name == PacingModes.VOO:
            return VOOBuilder.from_string(pacing_mode_settings)
        if pacing_mode_name == PacingModes.VVI:
            return VVIBuilder.from_string(pacing_mode_settings)

    @staticmethod
    def empty(pacing_mode_name: str):
        if pacing_mode_name == PacingModes.AOO:
            return AOOBuilder.empty()
        if pacing_mode_name == PacingModes.AAI:
            return AAIBuilder.empty()
        if pacing_mode_name == PacingModes.VOO:
            return VOOBuilder.empty()
        if pacing_mode_name == PacingModes.VVI:
            return VVIBuilder.empty()

    @staticmethod
    def empty():
        return PacingModeBuilder.empty(PacingModes.AOO)


class PacingModes(Enum):
    AAI = "AAI"
    AOO = "AOO"
    VOO = "VOO"
    VVI = "VVI"
