#Lab 9 Jamieson & Cardaropoli
#Imports
import random
import csv
#Takes filename and prints one line at a time
def display_file(filename):
    userfile = open(filename, 'r')
    for line in userfile:
        print(int(line))
    userfile.close()

#Takes filename and n, prints top n lines
def display_head(filename, n):
    numbersFile = open('names.txt', 'r')
    for x in range(n):
        line = numbersFile.readline()
        line = line.rstrip("\n")
        print(line)
    numbersFile.close()
    
#Takes filename and prints each line with line num
def print_line_numbers(filename):
    count = 1
    userfile = open(filename, 'r')
    for line in userfile:
        line = line.rstrip('\n')
        print(count, '', line)
        count += 1
    userfile.close()

#takes filename and returns the length
def count_lines(filename):
    file = open(filename,"r")
    count = 0
    for lines in file:
        count = count+1
    file.close()
    return count

#Takes a filename and prints int total
def read_sum(filename):
    userfile = open(filename, 'r')
    total = 0
    for line in userfile:
        total += int(line)
    print(total)
    userfile.close()
    
#Takes a filename and returns the average of nums in file
def read_average(filename):
    file = open(filename, 'r')
    total = 0
    for x in filename:
        total = total + 1
    print(total)

#Takes filename and n, appends n random num to file
def write_random(filename, n):
    userfile = open(filename, 'w')
    for i in range(int(n)):
        num = str(random.randint(1, 500)) + '\n'
        userfile.write(num)
    userfile.close()
    print(userfile)
# takes a file and lists it out, prints the total of the numbers
def read_average(filename):
    userfile = open(filename, 'r')
    total = 0
    for line in userfile:
        
        total += int(line)
        line = line.rstrip("\n")
        print(line)
        
    print("The total is:",total)
    userfile.close()

#Takes a filename, asks for a name and age, adds appends age/name pair
def write_ages(filename):
    userfile = open(filename, 'w')
    again = 'y'
    while again =='y':
        print('Enter the following data:')
        name = input('Name: ')
        age = input('Age: ')
        total = '\n%s : %s' % (name, age)
        userfile.write(total)
        again = input('Another record (y/n)? ')
    userfile.close()

#reads a file and prints name/age within file
def read_ages(filename):
    file = open(filename, 'r')
    
    for line in file:
        line = line.rstrip("\n")
        x = (line.split(':'))
       
        print("Name:",x[0])
        print("Age:",x[1])
    file.close()

#Takes a filename and prints ave num words per line
def average_num_words(filename):
    userfile = open(filename, 'r')
    file = userfile.readlines()
    lines = 0
    count = 0
    for i in file:
        lines += 1
        for j in i:
            count += 1
    final = count / lines
    userfile.close()
    print('The average number of words per line is: ', final)
    
#Takes a file and returns num that survived
def num_survived(filename):
    with open(filename, 'r') as csvfile:
        #file = csv.readline()
        reader = csv.reader(csvfile, delimiter = ',')
        tlived = 0
        for row in reader:
            if row[1] == '1':
                tlived += 1
        print('The total number of people who survived are', tlived)

#Takes a filename and gender then prints survivers of gender
def num_gender_survived(filename, gender):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        tlived = 0
        for row in reader:
            if row[4] == gender:
                if row[1] == '1':
                    tlived += 1
        print('The total number of', gender, 'who survived are', tlived)

#Take a filename and returns the average age of the survivors
def average_age(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        totalage = 0
        used = 0
        line = csvfile.readline()
        for row in reader:
            if row[5] != '':
                totalage += float(row[5])
                used += 1
        average = totalage / used
        print('The average age of the survivors is', average)

def main():
    #Variables
    filename = 'titanic.csv'
    #n = input('Enter a number: ')
    #gender = input('Enter a gender (male/female): ')
    
    #Function calls
    #display_file(filename)
    #display_head(filename, n)
    #display_head(filename, n)
    #print_line_numbers(filename)
    #print(count_lines(filename))
    #write_random(filename, n)
    #read_average(filename)
    #write_ages(filename)
    #read_ages(filename)
    #average_num_words(filename)
    #num_gender_survived(filename, gender)
    #num_survived(filename)
    average_age(filename)

main()


