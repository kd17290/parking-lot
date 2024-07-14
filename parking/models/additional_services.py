from enum import Enum

from parking.models.vehicle_type import VehicleType


class AdditionalServices(Enum):
    CAR_WASH = ([VehicleType.CAR, VehicleType.SUV], 400)
    CAR_DETAILING = ([VehicleType.CAR, VehicleType.SUV], 500)
    BIKE_WASH = ([VehicleType.BIKE, VehicleType.EV_BIKE], 100)
    SCOOTER_WASH = ([VehicleType.SCOOTER, VehicleType.EV_SCOOTER], 800)
    EV_CAR_CHARGE = ([VehicleType.EV_CAR], 300)
    EV_BIKE_CHARGE = ([VehicleType.EV_BIKE], 100)
    EV_SCOOTER_CHARGE = ([VehicleType.EV_SCOOTER], 80)
