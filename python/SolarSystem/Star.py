####Star.py####

#Lab 12 Jamieson & Cardaropoli

#Imports

class Star:
    #Constructor
    def __init__(self, name, type1, mass):
        self.__name = name
        self.__type1 = type1
        self.__mass = mass
        
    #Returns "'name' Star"
    def __str__(self):
        return self.__name + 'Star'
        
    #Returns the name of the star
    def get_name(self):
        return self.__name
        
    #Returns the type of the star
    def get_type(self):
        return self.__type1
        
    #Returns the mass of the star
    def get_mass(self):
        return self.__mass
        
    #Sets the name of the star
    def set_name(self):
        newname = str(input('Enter a new star name: '))
        self.__name = newname
        
    #Sets the type of star
    def set_type(self):
        newtype = str(input('Enter a new star type: '))
        self.__type1 = newtype
        
    #Sets the mass of the star
    def set_mass(self):
        newmass = float(input('Enter a new star mass: '))
        self.__mass = newmass
    