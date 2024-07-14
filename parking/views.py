import json

from django.http import JsonResponse

from parking.controllers.ticket_controller import TicketController
from parking.dtos import GenerateTicketRequestDTO
from parking.repository_factory.repository_factory import RepositoryFactory
from parking.services.ticket_service_impl import TicketServiceImpl


def generate_ticket(request):
    repository = RepositoryFactory.get_repository()
    data = json.loads(request.body)
    request_dto = GenerateTicketRequestDTO(**data)
    ticket_service = TicketServiceImpl(
        gate_repository=repository.gate_repository,
        vehicle_repository=repository.vehicle_repository,
        parking_lot_repository=repository.parking_lot_repository,
        ticket_repository=repository.ticket_repository,
        parking_spot_repository=repository.parking_spot_repository,
    )
    response = TicketController(ticket_service).generate_ticket(request_dto)
    return JsonResponse({"ticket": response.ticket.id})
