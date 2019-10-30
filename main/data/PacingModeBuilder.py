from main.data.PacingModes import PacingModes
from main.data.pacingmodes.AAI import AAIBuilder
from main.data.pacingmodes.AOO import AOOBuilder
from main.data.pacingmodes.VOO import VOOBuilder
from main.data.pacingmodes.DOO import DOOBuilder
from main.data.pacingmodes.VVIR import VVIRBuilder
from main.data.pacingmodes.AAIR import AAIRBuilder
from main.data.pacingmodes.AOOR import AOORBuilder
from main.data.pacingmodes.VOOR import VOORBuilder
from main.data.pacingmodes.DOOR import DOORBuilder


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
        if pacing_mode_name == PacingModes.DOO.name:
            return DOOBuilder.from_string(pacing_mode_settings)
        if pacing_mode_name == PacingModes.AOOR.name:
            return AOORBuilder.from_string(pacing_mode_settings)
        if pacing_mode_name == PacingModes.VOOR.name:
            return VOORBuilder.from_string(pacing_mode_settings)
        if pacing_mode_name == PacingModes.AAIR.name:
            return AAIRBuilder.from_string(pacing_mode_settings)
        if pacing_mode_name == PacingModes.VVIR.name:
            return VVIRBuilder.from_string(pacing_mode_settings)
        if pacing_mode_name == PacingModes.DOOR.name:
            return DOORBuilder.from_string(pacing_mode_settings)

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
        
        if pacing_mode_name == PacingModes.DOO:
            return DOOBuilder.empty()
        
        if pacing_mode_name == PacingModes.AOOR:
            return AOORBuilder.empty()

        if pacing_mode_name == PacingModes.VOOR:
            return VOORBuilder.empty()

        if pacing_mode_name == PacingModes.AAIR:
            return AAIRBuilder.empty()

        if pacing_mode_name == PacingModes.VVIR:
            return VVIRBuilder.empty()

        if pacing_mode_name == PacingModes.DOOR:
            return DOORBuilder.empty()
        

    @staticmethod
    def empty():
        return PacingModeBuilder.empty_specific(PacingModes.AOO)
