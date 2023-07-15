from abc import abstractmethod
import Serviceable
import car

class Engine(Serviceable):
    @abstractmethod
    def needs_service(self):
        pass