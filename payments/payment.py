#Class Payment
# The init method takes values for the amount of
    # the payment and date and initializes the object with these. 
class Payment:
    def __init__(self, amount, date):
        self.__amount = amount
        self.__date = date
        
    # "Getters:"
    def get_amount(self): 
        return self.__amount
    
    def get_date(self): 
        return self.__date
    
    def __str__(self): 
        return "Date: " + self.__date + " Amount: " + str(self.__amount) 
    
