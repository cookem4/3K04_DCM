from enum import Enum


class PacingModes(Enum):
    AAI = "AAI"
    AOO = "AOO"
    VOO = "VOO"
    VVI = "VVI"
    DOO = "DOO"
    AOOR = "AOOR"
    VOOR = "VOOR"
    VVIR = "VVIR"
    AAIR = "AAIR"
    DOOR = "DOOR"


class SerialPacingModes(Enum):
    AOO = 0x01
    VOO = 0x02
    AAI = 0x03
    VVI = 0x04
    DOO = 0x05
    AOOR = 0x06
    VOOR = 0x07
    AAIR = 0x08
    VVIR = 0x09
    DOOR = 0x0A


paceMap = {
    PacingModes.AAI: SerialPacingModes.AAI,
    PacingModes.AOO: SerialPacingModes.AOO,
    PacingModes.VOO: SerialPacingModes.VOO,
    PacingModes.VVI: SerialPacingModes.VVI,
    PacingModes.DOO: SerialPacingModes.DOO,
    PacingModes.AOOR: SerialPacingModes.AOOR,
    PacingModes.VOOR: SerialPacingModes.VOOR,
    PacingModes.VVIR: SerialPacingModes.VVIR,
    PacingModes.AAIR: SerialPacingModes.AAIR,
    PacingModes.DOOR: SerialPacingModes.DOOR,
    PacingModes.AAI.name: SerialPacingModes.AAI,
    PacingModes.AOO.name: SerialPacingModes.AOO,
    PacingModes.VOO.name: SerialPacingModes.VOO,
    PacingModes.VVI.name: SerialPacingModes.VVI,
    PacingModes.DOO.name: SerialPacingModes.DOO,
    PacingModes.AOOR.name: SerialPacingModes.AOOR,
    PacingModes.VOOR.name: SerialPacingModes.VOOR,
    PacingModes.VVIR.name: SerialPacingModes.VVIR,
    PacingModes.AAIR.name: SerialPacingModes.AAIR,
    PacingModes.DOOR.name: SerialPacingModes.DOOR
}


def toSerial(mode: PacingModes or str) -> SerialPacingModes:
    return paceMap[mode].value
