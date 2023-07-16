from abc import abstractmethod
import Serviceable
from Battery import Battery
from Engine import Engine


class Car(Serviceable):
    def __init__(self, engine_make: Engine, battery_make: Battery):
        self.batteryMake = battery_make
        self.engineMake = engine_make

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
