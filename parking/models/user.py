from parking.models.base_model import BaseModel
from parking.models.user_type import UserType


class User(BaseModel):
    name: str
    email: str
    password: str
    is_active: bool = True
    phone_number: str
    user_type: UserType

    def __init__(
        self,
        name: str,
        email: str,
        password: str,
        phone_number: str,
        user_type: UserType,
        id: int | None = None,
    ):
        super().__init__(id)
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.user_type = user_type
