from Tires import Tire


class OctoprimeTires(Tire):
    def __init__(self, wears_arr):
        self.wears_arr = wears_arr

    def needs_service(self):
        return sum(self.wears_arr) >= 3
