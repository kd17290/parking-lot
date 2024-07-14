from parking.models.base_model import BaseModel


class ParkingLot(BaseModel):
    name: str
    address: str

    def __init__(self, name: str, address: str, id: int | None = None):
        super().__init__(id)
        self.name = name
        self.address = address
