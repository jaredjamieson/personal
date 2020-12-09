# Jared Jamieson
# CSIT 200
# Lab 11 - Main

import Course_Class, Transcript

### Individual Files work, Save and Load does not ###

def main():
    
    # Save and load files
    temp_info = []
    
    user_input = input('Would you like to load a transcript? (y/n): ')
    if user_input == 'y':
        filename = input('Enter file name: ')
        infile = open(filename, 'r')
        for line in infile:
            temp_info.append(line)
    elif user_input == 'n':
        filename = input('Enter new filename')
        infile = open(filename, 'w+')
    else:
        print('Invalid response.')
    
    print(
        ' 1) Add course'
        ' 2) Update Course'
        ' 3) Delete Course'
        ' 4) Lookup Course'
        ' 5) Find by Attribute'
        ' 6) Show All'
        ' 7) Calculate GPA'
        ' 8) Calculate Field GPA'
        '9)  Undo'
        '10) Redo'
        'Press Enter to exit'
        )
    response = input('Enter command: ')
    user_continue = True
    while user_continue:
        if response == '1':
            pass
        elif response == '2':
            pass
        elif response == '3':
            pass
        elif response == '4':
            pass
        elif response == '5':
            pass
        elif response == '6':
            pass
        elif response == '7':
            pass
        elif response == '8':
            pass
        elif response == '9':
            pass
        elif response == '10':
            pass
        else:
            user_continue = False
    
    
    

main()