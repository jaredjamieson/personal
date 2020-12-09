# Lab 13 - Jamieson and Cardaropoli

# Imports
from school import School

# The ElementarySchool class
class ElementarySchool(School):
    
    # Constructor
    def __init__(self, name, location, number_of_students, has_playground):
        
        # Invokes constructor from superclass
        School.__init__(self, name, location, number_of_students)
        
        # Adds attributes to self
        self.__has_playground = has_playground
    
    # Returns boolean if ElementarySchool has a playground
    def get_has_playground(self):
        if self.__has_playground == 'True':
            return True
        elif self.__has_playground == 'False':
            return False
        else:
            return 'Input is invalid'
            
    # Sets boolean if ElementarySchool has a playground
    def set_has_playground(self):
        userbool = str(input('Enter if the Elementary School has a playground (True/False): '))
        if userbool == 'T' or userbool == 'True' or userbool == 't' or userbool == 'true':
            self.__has_playground == True
        elif userbool == 'F' or userbool == 'False' or userbool == 'f' or userbool == 'false':
            self.__has_playground == False
        else:
            print('User input is invalid')
