from data.pacingmodes.AAI import AAI
from data.pacingmodes.AOO import AOO
from data.pacingmodes.VOO import VOO
from data.pacingmodes.VVI import VVI
from data.pacingmodes.AAI import AAIBuilder
from data.pacingmodes.AOO import AOOBuilder
from data.pacingmodes.VOO import VOOBuilder
from data.pacingmodes.VVI import VVIBuilder
from data.PacingMode import PacingMode
from data.PacingMode import PacingModes
import json


class Configuration:
    aai: AAI
    aoo: AOO
    voo: VOO
    vvi: VVI

    def __init__(self):
        self.aai = AAI(0, 0, 0, 0)
        self.aoo = AOO(0, 0, 0, 0)
        self.voo = VOO(0, 0, 0, 0)
        self.vvi = VVI(0, 0, 0, 0)

    def set_pacing_mode(self, pacing_mode: PacingMode):
        if pacing_mode.NAME == AAI.NAME:
            self.aai = pacing_mode
        elif pacing_mode.NAME == AOO.NAME:
            self.aoo = pacing_mode
        elif pacing_mode.NAME == VOO.NAME:
            self.voo = pacing_mode
        elif pacing_mode.NAME == VVI.NAME:
            self.vvi = pacing_mode

    def to_string(self):
        data = {AAI.NAME: self.aai.to_string(),
                AOO.NAME: self.aoo.to_string(),
                VOO.NAME: self.voo.to_string(),
                VVI.NAME: self.vvi.to_string()}
        return json.dumps(data)

    def get(self, mode: PacingModes):
        if mode == PacingModes.AAI:
            return self.aai
        elif mode == PacingModes.AOO:
            return self.aoo
        elif mode == PacingModes.VOO:
            return self.voo
        elif mode == PacingModes.VVI:
            return self.vvi
        else:
            return None


class ConfigurationBuilder:

    def from_json(self, config_json):
        config = Configuration()
        config.aai = AAIBuilder().from_string(json.loads(config_json)[AAI.NAME])
        config.aoo = AOOBuilder().from_string(json.loads(config_json)[AOO.NAME])
        config.voo = VOOBuilder().from_string(json.loads(config_json)[VOO.NAME])
        config.vvi = VVIBuilder().from_string(json.loads(config_json)[VVI.NAME])
        return config
