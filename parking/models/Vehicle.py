from parking.models.base_model import BaseModel
from parking.models.vehicle_type import VehicleType


class Vehicle(BaseModel):
    number_plate: str
    vehicle_type: VehicleType

    def __init__(
        self, number_plate: str, vehicle_type: VehicleType, id: int | None = None
    ):
        super().__init__(id)
        self.number_plate = number_plate
        self.vehicle_type = vehicle_type
