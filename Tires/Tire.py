from abc import abstractmethod

import Serviceable


class Tire(Serviceable):
    @abstractmethod
    def needs_service(self):
        pass