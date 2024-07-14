from datetime import datetime

from parking.models.vehicle_type import VehicleType
from parking.strategies.pricing_strategy import PricingStrategy


class WeekdayPricingStrategy(PricingStrategy):
    def calculate_amount(
        self, exit_time: datetime, entry_time: datetime, vehicle_type: VehicleType
    ) -> float:
        hours = (exit_time - entry_time).seconds // 3600
        minimum_amount = 30
        return min(minimum_amount, hours * 10)
