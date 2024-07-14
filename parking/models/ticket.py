from datetime import datetime

from parking.models.additional_services import AdditionalServices
from parking.models.base_model import BaseModel
from parking.models.coordinator import Coordinator
from parking.models.gate import Gate
from parking.models.parking_spot import ParkingSpot
from parking.models.Vehicle import Vehicle


class Ticket(BaseModel):
    vehicle: Vehicle
    coordinator: Coordinator
    entry_time: datetime
    gate: Gate
    parking_spot: ParkingSpot
    additional_services: list[AdditionalServices]

    def __init__(
        self,
        vehicle: Vehicle,
        coordinator: Coordinator,
        entry_time: datetime,
        gate: Gate,
        parking_spot: ParkingSpot,
        additional_services: list[AdditionalServices],
        id: int | None = None,
    ):
        super().__init__(id)
        self.vehicle = vehicle
        self.coordinator = coordinator
        self.entry_time = entry_time
        self.gate = gate
        self.parking_spot = parking_spot
        self.additional_services = additional_services
