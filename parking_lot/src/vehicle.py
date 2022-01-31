r"""
Classes of Vehicles
"""


class Vehicle():
    def __init__(self, vehicle_id, vehicle_type) -> None:
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.ticket = None
    
    def assign_ticket(self, ticket):
        self.ticket = ticket


class Car(Vehicle):
    def __init__(self, vehicle_id) -> None:
        super().__init__(vehicle_id, "Car")


class Truck(Vehicle):
    def __init__(self, vehicle_id) -> None:
        super().__init__(vehicle_id, "Truck")


class Motorcycle(Vehicle):
    def __init__(self, vehicle_id) -> None:
        super().__init__(vehicle_id, "Motorcycle")


class ElectricCar(Vehicle):
    def __init__(self, vehicle_id) -> None:
        super().__init__(vehicle_id, "Electric")
