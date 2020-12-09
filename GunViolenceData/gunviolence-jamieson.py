#Lab 8 - Jamieson
#Global Variable
FILE = "gun_violence_data_2018Q1.csv"
#Imports
from datetime import datetime
# The get_choice function presents the list of menu options
# and uses a loop to prompt the user to enter a menu option until a
# correct menu option is selected.
# DO NOT MODIFY THIS FUNCTION!
def get_choice():
    choice = 0
    while choice not in range(1,8):
            print("Choose from the following selections: ")
            print("1. List number of incidents by state")
            print("2. List number of incidents versus deaths by state")
            print("3. List incidents for a state")
            print("4. Count incidents for a characteristic")
            print("5. Count the number of incidents with a given participant status for a provided state")
            print("6. List the number of incidents by date that have occurred between a start and end date")
            print("7. Exit")
            choice = int(input("Enter a selection: "))
    return choice
# The list_incidents_by_state function prints a list of each state and the number of gun violence
# incidents there are by state. If there are no incidents, the state is not listed
# file_name - Name of the file that contains the state gun violence information
# DO NOT MODIFY THIS FUNCTION!!
def list_incidents_by_state(file_name):
    states = {}
    infile = open(file_name,'r', encoding='utf-8')
    # Read the header line as it should not be processed like the rest
    # of the data
    line = infile.readline()
    for line in infile:
            line = line.rstrip()
            line = line.split(',')
            if line[2] not in states:
                states[line[2]] = 1
            else:
                states[line[2]] = states[line[2]]+1
    infile.close()
    # Retrieve the set of keys  
    key_list = states.keys()
    # Turn it into a list
    key_list = list(key_list)
    # Sort the list alphabetically
    key_list.sort()
    # Print a formatted list of the states and number of incidents
    print("Number of gun violence incidents by state: ")
    print("{:25} {:10}".format("STATE", "INCIDENTS"))
    for key in key_list:
            print("{:25} {:10}".format(key, states[key]))
# Takes a filename, prints list [num gun violence incidents, num deaths, % deaths] for each state
def list_incidents_vs_deaths_by_state(file_name):
    states = {}
    infile = open(file_name,'r', encoding='utf-8')
    # Read the header line as it should not be processed like the rest
    # of the data
    line = infile.readline()
    for line in infile:
            line = line.rstrip()
            line = line.split(',')
            if line[2] not in states:
                deaths = int(line[5])
                states[line[2]] = [1, deaths]
            else:
                states[line[2]][0] += 1
                states[line[2]][1] += int(line[5])
            
    infile.close()
    # Retrieve the set of keys  
    key_list = states.keys()
    # Turn it into a list
    key_list = list(key_list)
    # Sort the list alphabetically
    key_list.sort()
    # Print a formatted list of the states and number of incidents
    print("Number of gun violence incidents by state: ")
    print("{:22} {:5} {:10} {:10}".format("STATE", "INCIDENTS", "DEATHS", "PCT DEATHS"))
    for key in key_list:
            divi = (states[key][1]/states[key][0])
            perc = round(divi, 2)
            print("{:22} {:5} {:10} {:10}".format(key, states[key][0], states[key][1], perc))
    
# Take a filename and state name, prints num deaths for state
def list_deaths_for_state(file_name):
    #User input
    state_name = input('Enter state for deaths by gun violence report: ')
    # Read the header line as it should not be processed like the rest
    # of the data
    infile = open(file_name,'r', encoding='utf-8')
    line = infile.readline()
    for line in infile:
            line = line.rstrip()
            line = line.split(',')
            if line[2] == state_name:
                print(line[1], line[3], line[4], line[6])
    
# Takes a filename and characteristic and returns total number of that incident
def count_for_characteristic(file_name):
    #User input
    characteristic = input('Enter characteristic to search for: ')
    #Prime total
    total_incidents = 0
    # Read the header line as it should not be processed like the rest
    # of the data
    infile = open(file_name,'r', encoding='utf-8')
    line = infile.readline()
    for line in infile:
            line = line.rstrip()
            line = line.split(',')
        #Looks for input in incident_characteristics
            if characteristic in line[10]:
                total_incidents += 1
    print('There were', total_incidents, 'incidents with characteristic:', characteristic)
# Takes filename, status and state then returns total num of incident
def count_for_status_for_state(file_name):
    #User inputs
    part_status = input('Enter participant status to search for: ')
    state_name = input('Enter state for participant status in interests: ')
    #Prime total
    total_incidents = 0
    # Read the header line as it should not be processed like the rest
    # of the data
    infile = open(file_name,'r', encoding='utf-8')
    line = infile.readline()
    for line in infile:
            line = line.rstrip()
            line = line.split(',')
            if line[2] == state_name:
                #Looks for input in participant_status
                if part_status in line[19]:
                    total_incidents += 1
    print('There were', total_incidents, 'incidents with status:', part_status, 'in', state_name)
#Take a begin and end date
def list_incidents_between_dates(file_name):
    #User inputs
    start_date = str(input('Enter start date (e.g., 2013-01-01: '))
    end_date = str(input('Enter end date (e.g., 2013-02-01): '))
    datedic = {}
    # Read the header line as it should not be processed like the rest
    # of the data
    infile = open(file_name,'r', encoding='utf-8')
    line = infile.readline()
    for line in infile:
        line = line.rstrip()
        line = line.split(',')
        dtime = datetime.strptime("2018-3-28", "%Y-%m-%d")
        exceldate = datetime.strptime(line[1], "%Y-%m-%d")
        startdate = datetime.strptime(start_date, "%Y-%m-%d")
        enddate = datetime.strptime(end_date, "%Y-%m-%d")
        if (startdate <= exceldate and enddate >= exceldate):
            if line[1] not in datedic:
                datedic[line[1]] = 1
            else:
                datedic[line[1]] += 1
    infile.close()
    # Retrieve the set of keys  
    key_list = datedic.keys()
    # Turn it into a list
    key_list = list(key_list)
    # Sort the list alphabetically
    key_list.sort()
    # Print a formatted list of the states and number of incidents
    print("{:25} {:10}".format("DATE", "INCIDENTS"))
    for key in key_list:
        print("{:22} {:10}".format(key, datedic[key]))
# The main program should call get_choice and loop through
# to call the function that corresponds with the chosen
# menu option.
def main():
# Code here
    global FILE
    file_name = FILE
        #User inputs
    #state_name = input('Enter a state name: ')
        
    userchoice = get_choice()
    if userchoice == 1: 
            list_incidents_by_state(file_name)
    elif userchoice == 2: 
            list_incidents_vs_deaths_by_state(file_name)
    elif userchoice == 3:
            list_deaths_for_state(file_name)
    elif userchoice == 4: 
            count_for_characteristic(file_name)
    elif userchoice == 5:
            count_for_status_for_state(file_name)
    elif userchoice == 6:
            list_incidents_between_dates(file_name)
main()
 
