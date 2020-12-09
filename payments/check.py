import payment

class Check(payment.Payment):
    # The constructor calls the superclass' constructor
    def __init__(self, amount, date, account_no, routing_no, check_no):
        # Call supertype constructor
        payment.Payment.__init__(self, amount, date)
        self.__account_no = account_no
        self.__routing_no = routing_no
        self.__check_no = check_no
        
    # Getters:
    def get_account_no(self):
        return self.__account_no
    
    def get_routing_no(self):
        return self.__routing_no
    
    def get_check_no(self):
        return self.__check_no

    def __str__(self):
        return super().__str__()  + " Account no: " + self.__account_no \
            + " Routing no: " + self.__routing_no \
    + " Check no: " + str(self.__check_no)
