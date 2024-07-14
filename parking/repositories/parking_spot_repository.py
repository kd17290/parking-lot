from parking.models.parking_spot import ParkingSpot
from parking.repositories.in_memory_crud_repository import InMemoryCRUDRepository


class ParkingSpotRepository(InMemoryCRUDRepository[ParkingSpot]):
    pass
