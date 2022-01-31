r"""
Parking floor
"""
from display_board import ParkingDisplayBoard

class ParkingFloor:
    def __init__(self, floor_num) -> None:
        self.floor_num = floor_num
        # Init for different spots
        self.mini_spots = {}
        self.large_spots = {}
        self.motorcycle_spots = {}
        self.electric_spots = {}
        self.customer_info_panels = {}
        self.display_board = ParkingDisplayBoard()
    
    def add_parking_spot(self, spot):
        putter = {
            "Mini": self.mini_spots.put(spot.get_number(), spot),
            "Large": self.large_spots.put(spot.get_number(), spot),
            "Motorcycle": self.motorcycle_spots.put(spot.get_number(), spot),
            "Electric": self.electric_spots.put(spot.get_number(), spot),
        }
        putter.get(spot.get_type(), "No corresponding parking spot type")
    
    def assign_spot(self, vehicle, spot):
        spot.assign_vehicle(vehicle)
        putter = {
            "Mini": self.update_display_board_for_mini.put(spot),
            "Large": self.update_display_board_for_large.put(spot),
            "Motorcycle": self.update_display_board_for_motorcycle.put(spot),
            "Electric": self.update_display_board_for_electric.put(spot),
        }
        putter.get(spot.get_type(), "No corresponding parking spot type")

    def update_display_board_for_mini(self, spot):
        if self.display_board.get_mini_free_spot().get_number() == spot.get_number():
            # find another free parking and assign to display_board
            for vid in self.mini_spots:
                if self.mini_spots[vid].is_free():
                    self.display_board.set_mini_free_spot(self.mini_spots[vid])
            
            self.display_board.show_empty_spot_number()

    def update_display_board_for_large(self, spot):
        if self.display_board.get_large_free_spot().get_number() == spot.get_number():
            # find another free parking and assign to display_board
            for vid in self.large_spots:
                if self.large_spots[vid].is_free():
                    self.display_board.set_large_free_spot(self.large_spots[vid])
            
            self.display_board.show_empty_spot_number()

    def update_display_board_for_motorcycle(self, spot):
        if self.display_board.get_motorcycle_free_spot().get_number() == spot.get_number():
            # find another free parking and assign to display_board
            for vid in self.motorcycle_spots:
                if self.motorcycle_spots[vid].is_free():
                    self.display_board.set_motorcycle_free_spot(self.motorcycle_spots[vid])
            
            self.display_board.show_empty_spot_number()

    def update_display_board_for_electric(self, spot):
        if self.display_board.get_electric_free_spot().get_number() == spot.get_number():
            # find another free parking and assign to display_board
            for vid in self.electric_spots:
                if self.electric_spots[vid].is_free():
                    self.display_board.set_electric_free_spot(self.electric_spots[vid])
            
            self.display_board.show_empty_spot_number()
    
    def free_spot(self, spot):
        spot.remove_vehicle()
        putter = {
            "Mini": self.__free_mini_spot_count += 1,
            "Large": self.__free_large_spot_count += 1,
            "Motorcycle": self.__free_motorcycle_spot_count += 1,
            "Electric": self.__free_electric_spot_count += 1,
        }
        putter.get(spot.get_type(), "No corresponding parking spot type")

