from parking.models.base_model import BaseModel
from parking.models.parking_lot import ParkingLot


class ParkingFloor(BaseModel):
    floor_name: str
    parking_lot = ParkingLot

    def __init__(self, floor_name: str, parking_lot: ParkingLot, id: int | None = None):
        super().__init__(id)
        self.floor_name = floor_name
        self.parking_lot = parking_lot
