from abc import ABC, abstractmethod
from datetime import datetime

from parking.models.vehicle_type import VehicleType


class PricingStrategy(ABC):
    @abstractmethod
    def calculate_amount(
        self, exit_time: datetime, entry_time: datetime, vehicle_type: VehicleType
    ) -> float:
        pass
