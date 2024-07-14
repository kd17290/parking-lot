from parking.dtos import (
    GenerateTicketRequestDTO,
    GenerateTicketResponseDTO,
    ResponseStatus,
)
from parking.exceptions import InvalidGateException, InvalidParkingLotException
from parking.services.ticket_service_impl import TicketServiceImpl


class TicketController:
    ticket_service: TicketServiceImpl

    def __init__(self, ticket_service: TicketServiceImpl):
        self.ticket_service = ticket_service

    def generate_ticket(
        self, request: GenerateTicketRequestDTO
    ) -> GenerateTicketResponseDTO:
        try:
            ticket = self.ticket_service.generate_ticket(
                request.gate_id,
                request.number_plate,
                request.vehicle_type,
                request.additional_services,
            )
            return GenerateTicketResponseDTO(
                response_status=ResponseStatus.SUCCESS, ticket=ticket
            )
        except (InvalidGateException, InvalidParkingLotException):
            return GenerateTicketResponseDTO(
                response_status=ResponseStatus.FAILURE,
            )
