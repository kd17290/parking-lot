from datetime import datetime

from parking.models.base_model import BaseModel
from parking.models.coordinator import Coordinator
from parking.models.gate import Gate
from parking.models.ticket import Ticket


class Invoice(BaseModel):
    ticket: Ticket
    gate: Gate
    coordinator: Coordinator
    exit_time: datetime
    amount: float

    def __init__(
        self,
        ticket: Ticket,
        gate: Gate,
        coordinator: Coordinator,
        exit_time: datetime,
        amount: float,
        id: int | None = None,
    ):
        super().__init__(id)
        self.ticket = ticket
        self.gate = gate
        self.coordinator = coordinator
        self.exit_time = exit_time
        self.amount = amount
