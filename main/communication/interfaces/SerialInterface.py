import abc

from main.data.pacingmode.PacingMode import PacingMode


class SerialInterface(abc.ABC):

    @abc.abstractmethod
    def connect_to_pacemaker(self) -> None:
        pass

    @abc.abstractmethod
    def send_pacing_data(self, data: PacingMode) -> bool:
        pass

    @abc.abstractmethod
    def request_EGM_data(self):
        pass

    @abc.abstractmethod
    def receive_EGM_data(self) -> list:
        pass

    @abc.abstractmethod
    def check_timeout(self) -> bool:
        pass

    @abc.abstractmethod
    def end_egm_data(self) -> None:
        pass

    @abc.abstractmethod
    def get_graphing_data(self) -> list:
        pass

    @abc.abstractmethod
    def is_pacing_being_saved(self) -> bool:
        pass

    @abc.abstractmethod
    def get_device_ID(self) -> int:
        pass

    @abc.abstractmethod
    def is_connection_established(self) -> bool:
        pass

    @abc.abstractmethod
    def get_last_device_connected(self) -> str:
        pass
