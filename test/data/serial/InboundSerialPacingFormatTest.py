import unittest

from main.constants.PacingModes import SerialPacingModes
from main.constants.SerialIdentifier import SerialIdentifier
from main.data.pacing.modes.AAI import AAI
from main.data.serial.InboundSerialPacingMode import InboundSerialPacingMode


class InboundSerialPacingFormatTest(unittest.TestCase):
    aair = AAI(60, 70, 4, 3, 300)
    data = aair.as_serial.as_inbound_data()

    def testSerialMatchesInputtedData(self):
        self.assertTrue(self.aair.validation_result)
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
