from abc import abstractmethod, ABC


class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass
