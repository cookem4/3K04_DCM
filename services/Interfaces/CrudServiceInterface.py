import abc


class CrudServiceInterface(abc.ABC):

    @abc.abstractmethod
    def create(self, object):  # create and save a new object into database
        pass

    @abc.abstractmethod
    def read(self, key: str):  # find and return object with matching key if exists
        pass

    @abc.abstractmethod
    def update(self, object):  # if object with matching info exists, update it with this new info
        pass

    @abc.abstractmethod
    def delete(self, key: str):  # delete object if they exist
        pass
