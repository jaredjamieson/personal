from vehicle import Vehicle

# Pickup class
class Pickup(Vehicle):
    
    # Pickup counter
    pickup_num = 0
    
    # Constructor
    def __init__(self, make, year, mileage, price, drivetype):
        Vehicle.__init__(self, make, year, mileage, price)
        self.__drivetype = drivetype
        
        # Pickup counter
        pickup_num += 1
        
    # Returns drivetype
    def get_drivetype(self):
        return self.__drivetype
    
    # Sets drivetype
    def set_drivetype(self):
        self.__drivetype = str(input('Enter drivetype of the pickup: '))