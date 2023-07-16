from datetime import date

from Battery.NubbinBattery import NubbinBattery
from Battery.SpindlerBattery import SpindlerBattery
from Engine.capulet_engine import CapuletEngine
from Engine.sternman_engine import SternmanEngine
from Engine.willoughby_engine import WilloughbyEngine
from car import Car


class CarFactory:
    def __int__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    @staticmethod
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int):
        b = SpindlerBattery(last_service_date, current_date)
        e = CapuletEngine(current_mileage, last_service_mileage)
        c = Car(e, b)
        return c

    @staticmethod
    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        b = SpindlerBattery(last_service_date, current_date)
        e = WilloughbyEngine(current_mileage, last_service_mileage)
        c = Car(e, b)
        return c

    @staticmethod
    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool):
        b = SpindlerBattery(last_service_date, current_date)
        e = SternmanEngine(warning_light_on)
        c = Car(e, b)
        return c

    @staticmethod
    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        b = NubbinBattery(last_service_date, current_date)
        e = WilloughbyEngine(current_mileage, last_service_mileage)
        c = Car(e, b)
        return c

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        b = NubbinBattery(last_service_date, current_date)
        e = CapuletEngine(current_mileage, last_service_mileage)
        c = Car(e, b)
        return c
