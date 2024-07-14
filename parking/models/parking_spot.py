from parking.models.base_model import BaseModel
from parking.models.parking_floor import ParkingFloor
from parking.models.parking_lot import ParkingLot
from parking.models.parking_spot_status import ParkingSpotStatus
from parking.models.vehicle_type import VehicleType


class ParkingSpot(BaseModel):
    spot_name: str
    parking_lot: ParkingLot
    parking_floor: ParkingFloor
    parking_spot_status: ParkingSpotStatus
    vehicle_type: VehicleType

    def __init__(
        self,
        spot_name: str,
        parking_lot: ParkingLot,
        parking_floor: ParkingFloor,
        parking_spot_status: ParkingSpotStatus,
        vehicle_type: VehicleType,
        id: int | None = None,
    ):
        super().__init__(id)
        self.spot_name = spot_name
        self.parking_lot = parking_lot
        self.parking_floor = parking_floor
        self.parking_spot_status = parking_spot_status
        self.vehicle_type = vehicle_type
