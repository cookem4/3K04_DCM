import unittest

from main.data.egm.EGMPoint import EGMPoint
from main.data.serial.SerialUtils import double_byte_to_value


class EGMDataTest(unittest.TestCase):
    def setUp(self) -> None:
        self.a_val = 4.25
        self.v_val = 2.75
        self.p_val = 300

    def test_EGM_to_serial(self):
        egm_point = EGMPoint(self.a_val, self.v_val, self.p_val)
        serialized_point = egm_point.serialize()
        assert double_byte_to_value([serialized_point[0], serialized_point[1]]) == self.p_val
        assert double_byte_to_value([serialized_point[2], serialized_point[3]], 5) == self.a_val
        assert double_byte_to_value([serialized_point[4], serialized_point[5]], 5) == self.v_val

