from datetime import datetime

from parking.exceptions import InvalidGateException, InvalidTicketException
from parking.models.gate import Gate
from parking.models.invoice import Invoice
from parking.models.Ticket import Ticket
from parking.repositories.gate_repository import GateRepository
from parking.repositories.invoice_repository import InvoiceRepository
from parking.repositories.ticket_repository import TicketRepository
from parking.repository_factory.pricing_strategy_factory import PricingStrategyFactory
from parking.services.invoice_service import InvoiceService


class InvoiceServiceImpl(InvoiceService):
    def __init__(
        self,
        ticket_repository: TicketRepository,
        invoice_repository: InvoiceRepository,
        gate_repository: GateRepository,
    ):
        self.ticket_repository = ticket_repository
        self.invoice_repository = invoice_repository
        self.gate_repository = gate_repository
        self.pricing_strategy = PricingStrategyFactory.get_pricing_strategy()

    def create_invoice(self, ticket_id: int, gate_id: int) -> Invoice:
        ticket: Ticket | None = self.ticket_repository.find_by_id(ticket_id)
        if ticket is None:
            raise InvalidTicketException()
        gate: Gate | None = self.gate_repository.find_by_id(gate_id)
        if gate is None:
            raise InvalidGateException()
        exit_time = datetime.now()
        amount: float = self.pricing_strategy.calculate_amount(
            exit_time, ticket.entry_time, ticket.vehicle.vehicle_type
        )
        # todo: Account for additional services and add up in amount.
        invoice: Invoice = Invoice(
            ticket=ticket,
            gate=gate,
            coordinator=gate.coordinator,
            exit_time=exit_time,
            amount=amount,
        )
        return self.invoice_repository.create(invoice)
