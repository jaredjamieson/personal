# Basic vehicle class
class Vehicle:
    
    # Vehicle counter
    vehicle_num = 0
    
    # Constructor
    def __init__(self, make, year, mileage, price):
        self.__make = make
        self.__year = year
        self.__mileage = mileage
        self.__price = price
        
        # Vehicle counter incriment
        Vehicle.vehicle_num += 1
        
    ### Get methods ###
    
    # Returns make
    def get_make(self):
        return self.__make
    
    # Returns year
    def get_year(self):
        return self.__year
    
    # Returns mileage
    def get_mileage(self):
        return self.__mileage
    
    # Returns price
    def get_price(self):
        return self.__price
    
    ### Set methods ###
    
    # Sets make
    def set_make(self):
        self.__make == str(input('Enter new make of the vehicle: '))
    
    # Sets year
    def set_year(self):
        self.__year == str(input('Enter the new year of the vehicle: '))
    
    # Sets mileage
    def set_mileage(self):
        self.__mileage == str(input('Enter the new mileage of the vehicle: '))
    
    # Sets price
    def set_price(self):
        self.__price == str(input('Enter the new price of the vehicle: '))
