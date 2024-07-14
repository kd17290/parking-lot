from parking.models.gate import Gate
from parking.repositories.in_memory_crud_repository import InMemoryCRUDRepository


class GateRepository(InMemoryCRUDRepository[Gate]):
    pass
