import string
import random



class Account:

    name = ""
    _password = ""
    _accountBalance = 0
    _accountID = 0
    _accountRouter = 0

    def __init__(self, name,password):
        self._name = name
        self._password = password
        self._accountBalance = 0
        self.__accountID = "".join(random.choices(string.ascii_uppercase +string.digits, k = 9))
        self.accountRouter = 12510165

    def returnName(self):
        return self._name

    def changeName(self, password):
        status = 0
        if (self.password != password):
            print("Unable to change name, wrong password")
        else:
            self._name = input(str("New name:"))
            status = 1
        
        return status
    
    def changePassword(self, password):
        status = 0
        if (self._password != password):
            return status
        else:
            self._password = input(str("New passowrd:"))
            status =1
        return status

    def withdrawMoney(self,amount):
        status = False
        if self._accountBalance >= amount:
            self._accountBalance =- amount
            status = True
        return status

    def depositMoney(self, amount):
        self._accountBalance += amount
        return True
    


class SavingsAccount(Account):
    interestRate = 0

    def __init__(self, name, password, interest):
        super().__init__(name, password)
        self.Yearlybonus = 0.05
        self.interestRate = interest

    def monthInterestRate(self):
        self._accountBalance += (self._accountBalance * self.interestRate)
    
    def yearlyInterestRate(self):
        for i in range(1, 12):
            self._accountBalance = self._accountBalance + (self._accountBalance * self.interestRate)
        self._accountBalance = self._accountBalance + (self._accountBalance * (self.interestRate + 1))
        print(self._accountBalance)
    
    def fiveYearGrowth(self):
        for i in range(1, 60):
            self._accountBalance = self._accountBalance + (self._accountBalance * self.interestRate)
    



    


