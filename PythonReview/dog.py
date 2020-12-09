# Lab 1 - Jared Jamieson

# The Dog class
class Dog:
    
    # Constructor - Defines arguments to be used in methods
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    
    # Getter Methods
    
    # Returns the dog's name
    def get_name(self):
        
        return self.name
    
    # Returns the dog's age
    def get_age(self):
        
        return self.age
    
    # Returns the dog's breed
    def get_breed(self):
        
        return self.breed
    
    
    # Setter Methods
    
    # Overrides's the dog's name
    def set_name(self):
        
        self.name = str(input("Enter dog's name: "))
    
    # Overrides the dog's age
    def set_age(self):
        
        self.age = int(input("Enter dog's age: "))
        
    # Overrides the dog's breed
    def set_breed(self):
        
        self.breed = str(input("Enter deg's breed: "))
        
        
# Main Function
def main():
    
    # Populates dog object
    #Obj = Class ( name, age, breed )
    dogobj = Dog('Max', 2, 'beagle')
    
    # Setter Method Calls
    dogobj.set_name()
    dogobj.set_age()
    dogobj.set_breed()
    
    # Getter Method Calls (Differ from main object due to setter calls first)
    print(dogobj.get_name())
    print(dogobj.get_age())
    print(dogobj.get_breed())
    
    
    
    

main()