# Design a Parking Lot

### Requirements 
1. Parking Lot should have multiple floors
2. Parking Lot should have multiple entries and exit points.
3. A customer will get a parking ticket at the entry points and can pay for it at the exit points
4. A customer will pay parking ticket at the automated exit panel or to the parking attendant
5. A customer can pay with cash or a credit card
6. A customer can pay at the customer info portal on each floor, and if he/she do so, they don't need to pay at the excit points
7. There will be a maximum capacity for the parking lot. If reached, there will be a display board suggest so.
8. There will be different parking spots for different types of vehicles (like Compact, Large, Motorcycle, etc.)
    * (Optional) If support parking spots for electric cars, there should be a electric panel for charging vehicles.
9. Each floor will have a display board showing any free parking spots for each type of spots.
10. There's a system to change the per-hour parking fee. 

### Use case 
1. Admin: for adding and modifying parking floors, parking spots, entrance, and exit panels, adding/removing parking attendants, etc.
2. Customer: can get a parking ticket or pay for it
3. Parking Attendant: can perform all activities on customer's behalf, and can take cash from customer for paying parking tickets
4. System: to control different situations:
    * display messages on different info panels on each floor
    * assigning/removing a vehicle from a parking spot

### Class
* ParkingLot
* ParkingFloor
* ParkingSpot
* Account: accounts for controlling the system.
    * Admin account
    * Parking attendant account
* Parking ticket
* Vehicle: an abstract supporting different types of vehicles
* EntrancePanel and ExitPanel
* Payment: support cash and credit card
* ParkingRate
* ParkingDisplayBoard
* ParkingAttendantPortal: contains all the operations that an attendant can perform, like scanning tickets and processing payments
* CustomerInfoPortal
* (Optional) ElectricPanel




