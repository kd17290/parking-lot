from abc import ABC, abstractmethod

from parking.models.additional_services import AdditionalServices
from parking.models.ticket import Ticket
from parking.models.vehicle_type import VehicleType


class TicketService(ABC):
    @abstractmethod
    def generate_ticket(
        self,
        gate_id: int,
        number_plate: str,
        vehicle_type: VehicleType,
        additional_services: list[AdditionalServices],
    ) -> Ticket:
        pass
