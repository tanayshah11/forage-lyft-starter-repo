from Tires import Tire


class CarriganTires(Tire):
    def __init__(self, wears_arr):
        self.wears_arr = wears_arr

    def needs_service(self):
        return any(wear >= 0.9 for wear in self.wears_arr)