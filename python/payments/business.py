# The Business class holds a name, owner, and a list of payments
class Business:
    # The init method takes values for the company name, owner
    # and sets up an empty list of payments
    def __init__(self, company, owner):
        self.__company = company
        self.__owner = owner
        self.__payments = []
   
    def get_company(self):
        return self.__company
    
    def get_owner(self):
        return self.__owner
    
    def add_payment(self, pymnt):
        self.__payments.append(pymnt)
    
    def print_payments(self): 
        for pymnt in self.__payments:
            print(pymnt)
