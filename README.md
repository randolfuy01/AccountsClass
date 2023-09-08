# AccountsClass
This is illustrating my understanding of inheritance and classes in python. Using a simply class definitions and demonstrating it.
We have 2 classes, the Account class and the SavingsAccount class. 

The Account class is the parent class and it consists of class variables that are name, password, accountBalance, accountID, and accountRouter. 
  - I chose to have most of these variables protected so that only this clas and subclasses can access them, thus like in a real bank account you             wouldn't want everything being easily accessible. 
  - The initial configuration of the class is a constructor that takes in 3 arguments (2 technically because self is referencing the object) -> name and      pasword
  - We also want to have an accountRouter similar to what your bank's routing number is and an ID number that is assigned to every person when creating       an account with a respective bank.
  - We want to be able to change and transform these values so we have different functions suchas returnName, changeName, changePassword in order to do       so.
  - Since this is a bank acocunt we want to be able to withdraw, deposit money as well so we have functions for that as well.

The SavingsAccount class is a subclasses that inherits form the Account class. We want the same values we already have in the Account class but we would also like to add certain functionalities, similar to how a checking and a SavingsAccount would be different. 
  - The difference mainly lays with one thing, we want to be able to check for interest rate for 1 month, 1 year, and 5 years, so we create functions in      order to be able to do that for us. 
