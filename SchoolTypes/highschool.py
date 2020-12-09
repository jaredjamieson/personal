# Lab 13 - Jamieson and Cardaropoli

# Imports
from school import School

# The HighSchool class
class HighSchool(School):
    
    # Constructor
    def __init__(self, name, location, number_of_students, is_public, mascot, number_of_AP_classes):
        
        # Invokes constructor from superclass
        School.__init__(self, name, location, number_of_students)
        
        # Adds attributes to self
        self.__is_public = is_public
        self.__mascot = mascot
        self.__number_of_AP_classes = number_of_AP_classes
        
    # Returns boolean if HighSchool is public
    def get_is_public(self):
        if self.__is_public == 'True':
            return True
        elif self.__is_public == 'False':
            return False
        else:
            return 'Input is invalid'
    
    # Returns the mascot for the HighSchool
    def get_mascot(self):
        return self.__mascot
        
    # Returns the number of AP classes for the HighSchool
    def get_number_of_AP_classes(self):
        return self.__number_of_AP_classes
    
    # Sets boolean if HighSchool is public
    def set_is_public(self):
        userbool = str(input('Enter if the High School is public (True/False): '))
        if userbool == 'T' or userbool == 'True' or userbool == 't' or userbool == 'true':
            self.__is_public == True
        elif userbool == 'F' or userbool == 'False' or userbool == 'f' or userbool == 'false':
            self.__is_public == False
        else:
            print('User input is invalid')
    
    # Sets the mascot for the HighSchool
    def set_mascot(self):
        usermascot = str(input('Enter the High School mascot: '))
        self.__mascot = usermascot
        
    # Sets the number of AP classes for HighSchool
    def set_number_of_AP_classes(self):
        userclasses = int(input('Enter the number of AP classes: '))
        self.__number_of_AP_classes = userclasses
