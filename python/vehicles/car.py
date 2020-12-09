from vehicle import Vehicle

# Car class
class Car(Vehicle):
    
    # Car object counter 
    car_count = 0
    # Value counter
    total_value = 0
    
    # Constructor 
    def __init__(self, make, year, mileage, price, doornum):
        Vehicle.__init__(self, make, year, mileage, price)
        self.__doornum = doornum
        
        # Counts num of car objects
        Car.car_count += 1
        # Value adder
        Car.total_value += price
        
    # Returns doornum
    def get_doornum(self):
        return self.__doornum
    
    # Sets doornum
    def set_doornum(self):
        self.__doornum == int(input('Enter number of doors: '))
        
