from parking.models.ticket import Ticket
from parking.repositories.in_memory_crud_repository import InMemoryCRUDRepository


class TicketRepository(InMemoryCRUDRepository[Ticket]):
    pass
