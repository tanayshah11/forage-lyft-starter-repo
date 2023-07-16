import Serviceable
from Battery import Battery
from Engine import Engine
from Tires import Tire


class Car(Serviceable):
    def __init__(self, engine_make: Engine, battery_make: Battery, tire_make: Tire):
        self.batteryMake = battery_make
        self.engineMake = engine_make
        self.tire_make = tire_make

    def needs_service(self):
        return self.Engine.needs_service() or self.Battery.needs_service() or self.Tire.needs_service()
