from parking.strategies.random_spot_assignment_strategy import (
    RandomSpotAssignmentStrategy,
)


class SpotAssignmentFactory:
    @staticmethod
    def get_spot_assignment():
        return RandomSpotAssignmentStrategy
