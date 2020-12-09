#Lab 8 - Jared Jamieson Niccolo Cardaropoli

#Imports

#Problem 1 - Returns each key/value on a new line
def display_dict(animals):
    for key, value in animals.items():
        print(key + ',', value)

#problem 2 - Prints key, string, value
def display_entry(animals, string):
    for key, value in animals.items():
        print(key, string, value)

#Problem 3 - Adds name and species to dict
def add_animal(name, species, animals):
    animals[name] = species
    return animals

#Problem 4 - Deletes an animal
def del_animal(animals, name):
    animals.pop(name)
    return animals

#Problem 5 - Prints keys
def print_keys(animals):
    for key in animals:
        print(key)
        
#Problem 6 - Counts each letter in string
def letter_count(string):
    newdict = {}
    for letter in string:
        newdict[letter] = newdict.get(letter, 0) + 1
    return newdict

#Problem 7 - returns value of string in scrabble letters
def scrabble_value(string):
    score = 0
    scrletters = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,
                  'h':4,'i':1,'j':8,'k':5,'l':1,'m':3,'n':1,
                  'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,
                  'v':4,'w':4,'x':8,'y':4,'z':10}
    string = string.lower()
    for letter in string:
        score += scrletters[letter]
    return score

#Problem 8 - Returns squares including given number
def create_squares(integer):
    int_dict = dict()
    for x in range(1,integer):
        int_dict[x]=x**2
    return int_dict

#problem 9 - takes two dictionaries and returns a single dictionary
#that contains all of the elements in both dictionar
def combine_dict(animals,states):
    animals.update(states)
    return animals

#problem 10 - takes two lists and creates a dictionary where the element in the first list is the key to the element in the second list.
def lists_to_dict(list1, list2):
    dictionary = dict(zip(list1, list2))
    return dictionary

#Main functions
def main():
    '''
    #Dictionary of animals and their names
    animals = {
        'Hedwig':'owl', 'Kha':'snake', 'Elsa':'lion',
        'Phil':'groundhog', 'Jumbo':'elephant'}
    #Dictionary of states and their acronyms
    states = {"Massachusetts" : "MA",
          "Pennsilvania" : "PA",
          "Conneticut" : "CT",
          "Florida" : "FL",
          "New Hampshire": "NH",
          "New York": "NY",
          "Texas" : "TX",
          "California" : "CA",
          "Mississippi" : "MI",
          "Washington" : "WA",
          "Missouri" : "MR",
          "Minnisota" : "MN",
          "Arizona" : "AZ",
          "New Mexico" : "NM"
          }
    '''
    #User inputs
    #name = str(input('Enter an animal name: '))
    #string = str(input('Enter a string: '))
    #species = str(input('Enter a species: '))
    #integer = int(input("Enter an integer: "))+1
    #Two lists for Problem 10
    #list1 = [123, 456, 789]
    #list2 = ["Jose", "Xian", "Radda"]

    #Functions
    #display_dict(animals)
    #display_entry(animals, string)
    #print(add_animal(name, species, animals))
    #print(del_animal(animals, name))
    #print_keys(animals)
    #print(letter_count(string))
    #print(create_squares(integer))
    #print (combine_dict(animals,states))
    #print(scrabble_value(string))
    #print(lists_to_dict(list1, list2))

#Calls the main function
main()
