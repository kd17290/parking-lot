from datetime import datetime

from parking.strategies.weekday_pricing_strategy import WeekdayPricingStrategy
from parking.strategies.weekend_pricing_strategy import WeekendPricingStrategy


class PricingStrategyFactory:
    @staticmethod
    def get_pricing_strategy():
        now = datetime.now()
        day = now.weekday()
        if day >= 5:
            return WeekendPricingStrategy()
        else:
            return WeekdayPricingStrategy()
