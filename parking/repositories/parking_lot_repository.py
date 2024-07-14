from parking.models.parking_lot import ParkingLot
from parking.repositories.in_memory_crud_repository import InMemoryCRUDRepository


class ParkingLotRepository(InMemoryCRUDRepository[ParkingLot]):
    pass
