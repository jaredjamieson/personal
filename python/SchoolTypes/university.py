# Lab 13 - Jamieson and Cardaropoli

# Imports
from school import School

# The University class
class University(School):
    
    # Constructor
    def __init__(self, name, location, number_of_students, is_public, tuition, mascot, number_of_undergrads, number_of_grad_students):
        
        # Invokes constructor from superclass
        School.__init__(self, name, location, number_of_students)
        
        # Adds attributes to self
        self.__is_public = is_public
        self.__tuition = tuition
        self.__mascot = mascot
        self.__number_of_undergrads = number_of_undergrads
        self.__number_of_grad_students = number_of_grad_students
        
    # String Method
    def __str__(self):
        return 'Name: ' + self.__name + '\nLocation: ' + self.__location + '\nTuition: ' + self.__tuition
    
    # Totals students and overrides num_of_stu from school
    def get_number_of_students(self):
        return (int(self.__number_of_undergrads) + int(self.__number_of_grad_students))
    
    # Returns boolean if University is public
    def get_is_public(self):
        if self.__is_public == 'True' or self.__is_public == 'true' or self.__is_public == 't' or self.__is_public == 'T':
            return True
        elif self.__is_public == 'False' or self.__is_public == 'false' or self.__is_public == 'f' or self.__is_public == 'F':
            return False
        else:
            return 'Input is invalid'
        
    # Returns the tuition for the University
    def get_tuition(self):
        return self.__tuition
    
    # Returns the mascot for the University
    def get_mascot(self):
        return self.__mascot
    
    # Returns the number of undergrad students
    def get_number_of_undergrads(self):
        return self.__number_of_undergrads
    
    # Returns the number of grad students
    def get_number_of_grad_students(self):
        return self.__number_of_grad_students
    
    # Sets boolean if University is public
    def set_is_public(self):
        userbool = str(input('Enter if the University is public (True/Flase): '))
        if userbool == 'T' or userbool == 'True' or userbool == 't' or userbool == 'true':
            self.__is_public == True
        elif userbool == 'F' or userbool == 'False' or userbool == 'f' or userbool == 'false':
            self.__is_public == False
        else:
            print('User input is invalid')
        
    # Sets the tuition for the University
    def set_tuition(self):
        usertuition = str(input('Enter the tuition for the University (String): '))
        self.__tuition = usertuition
    
    # Sets the mascot for the University
    def set_mascot(self):
        usermascot = str(input('Enter the University mascot: '))
        self.__mascot = usermascot
    
    # Sets the number of undergrad students
    def set_number_of_undergrads(self):
        userundergrad = int(input('Enter the number of undergraduate students: '))
        self.__number_of_undergrads = userundergrad
    
    # Sets the number of grad students
    def set_number_of_grad_students(self):
        usergrad = int(input('Enter the number of graduate students: '))
        self.__number_of_grad_students = usergrad
