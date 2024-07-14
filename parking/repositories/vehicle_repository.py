from parking.models.Vehicle import Vehicle
from parking.repositories.in_memory_crud_repository import InMemoryCRUDRepository


class VehicleRepository(InMemoryCRUDRepository[Vehicle]):
    pass
