####Planet.py####

#Lab 12 Jamieson & Cardaropoli

#Imports
import math

class Planet:
    #Constructor
    def __init__(self, name, radius, mass, distance):
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__distance = distance
    
    #Returns last saved planet name
    def get_name(self):
        return self.__name
        
    #Returns planet's radius
    def get_radius(self):
        return self.__radius
    
    #Returns planet's mass
    def get_mass(self):
        return self.__mass
        
    #Returns the planet's total volume
    def get_volume(self):
        vol = ((4/3) * 3.14) * self.__radius ** 3
        return vol
    
    #Returns the planet's total surface area
    def get_surface_area(self):
        surfarea = (4 * math.pi) * (self.__radius ** 2)
        return surfarea
    
    #Sets the planet name to a new user string
    def set_name(self):
        newstr = input('Enter a new planet name: ')
        self.__name = newstr
    
    #Returns 'Planet (name)'
    def __str__(self):
        return 'Planet %s' % self.__name
