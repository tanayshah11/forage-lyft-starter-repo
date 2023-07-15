from abc import abstractmethod
import datetime

import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        delta = datetime.strptime(self.current_date, "%Y/%m/%d") - datetime.strptime(self.last_service_date, "%Y/%m/%d")
        return delta > 1460
