r"""
Classes of accounts that can control systems.
Admin can 
"""


class Account:
    def __init__(self, user_id, pwd, status=AccountStatus.Active) -> None:
        self.user_id = user_id
        self.pwd = pwd
        self.status = status
    
    def reset_password(self):
        pass


class Admin(Account):
    def __init__(self, user_id, pwd, status=AccountStatus.Active) -> None:
        super().__init__(user_id, pwd, status)
    
    def add_parking_floor(self, floor):
        pass

    def add_parking_spot(self, floor, spot):
        pass

    def add_parking_display_board(self, floor, display_board):
        pass

    def add_customer_info_panel(self, floor, customer_info):
        pass

    def add_excit_panel(self, excit_panel):
        pass


class ParkingAttendant(Account):
    def __init__(self, user_id, pwd, status=AccountStatus.Active) -> None:
        super().__init__(user_id, pwd, status)
    
    def process_ticket(self, ticket_id):
        pass
