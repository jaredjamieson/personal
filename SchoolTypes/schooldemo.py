# Lab 13 - Jamieson and Cardaropoli

# Imports
from school import School
from elementaryschool import ElementarySchool
from highschool import HighSchool
from university import University

def main():
    
    schoollist = []
    
    ### Strings are used for numbers because arguments could include , and $ ###
    
    # Prime the subclasses
    uni = University('Western New England University', 'Springfield, Mass.', '3000', 'False', '20000', 'Golden Bear', '2000', '1000')
    #hs = HighSchool('WNE High', 'Springfield, Mass.', '500', 'True', 'Cubs', '6')
    #es = ElementarySchool('WNE Elementary', 'Springfield, Mass.', '300', 'False')
    
    '''
    # Uni Calls
    ## School Calls ##
    print('University Name: ', uni.get_name())
    print('University Location: ', uni.get_location())
    uni.set_name()
    print('New University Name: ', uni.get_name())
    uni.set_location()
    print('New University Location: ', uni.get_location())
    ## University Calls ##
    print('University Is Public: ', uni.get_is_public())
    print('University Tuition: $' + uni.get_tuition())
    print('University Mascot: ', uni.get_mascot())
    print('University Undergraduates: ', uni.get_number_of_undergrads())
    print('University Graduates: ', uni.get_number_of_grad_students())
    uni.set_is_public()
    print('New University Is Public: ', uni.get_is_public())
    uni.set_tuition()    
    print('New University Tuition: $' + uni.get_tuition())
    uni.set_mascot()
    print('New University Mascot: ', uni.get_mascot())
    uni.set_number_of_undergrads()
    print('New University Undergraduates: ', uni.get_number_of_undergrads())
    uni.set_number_of_grad_students()
    print('New University Graduates: ', uni.get_number_of_grad_students())
    '''
    '''
    # hs Calls
    ## School Calls ##
    print('Highschool Name: ', hs.get_name())
    print('Highschool Location: ', hs.get_location())
    hs.set_name()
    print('New Highschool Name: ', hs.get_name())
    hs.set_location()
    print('New Highschool Location: ', hs.get_location())
    ## HighSchool Calls ##
    print('Highschool Is Public: ', hs.get_is_public())
    print('Highschool Mascot: ', hs.get_mascot())
    print('Highschool AP Classes: ', hs.get_number_of_AP_classes())
    hs.set_is_public()
    print('New Highschool Is Public: ', hs.get_is_public())
    hs.set_mascot()
    print('New Highschool Mascot: ', hs.get_mascot())
    hs.set_number_of_AP_classes()
    print('New Highschool AP Classes: ', hs.get_number_of_AP_classes())
    '''
    '''
    # es Calls
    ## School Calls ##
    print('Elementary School Name: ', es.get_name())
    print('Elementary School Location: ', es.get_location())
    es.set_name()
    print('New Elementary School Name: ', es.get_name())
    es.set_location()
    print('New Elementary School Location: ', es.get_location())
    ## ElementarySchool Calls ##
    print('Elementary School Has A Playground: ', es.get_has_playground())
    es.set_has_playground()
    print('New Elementary School Has A Playground: ', es.get_has_playground())
    '''
    # Part 3 - Print str methods
    
    numschools = int(input('How many schools would you like to enter? '))
    while numschools != 0:
        schoollist.append(str(input('Enter type of school (school, elementary, highschool, university): ')))
        numschools -= 1
    
    for schooltype in schoollist:
        
        totalstudents = 0
        
        if schooltype == 'school':
            name = str(input('Enter school name: '))
            location = str(input('Enter school location: '))
            number_of_students = 1
            
            schoolinstance = School(name, location, number_of_students)
            print(schoolinstance.__str__())
            
        elif schooltype == 'elementary':
            name = str(input('Enter school name: '))
            location = str(input('Enter school location: '))
            number_of_students = int(input('Enter number of students: '))
            has_playground = 'null'
            
            elementaryinstance = ElementarySchool(name, location, number_of_students, has_playground)
            totalstudents += number_of_students
            print(elementaryinstance.__str__())
            
        elif schooltype == 'highschool':
            name = str(input('Enter school name: '))
            location = str(input('Enter school location: '))
            number_of_students = int(input('Enter number of students: '))
            is_public = 'null'
            mascot = 'null'
            number_of_AP_classes = 'null'
            
            highschoolinstance = HighSchool(name, location, number_of_students, is_public, mascot, number_of_AP_classes)
            totalstudents += number_of_students
            print(highschoolinstance.__str__())
            
        elif schooltype == 'university':
            name = str(input('Enter school name: '))
            location = str(input('Enter school location: '))
            number_of_students = 'null'
            is_public = 'null'
            tuition = 'null'
            mascot = 'null'
            number_of_undergrads = int(input('Enter number of undergrads: '))
            number_of_grad_students = int(input('Enter number of grads: '))
            
            universityinstance = University(name, location, number_of_students, is_public, tuition, mascot, number_of_undergrads, number_of_grad_students)
            totalstudents += number_of_undergrads
            totalstudents += number_of_grad_students
            print(universityinstance.__str__())
            
        else:
            print(schooltype, 'is not valid')
    
    print(totalstudents)
    #print('Total number of students: ', uni.get_number_of_students())
    
main()

