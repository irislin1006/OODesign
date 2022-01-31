r"""
Classes of parking spots
"""
from abc import ABC


class ParkingSpot(ABC):
    def __init__(self, number, parking_spot_type) -> None:
        self.number = number
        self.parking_spot_type = parking_spot_type
        self.is_free = True
        self.__vehicle = None
    
    def is_free(self):
        return self.is_free
    
    def assign_vehicle(self, vehicle):
        self.__vehicle = vehicle
        self.is_free = False
    
    def remove_vehicle(self):
        self.__vehicle = None
        self.is_free = True


class MiniSpot(ParkingSpot):
    def __init__(self, number) -> None:
        super().__init__(number, "Mini")


class LargeSpot(ParkingSpot):
    def __init__(self, number) -> None:
        super().__init__(number, "Large")


class MotorcycleSpot(ParkingSpot):
    def __init__(self, number) -> None:
        super().__init__(number, "Motorcycle")


class ElectricCarSpot(ParkingSpot):
    def __init__(self, number) -> None:
        super().__init__(number, "Electric")
