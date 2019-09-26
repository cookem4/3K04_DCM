from data.pacingmodes.AAI import AAI
from data.pacingmodes.AOO import AOO
from data.pacingmodes.VOO import VOO
from data.pacingmodes.VVI import VVI
from data.PacingMode import PacingMode
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
            self.aii = pacing_mode
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
