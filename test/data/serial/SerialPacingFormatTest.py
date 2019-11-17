import unittest

from main.data.pacing.PacingMode import SerialPacingMode
from main.data.pacing.modes.AAI import AAI
from main.data.pacing.modes.AOO import AOO
from main.data.pacing.modes.DOOR import DOOR


class SerialPacingFormatTest(unittest.TestCase):
    def test_byte_array_matches_bytes(self):
        paceAAI = AAI(50, 150, 3, 4, 300)
        paceAOO = AOO(66, 175, 3, 2)
        paceDOOR = DOOR(66, 80, 3, 3, 3, 2, 1, 25, 14, 220)
        sutAAI: SerialPacingMode = SerialPacingMode(paceAAI)
        sutAOO: SerialPacingMode = SerialPacingMode(paceAOO)
        sutDOOR: SerialPacingMode = SerialPacingMode(paceDOOR)




if __name__ == '__main__':
    unittest.main()
