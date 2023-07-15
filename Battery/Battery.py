from abc import abstractmethod

import car


class Battery(car):
    @abstractmethod
    def needs_service(self):
        pass
