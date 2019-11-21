import unittest

from serial import to_bytes

from main.data.pacing.PacingModes import SerialPacingModes
from main.data.pacing.modes.AAI import AAI
from main.data.serial.InboundSerialPacingMode import InboundSerialPacingMode
from main.data.serial.SerialIdentifier import SerialIdentifier


class InboundSerialPacingFormatTest(unittest.TestCase):
    aair = AAI(60, 70, 4, 3, 300)
    data = [SerialIdentifier.SEND_DATA.value, 3, 0, 60, 0, 70, 0, 4, 0, 3, 0, 0, 0, 0, 1, 44]
    data = to_bytes(data + [0] * (34 - len(data)))

    def testSerialMatchesInputtedData(self):
        inboundSerialPacingMode = InboundSerialPacingMode(self.data)
        self.assertEqual(inboundSerialPacingMode.identifier, SerialIdentifier.SEND_DATA.value)
        self.assertEqual(inboundSerialPacingMode.pacingMode, SerialPacingModes.AAI.value)
        self.assertEqual(inboundSerialPacingMode.lower_rate_limit, 60)
        self.assertEqual(inboundSerialPacingMode.upper_rate_limit, 70)
        self.assertEqual(inboundSerialPacingMode.atrial_amplitude, 4)
        self.assertEqual(inboundSerialPacingMode.atrial_pulse_width, 3)
        self.assertEqual(inboundSerialPacingMode.arp, 300)


if __name__ == '__main__':
    unittest.main()
