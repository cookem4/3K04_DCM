import unittest

from main.data.pacing.modes.AAI import AAI
from main.data.pacing.modes.AOO import AOO
from main.data.pacing.modes.DOOR import DOOR
from main.data.serial.SerialPacingFormat import SerialPacingFormat


class SerialPacingFormatTest(unittest.TestCase):
    def test_byte_array_matches_bytes(self):
        paceAAI = AAI(50, 150, 3, 4, 300)
        paceAOO = AOO(66, 175, 3, 2)
        paceDOOR = DOOR(66, 200, 3, 3, 4, 4, 100, 225)
        sutAAI: SerialPacingFormat = SerialPacingFormat(paceAAI)
        sutAOO: SerialPacingFormat = SerialPacingFormat(paceAOO)
        sutDOOR: SerialPacingFormat = SerialPacingFormat(paceDOOR)

        bAAI: bytearray = sutAAI.getBytes()
        bAOO: bytearray = sutAOO.getBytes()
        bDOOR: bytearray = sutDOOR.getBytes()

        self.assertEqual([x for x in bAAI], sutAAI.bytes)
        self.assertEqual([x for x in bAOO], sutAOO.bytes)
        self.assertEqual([x for x in bDOOR], sutDOOR.bytes)


if __name__ == '__main__':
    unittest.main()
