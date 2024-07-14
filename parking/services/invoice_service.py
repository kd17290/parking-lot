from abc import ABC, abstractmethod

from parking.models.invoice import Invoice


class InvoiceService(ABC):
    @abstractmethod
    def create_invoice(self, ticket_id: int, gate_id: int) -> Invoice:
        pass
