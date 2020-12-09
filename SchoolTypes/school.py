# Lab 13 - Jamieson and Cardaropoli

# Imports

# The School class
class School:
    
    # Constructor
    def __init__(self, name, location, number_of_students):
        # Creates attributes to self
        self.__name = name
        self.__location = location
        self.__number_of_students = number_of_students
        
    # String Method
    def __str__(self):
        return 'Name: ' + self.__name + '\nLocaction: ' + self.__location
        
    # Returns the name of the School
    def get_name(self):
        return self.__name
    
    # Returns the location of the School
    def get_location(self):
        return self.__location
        
    # Returns the number of students in the School
    def get_number_of_students(self):
        return self.__number_of_students
        
    # Changes the name of the School
    def set_name(self):
        username = str(input('Enter the name of the new school (String): '))
        self.__name = username
        
    # Changes the location of the School
    def set_location(self):
        userlocation = str(input('Enter the location of the new school (String): '))
        self.__location = userlocation
        
    # Changes the number of students of the School
    def set_number_of_students(self):
        userstudentnum = int(input('Enter the number of students in the new school (Integer): '))
        self.__number_of_students = userstudentnum
