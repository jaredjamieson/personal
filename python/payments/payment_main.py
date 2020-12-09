# Imports from payment.py
from payment import Payment
from check import Check
from creditcard import CreditCard
from business import Business

# Main function
def main():
    # Calls to the Payment file
    pay = Payment(100, "04/15/2016")
    #print(pay)
    
    # Calls to the Check file
    chk = Check(200, "04/28/2019", "1234", "4567", "8970")
    #print(chk)
    
    # Calls the CreditCard file
    ccard = CreditCard(300, "04/30/2019", "VISA", "1111-2222-3333-4444", "12/22", "123")
    print(ccard)
    
    # Calls the Business file
    bus = Business("ACME", "Jan")
    bus.add_payment(pay)
    bus.add_payment(chk)
    bus.add_payment(ccard)
    bus.print_payments()
    
main()


