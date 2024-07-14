from datetime import datetime

from parking.exceptions import InvalidGateException, InvalidParkingLotException
from parking.models.additional_services import AdditionalServices
from parking.models.coordinator import Coordinator
from parking.models.gate import Gate
from parking.models.parking_spot import ParkingSpot
from parking.models.ticket import Ticket
from parking.models.Vehicle import Vehicle
from parking.models.vehicle_type import VehicleType
from parking.repositories.gate_repository import GateRepository
from parking.repositories.parking_lot_repository import ParkingLotRepository
from parking.repositories.parking_spot_repository import ParkingSpotRepository
from parking.repositories.ticket_repository import TicketRepository
from parking.repositories.vehicle_repository import VehicleRepository
from parking.repository_factory.spot_assignment_factory import SpotAssignmentFactory
from parking.services.ticket_service import TicketService


class TicketServiceImpl(TicketService):
    def __init__(
        self,
        gate_repository: GateRepository,
        vehicle_repository: VehicleRepository,
        parking_lot_repository: ParkingLotRepository,
        ticket_repository: TicketRepository,
        parking_spot_repository: ParkingSpotRepository,
    ):
        self.gate_repository = gate_repository
        self.vehicle_repository = vehicle_repository
        self.parking_lot_repository = parking_lot_repository
        self.ticket_repository = ticket_repository
        self.parking_spot_repository = parking_spot_repository
        self.spot_assignment_strategy = SpotAssignmentFactory.get_spot_assignment()

    def generate_ticket(
        self,
        gate_id: int,
        number_plate: str,
        vehicle_type: VehicleType,
        additional_services: list[AdditionalServices],
    ) -> Ticket:
        gate: Gate = self.gate_repository.find_by_id(gate_id)
        if not gate:
            raise InvalidGateException()
        parking_lot = gate.parking_lot
        coordinator: Coordinator = gate.coordinator
        vehicle: Vehicle = self.vehicle_repository.create(
            Vehicle(number_plate=number_plate, vehicle_type=vehicle_type)
        )
        parking_spot: ParkingSpot | None = self.spot_assignment_strategy(
            self.parking_spot_repository
        ).assign_spot(parking_lot=parking_lot, vehicle_type=vehicle_type)
        if not parking_spot:
            raise InvalidParkingLotException()
        ticket = Ticket(
            vehicle=vehicle,
            coordinator=coordinator,
            entry_time=datetime.now(),
            gate=gate,
            parking_spot=parking_spot,
            additional_services=additional_services,
        )
        return self.ticket_repository.create(ticket)
