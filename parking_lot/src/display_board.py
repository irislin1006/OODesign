r"""
parking display board
"""

class ParkingDisplayBoard:
    def __init__(self, parking_id) -> None:
        self.id = parking_id
        self.mini_free_spot = None
        self.large_free_spot = None
        self.motorcycle_free_spot = None
        self.electric_free_spot = None
    
    def show_empty_spot_number(self):
        message = ""
        if self.mini_free_spot.is_free():
            message += "Free Mini: " + self.mini_free_spot.get_number()
        else:
            message += "Mini spots are fulled"
        message += "\n"

        if self.large_free_spot.is_free():
            message += "Free Large: " + self.large_free_spot.get_number()
        else:
            message += "Large spots are fulled"
        message += "\n"

        if self.motorcycle_free_spot.is_free():
            message += "Free Motorcycle: " + self.motorcycle_free_spot.get_number()
        else:
            message += "Motorcycle spots are fulled"
        message += "\n"

        if self.electric_free_spot.is_free():
            message += "Free Electric car: " + self.electric_free_spot.get_number()
        else:
            message += "Electric car spots are fulled"
        message += "\n"

        print(message)
