from abc import ABC, abstractmethod

from parking.models.parking_lot import ParkingLot
from parking.models.parking_spot import ParkingSpot
from parking.models.vehicle_type import VehicleType


class SpotAssignmentStrategy(ABC):
    @abstractmethod
    def assign_spot(
        self, parking_lot: ParkingLot, vehicle_type: VehicleType
    ) -> ParkingSpot | None:
        pass
