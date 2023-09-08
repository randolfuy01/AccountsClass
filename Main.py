from Account import Account, SavingsAccount

Account1 = Account("Randolf", "NewPassword")
Account1.depositMoney(4000)
print(Account1._accountBalance)
print(Account1.withdrawMoney(5000))
Account1.changePassword("NewPassword")
print(Account1._password)

Account2 = SavingsAccount("Gabe", "NewPassword", 0.025)
Account2.depositMoney(10000)
print(Account2._accountBalance)
Account2.monthInterestRate()
print(Account2._accountBalance)
Account2.yearlyInterestRate()
print(Account2._accountBalance)
Account2.fiveYearGrowth()
print(Account2._accountBalance)