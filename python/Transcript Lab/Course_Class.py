# Jared Jamieson
# CSIT 200
# Lab 11 - Course Class

class Course():
    """ Basic Course Class """
    def __init__(self, code = 'No Code', name = 'No Name', credit = 0, grade = 'No Grade',
                 semester = 'No semester listed', instructor = 'No instructor listed'):
        self.code = str(code)             # Course Code           (Ex. CS 200)
        self.name = name                  # Course Name           (Ex. Data Structures)
        self.credit = int(credit)         # Num Course Credits    (Ex. 4)
        self.grade = str(grade)           # Course Final Grade    (Ex. A-)
        self.semester = str(semester)     # Semester Course Taken (Ex. Fall 2019)
        self.instructor = instructor      # Instructor's Name     (Ex. Dr. Moulema)
        
    # Getter Methods
    def get_code(self):
        return self.code
    
    def get_name(self):
        return self.name
    
    def get_credit(self):
        return self.credit
    
    def get_grade(self):
        return self.grade
    
    def get_semester(self):
        return self.semester
    
    def get_instructor(self):
        return self.instructor
    
    def get_data(self):
        return ('\nCode: %s'
                '\nName: %s'
                '\nCredit: %s'
                '\nGrade: %s'
                '\nSemester: %s'
                '\nInstructor: %s'
                % (self.code, self.name, self.credit, self.grade, self.semester, self.instructor))
        
    
    # Setter Methods
    def set_code(self, code):
        self.code = code
        
    def set_name(self, name):
        self.name = name
        
    def set_credit(self, credit):
        self.credit = credit
        
    def set_grade(self, grade):
        self.grade = grade
        
    def set_semester(self, semester):
        self.semester = semester
        
    def set_instructor(self, instructor):
        self.instructor = instructor
        
        
def main():
    
    obj = Course(code = 'CS 200', name = 'Data Structures',
                 credit = 4, grade = 'A-', semester = 'Fall 2019',
                 instructor = 'Dr. Moulema')
    # Setters - Test
    '''
    obj.set_code()
    obj.set_name()
    obj.set_credit()
    obj.set_grade()
    obj.set_semester()
    obj.set_instructor()
    '''
    # Getters - Test
    '''
    print(obj.get_code())
    print(obj.get_name())
    print(obj.get_credit())
    print(obj.get_grade())
    print(obj.get_semester())
    print(obj.get_instructor())
    '''
    #print(obj.get_data())
    
#main()