from main.data.egm.EGMPoint import EGMPoint
from main.data.pacing.PacingModeValidator import PM_LIMIT
from main.utils.SerialUtils import single_byte_to_value


class SerialEGMPoint(object):
    def __init__(self, data: bytearray):
        self.identifier = data[0]
        self.period = (data[1])
        self.atrium = single_byte_to_value(data[2], PM_LIMIT.ATRIAL_AMPLITUDE["max"])
        self.ventricle = single_byte_to_value(data[3], PM_LIMIT.VENTRICULAR_AMPLITUDE["max"])

    def to_egm_point(self):
        return EGMPoint(self.atrium, self.ventricle, self.period)
