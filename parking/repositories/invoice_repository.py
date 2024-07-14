from parking.models.invoice import Invoice
from parking.repositories.in_memory_crud_repository import InMemoryCRUDRepository


class InvoiceRepository(InMemoryCRUDRepository[Invoice]):
    pass
