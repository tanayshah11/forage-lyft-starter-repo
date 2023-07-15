from abc import abstractmethod
import Serviceable
import Battery
import Engine


class Car(Serviceable):
    def __init__(self, engine_make: Engine, battery_make: Battery):
        self.batteryMake = battery_make
        self.engineMake = engine_make

    @abstractmethod
    def needs_service(self):
        pass
