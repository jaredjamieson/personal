from vehicle import Vehicle

# SUV class
class SUV(Vehicle):
    
    # SUV counter
    suv_num = 0
    
    # Constructor
    def __init__(self, make, year, mileage, price, passcap):
        Vehicle.__init__(self, make, year, mileage, price)
        self.__passcap = passcap
        
        # suv counter
        suv_num += 1
        
    # Returns passenger capacity
    def get_passcap(self):
        return self.__passcap
    
    # Sets passenger capacity
    def set_passcap(self):
        self.__passcap = str(input('Enter passenger capacity of the SUV: '))