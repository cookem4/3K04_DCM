import unittest

from main.data.pacing.modes.AAI import AAI
from main.data.pacing.modes.VOOR import VOOR
from main.utils.SerialUtils import double_byte_to_value


class OutboundSerialPacingFormatTest(unittest.TestCase):
    aair = AAI(60, 70, 4, 3, 300)
    voor = VOOR(60, 70, 4, 3, 5, 20, 8, 100, 9)

    def testSerialMatchesInputtedData(self):
        data = self.aair.serialize()
        data_arr = [x for x in data]
        lrl = double_byte_to_value(data_arr[1:3], 220)
        url = double_byte_to_value(data_arr[3:5], 220)
        aa = double_byte_to_value(data_arr[5:7], 5)
        apw = double_byte_to_value(data_arr[7:9], 5)
        arp = double_byte_to_value(data_arr[9:11], 500)

        self.assertEqual(25, len(data))
        self.assertEqual(60, lrl)
        self.assertEqual(70, url)
        self.assertEqual(4, aa)
        self.assertEqual(3, apw)
        self.assertEqual(300, arp)

    def testAnotherSerialMatchesInputtedData(self):
        data = self.voor.serialize()
        data_arr = [x for x in data]
        lrl = double_byte_to_value(data_arr[1:3], 220)
        url = double_byte_to_value(data_arr[3:5], 220)
        va = double_byte_to_value(data_arr[5:7], 5)
        vpw = double_byte_to_value(data_arr[7:9], 5)
        at = double_byte_to_value(data_arr[9:11], 6)
        reat = double_byte_to_value(data_arr[11:13], 50)
        rect = double_byte_to_value(data_arr[13:15], 16)
        msr = double_byte_to_value(data_arr[15:17], 175)
        rf = double_byte_to_value(data_arr[17:19], 16)

        self.assertEqual(25, len(data))
        self.assertEqual(60, lrl)
        self.assertEqual(70, url)
        self.assertEqual(4, va)
        self.assertEqual(3, vpw)
        self.assertEqual(5, at)
        self.assertEqual(20, reat)
        self.assertEqual(8, rect)
        self.assertEqual(100, msr)
        self.assertEqual(9, rf)


if __name__ == '__main__':
    unittest.main()
