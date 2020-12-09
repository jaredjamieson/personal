# Homework 7 - Jared Jamieson
#Dictionary containing state names, region, population, GDP and personal income.  

# import statements go here
import math
# Any global variables, if needed, go here

# DO NOT CHANGE all_states!!
all_states = {'Alabama': ['Southeast', '4.7848', '153.84', '162.2283'], \
          'Alaska': ['Far_West', '0.7141', '43.47', '32.6496'], \
          'Arizona': ['Southwest', '6.4108', '221.02', '217.7587'], \
          'Arkansas': ['Southeast', '2.9228', '92.08', '93.6831'], \
          'California': ['Far_West', '37.3344', '1672.5', '1579.1'], \
          'Colorado': ['Rocky_Mountain', '5.0485', '230.98', '210.6077'], \
          'Connecticut': ['New_England', '3.5766', '197.61', '197.8393'], \
          'Delaware': ['Mideast', '0.8998', '55.5', '36.9576'], \
          'D.O.C': ['Mideast', '0.605', '89.97', '42.2093'], \
          'Florida': ['Southeast', '18.846', '650.29', '725.4363'], \
          'Georgia': ['Southeast', '9.7147', '358.84', '333.6327'], \
          'Hawaii': ['Far_West', '1.3643', '59.67', '56.8272'], \
          'Idaho': ['Rocky_Mountain', '1.5708', '50.73', '50.3852'], \
          'Illinois': ['Great_Lakes', '12.8405', '571.23', '540.2233'], \
          'Indiana': ['Great_Lakes', '6.4899', '241.93', '223.1581'], \
          'Iowa ': ['Plains', '3.0503', '124.01', '119.0797'], \
          'Kansas': ['Plains', '2.8588', '113.32', '110.8847'], \
          'Kentucky': ['Southeast', '4.3467', '141.98', '143.211'], \
          'Louisiana': ['Southeast', '4.5441', '200.94', '169.1167'], \
          'Maine': ['New_England', '1.3276', '45.56', '49.3602'], \
          'Maryland': ['Mideast', '5.788', '264.32', '289.6531'], \
          'Massachusetts': ['New_England', '6.5633', '340.16', '337.9316'], \
          'Michigan': ['Great_Lakes', '9.8777', '329.81', '346.8182'], \
          'Minnesota': ['Plains', '5.3107', '240.42', '226.3199'], \
          'Mississippi': ['Southeast', '2.9691', '85.36', '91.5883'], \
          'Missouri': ['Plains', '5.9961', '216.68', '219.484'], \
          'Montana': ['Rocky_Mountain', '0.9907', '31.92', '34.2688'], \
          'Nebraska': ['Plains', '1.8297', '80.64', '73.0691'], \
          'Nevada': ['Far_West', '2.7038', '109.61', '99.2062'], \
          'New_Hampshire': ['New_England', '1.3168', '55.24', '59.1947'], \
          'New_Mexico': ['Southwest', '2.0648', '70.79', '68.4891'], \
          'New_Jersey': ['Mideast', '8.8034', '431.41', '449.0599'], \
          'New_York': ['Mideast', '19.3992', '1013.3', '960.8265'], \
          'North_Carolina': ['Southeast', '9.559', '380.69', '338.9875'], \
          'North_Dakota': ['Plains', '0.6743', '31.62', '29.1538'], \
          'Ohio': ['Great_Lakes', '11.5383', '413.99', '418.5351'], \
          'Oklahoma': ['Southwest', '3.7595', '132.92', '135.0626'], \
          'Oregon': ['Far_West', '3.8382', '174.17', '137.6717'], \
          'Pennsylvania': ['Mideast', '12.7113', '493.53', '529.8078'], \
          'Rhode_Island': ['New_England', '1.0528', '43.153', '45.2676'], \
          'South_Carolina': ['Southeast', '4.6358', '143.41', '151.5368'], \
          'South_Dakota': ['Plains', '0.8162', '34.37', '33.1357'], \
          'Tennessee': ['Southeast', '6.3567', '227.36', '225.2247'], \
          'Texas': ['Southwest', '25.2427', '1116.27', '961.8281'], \
          'Utah': ['Rocky_Mountain', '2.7751', '105.2', '90.1127'], \
          'Vermont': ['New_England', '0.626', '23.34', '25.1157'], \
          'Virginia': ['Southeast', '8.0251', '377.47', '359.9561'], \
          'Washington': ['Far_West', '6.7436', '307.69', '286.7438'], \
          'West_Virginia': ['Southeast', '1.854', '53.58', '58.9501'], \
          'Wisconsin': ['Great_Lakes', '5.6896', '219.08', '220.5023'], \
          'Wyoming': ['Rocky_Mountain', '0.5644', '32', '25.4336']}

# Function to print the contents of the dictionary with headers
# Parameter is the dictionary containing state information
def print_state_info():
    #Table Headers
    print('STATE            REGION          POP        GDP      INCOME')
    #Prints state name and info to allign with headers
    for i in all_states:
        print(i, " " * (15 - len(i)), all_states[i][0], " " * (14 - len(all_states[i][0])), all_states[i][1], " " * (9 - len(all_states[i][1])), all_states[i][2],
              " " * (7 - len(all_states[i][2])), all_states[i][3], " " * (9 - len(all_states[i][3])))
       
# Function to print the state name and the per-capita income for that state
# Parameter is the dictionary containing state information
def per_capita_income():
    #Table headers
    print('STATE           PER-CAPITA INCOME')
    #Prints state name and percap info alligned with headers
    for i in all_states:
        #Calculates percapita income per state
        percap = (float(all_states[i][3]) / float(all_states[i][1])) * 1000
        print(i, " " * (14 - (len(i))), round(percap, 2))
        
# Function to print the information and summary for one region of the country
# Parameters are the dictionary containing the state information and
# a string representing the region for which the user wants information
def print_region():
    userregion = input('Select a region (Far_West, Great_Lakes, Mideast, New_England, Plains, Rocky_Mountain, Southeast, Southwest): ')
    print('Report for', userregion, 'region')
    print('STATE             POP      GDP      INCOME')
    poptotal = 0
    incometotal = 0
    for i in all_states:
        if all_states[i][0] == userregion:
            print(i, " " * (15 - len(i)), all_states[i][1], " " * (7 - len(all_states[i][1])), all_states[i][2], " " * (7 - len(all_states[i][2])), all_states[i][3])
            poptotal += float(all_states[i][1])
            incometotal += float(all_states[i][3])
            percaptotal = (incometotal / poptotal)
            percapfinal = (percaptotal * 1000)
    print('Total population for the', userregion, 'region is', round(poptotal, 3), 'million')
    print('Total income for the', userregion, 'region is', round(incometotal, 3), 'billion')
    print('Per capita income for the', userregion, 'region is $', round(percapfinal, 2))

# Main function goes here
def main():
    #Function Calls
    #print_state_info()
    #per_capita_income()
    print_region()
    
# Call to main function here    
main()
            