class Atm(object):
    def __init__(self,cardNumber=None, pinNumber=None):
        self.cardNumber = {}
        self.pinNumber = {}
    
    def CashWithdrawl(self):
        print("How much cash would you like to withdraw? Please type out below.")

    def BalanceEnquiry(self):
        print("Enter you Card Number as well as the Pin Number here. Note: The process is entirely secured :)")

    def PayBills(self):
        int(input("Please enter the number on which you want the pay the bill to - "))