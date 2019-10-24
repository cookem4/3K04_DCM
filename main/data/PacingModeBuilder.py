from main.data.PacingModes import PacingModes
from main.data.pacingmodes.AAI import AAIBuilder
from main.data.pacingmodes.AOO import AOOBuilder
from main.data.pacingmodes.VOO import VOOBuilder
from main.data.pacingmodes.VVI import VVIBuilder


class PacingModeBuilder:
    @staticmethod
    def from_string(pacing_mode_name: str, pacing_mode_settings: str):
        if pacing_mode_name == PacingModes.AOO.name:
            return AOOBuilder.from_string(pacing_mode_settings)
        if pacing_mode_name == PacingModes.AAI.name:
            return AAIBuilder.from_string(pacing_mode_settings)
        if pacing_mode_name == PacingModes.VOO.name:
            return VOOBuilder.from_string(pacing_mode_settings)
        if pacing_mode_name == PacingModes.VVI.name:
            return VVIBuilder.from_string(pacing_mode_settings)

    @staticmethod
    def empty_specific(pacing_mode_name: PacingModes):
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
        return PacingModeBuilder.empty_specific(PacingModes.AOO)
