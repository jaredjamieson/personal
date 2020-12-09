import payment
    
# The CreditCard class represents payment made by a credit card
class CreditCard(payment.Payment):
    # The constructor calls the superclass' constructor
    def __init__(self, amount, date, company, account_no, exp_date, security_no):
        # Call supertype constructor
        payment.Payment.__init__(self, amount, date)
        self.__company = company
        self.__account_no = account_no
        self.__exp_date = exp_date
        self.__security_no = security_no
        
    # Getters:
    def get_company(self):
        return self.__company
    
    def get_account_no(self):
        return self.__account_no
    
    def get_exp_date(self):
        return self.__exp_date
    
    def get_security_no(self):
        return self.__security_no
       
    def __str__(self):
        return super().__str__()  + " Company: " + self.__company \
            + " Account no: " + self.__account_no \
            + " Expiration date: " + self.__exp_date \
            + " Security code: " + self.__security_no
