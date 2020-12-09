####SolarSystem.py####

#Lab 12 Jamieson & Cardaropoli

#Imports
from Star import Star
from Planet import Planet

class SolarSystem:
    #Constructor
    def __init__(self, sun):
        self.__sun = sun
        self.__planets = []
        
    #Returns the sun
    def get_sun(self):
        return self.__sun
        
    #Returns the planets list
    def get_planets(self):
        return self.__planets
    
    #Adds a planet to the planet list    
    def add_planet(self, planet):
        self.__planets.append(planet)
        
    #Remove a planet from the planets list
    def remove_planet(self, planetString):
        for planet in self.__planets:
            if planet.get_name() == planetString:
                self.__planets.remove()
        
    #Returns "'Star name' Solar System"
    def __str__(self):
        return '%s Solar System' % self.__sun.get_name()        