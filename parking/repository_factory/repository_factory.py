from parking.models.coordinator import Coordinator
from parking.models.gate import Gate
from parking.models.gate_type import GateType
from parking.models.parking_floor import ParkingFloor
from parking.models.parking_lot import ParkingLot
from parking.models.parking_spot import ParkingSpot
from parking.models.parking_spot_status import ParkingSpotStatus
from parking.models.vehicle_type import VehicleType
from parking.repositories.gate_repository import GateRepository
from parking.repositories.parking_lot_repository import ParkingLotRepository
from parking.repositories.parking_spot_repository import ParkingSpotRepository
from parking.repositories.ticket_repository import TicketRepository
from parking.repositories.vehicle_repository import VehicleRepository
from singleton import Singleton


class RepositoryFactory:
    @staticmethod
    def get_repository():
        return GlobalRepository()


class GlobalRepository(metaclass=Singleton["RepositoryFactory"]):
    def __init__(self):
        self.gate_repository = GateRepository()
        self.vehicle_repository = VehicleRepository()
        self.parking_lot_repository = ParkingLotRepository()
        self.ticket_repository = TicketRepository()
        self.parking_spot_repository = ParkingSpotRepository()
        self.create_sample_data()

    def create_sample_data(self):
        parking_lot = ParkingLot(
            name="first parking lot", address="first parking lot address"
        )
        self.parking_lot_repository.create(parking_lot)
        parking_spot = ParkingSpot(
            spot_name="Spot Name",
            parking_lot=parking_lot,
            parking_floor=ParkingFloor(
                floor_name="floor name", parking_lot=parking_lot
            ),
            parking_spot_status=ParkingSpotStatus.FREE,
            vehicle_type=VehicleType.CAR.value,
        )
        self.parking_spot_repository.create(parking_spot)
        coordinator = Coordinator(name="first coordinator", email="<email>")
        gate = Gate(
            name="first gate",
            gate_type=GateType.ENTRY,
            parking_lot=parking_lot,
            coordinator=coordinator,
        )
        self.gate_repository.create(gate)
