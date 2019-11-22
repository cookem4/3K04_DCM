from main.data.egm.EGMPoint import EGMPoint
from main.constants.PacingValueRange import PM_LIMIT
from main.utils.SerialUtils import double_byte_to_value


class SerialEGMPoint(object):
    def __init__(self, data: bytearray):
        self.identifier = data[0]
        self.period = double_byte_to_value(data[1:3])
        self.atrium = double_byte_to_value(data[3:5], PM_LIMIT.ATRIAL_AMPLITUDE["max"])
        self.ventricle = double_byte_to_value(data[5:7], PM_LIMIT.VENTRICULAR_AMPLITUDE["max"])

    def to_egm_point(self):
        return EGMPoint(self.atrium, self.ventricle, self.period)
