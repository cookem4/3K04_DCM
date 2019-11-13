from unittest import TestCase

from main.communication.SerialCommunicator import SerialCommunicator
from main.data.pacingmode.DOOR import DOOR


class TestSerialCommunicator(TestCase):

    def testSerialOuputsCorrectValues(self):
        paceDOOR = DOOR(66, 200, 3, 3, 4, 4, 100, 225)
        com: SerialCommunicator = SerialCommunicator("COM4")
        com.send_pacing_data(paceDOOR)


