import unittest


from Battery import SpindlerBattery
from Battery import NubbinBattery
from Engine.capulet_engine import CapuletEngine
from Engine.sternman_engine import SternmanEngine
from Engine.willoughby_engine import WilloughbyEngine


class EngineTests(unittest.TestCase):
    def test_CapuletEngine_needs_service(self):
        engine = CapuletEngine(50000, 20000)
        self.assertTrue(engine.needs_service())

    def test_WilloughbyEngine_needs_service(self):
        engine = WilloughbyEngine(70000, 50000)
        self.assertTrue(engine.needs_service())

    def test_SternmanEngine_needs_service_warning_light_on(self):
        engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service())

    def test_SternmanEngine_needs_service_warning_light_off(self):
        engine = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(engine.needs_service())


class BatteryTests(unittest.TestCase):
    def test_NubbinBattery_needs_service(self):
        last_service_date = "2022/01/01"
        current_date = "2023/07/16"
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_SpindlerBattery_needs_service(self):
        last_service_date = "2023/01/01"
        current_date = "2023/07/16"
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


if __name__ == "__main__":
    unittest.main()
