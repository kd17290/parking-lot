from dataclasses import dataclass
from enum import Enum

from parking.models.additional_services import AdditionalServices
from parking.models.ticket import Ticket
from parking.models.vehicle_type import VehicleType


class ResponseStatus(Enum):
    SUCCESS = 0
    FAILURE = 1


@dataclass
class GenerateTicketRequestDTO:
    gate_id: int
    number_plate: str
    vehicle_type: VehicleType
    additional_services: list[AdditionalServices]


@dataclass
class GenerateTicketResponseDTO:
    response_status: ResponseStatus
    ticket: Ticket | None = None
