from parking.models.parking_lot import ParkingLot
from parking.models.parking_spot import ParkingSpot
from parking.models.parking_spot_status import ParkingSpotStatus
from parking.models.vehicle_type import VehicleType
from parking.repositories.parking_spot_repository import ParkingSpotRepository
from parking.strategies.spot_assignment_strategy import SpotAssignmentStrategy


class RandomSpotAssignmentStrategy(SpotAssignmentStrategy):
    parking_spot_repository: ParkingSpotRepository

    def __init__(self, parking_spot_repository: ParkingSpotRepository):
        self.parking_spot_repository = parking_spot_repository

    def assign_spot(
        self, parking_lot: ParkingLot, vehicle_type: VehicleType
    ) -> ParkingSpot | None:
        open_spot: ParkingSpot | None = self.parking_spot_repository.find_one(
            parking_lot=parking_lot, vehicle_type=vehicle_type
        )
        if open_spot is None:
            return None

        open_spot.parking_spot_status = ParkingSpotStatus.OCCUPIED
        self.parking_spot_repository.update(open_spot)
        return open_spot
