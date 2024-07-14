from abc import ABC


class BaseModel(ABC):
    id: int

    def __init__(self, id: int | None = None):
        self.id = id
