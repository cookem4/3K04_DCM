import time
import unittest
from main.communication.SerialCommunicator import SerialCommunicator
from test.communication.MockPacemaker import MockPacemaker



class SerialCommuncationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.pacemaker = MockPacemaker(port="COM1")
        self.communicator = SerialCommunicator(port="COM2")
        self.pacemaker.start()


    def test_recieve_egm_data(self):
        self.communicator.connect_to_pacemaker()
        self.pacemaker.stop()
        self.assertEqual(self.pacemaker.deviceId, self.communicator.device_id)


