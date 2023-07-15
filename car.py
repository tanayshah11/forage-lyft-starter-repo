from abc import abstractmethod
import Serviceable


class Car(Serviceable):
    def __init__(self, engine_make, battery_make):
        self.batteryMake = battery_make
        self.engineMake = engine_make

    @abstractmethod
    def needs_service(self):
        pass
