r"""
Use singleton to ensure only one object of ParkingLot in the system
"""
import threading

class ParkingLot:
    # singleton
    instance = None

    class __OnlyOne:
        def __init__(self, name, address) -> None:
            # 1. initialize variables: read name, address and parking_rate from database
            # 2. initialize parking floors: read the parking floor map from database,
            #    this map should tell how many parking spots are there on each floor. This
            #    should also initialize max spot counts too.
            # 3. initialize parking spot counts by reading all active tickets from database
            # 4. initialize entrance and exit panels: read from database

            self.name = name
            self.address = address
            self.parking_rate = ParkingRate()

            self.mini_spot_count = 0
            self.large_spot_count = 0
            self.motorcycle_spot_count = 0
            self.electric_spot_count = 0

            self.max_mini_count = 0
            self.max_large_count = 0
            self.max_motorcycle_count = 0
            self.max_electric_count = 0

            self.entrance_panels = {}
            self.exit_panels = {}
            self.parking_floors = {}

            # all active parking tickets, identified by their ticket_number
            self.active_tickets = {}

            self.__lock = threading.Lock()

    def __init__(self, name, address) -> None:
        if not ParkingLot.instance:
            ParkingLot.instance = ParkingLot.__OnlyOne(name, address)
        else:
            ParkingLot.instance.name = name
            ParkingLot.instance.address = address
    
    def __getattr__(self, name):
        return getattr(self.instance, name)

    def get_new_parking_ticket(self, vehicle):
        if self.is_full(vehicle.get_type()):
            raise Exception("Parking full!")
        
        # synchronizing to allow multiple entrances panels to issue a new
        # parking ticket without interfering with each other
        self.__lock.acquire()
        ticket = ParkingTicket()
        vehicle.assign_ticket(ticket)
        ticket.save_inDB()

        self.__lock.release()
        return ticket
    
    def is_full(self, type):
        if type == "Car":
            return self.mini_spot_count >= self.max_mini_count
        elif type == "Truck":
            return self.large_spot_count >= self.max_large_count
        elif type == "Motorcycle":
            return self.motorcycle_spot_count >= self.max_motorcycle_count
        else:
            return self.electric_spot_count >= self.max_electric_count

    def is_full(self):
        for key in self.parking_floors:
            if not self.parking_floors[key].is_full():
                return False
        return True
    
    def increment_spot_count(self, type):
        if type == "Car":
            if self.mini_spot_count < self.max_mini_count:
                self.mini_spot_count += 1
            else:
                self.large_spot_count += 1
        elif type == "Truck":
            self.large_spot_count += 1
        elif type == "Motorcycle":
            self.motorcycle_spot_count += 1
        else:
            if self.electric_spot_count < self.max_electric_count:
                self.electric_spot_count += 1
            elif self.mini_spot_count < self.max_mini_count:
                self.mini_spot_count += 1
            else:
                self.large_spot_count += 1
    
    def add_parking_floor(self, floor):
        # store in DB
        pass

    def add_entrance(self, entrance_panel):
        # store in DB
        pass

    def add_excit(self, exit_panel):
        # store in DB
        pass
