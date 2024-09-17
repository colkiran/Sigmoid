
from abc import ABC, abstractmethod

class Account(ABC):

    def withdraw(self):
        pass

    @abstractmethod
    def checkBalance(self):
        pass

class Savings(Account):

    def withdraw(self):
        print("Amount ##### debited from the account....")

    def checkBalance(self):
        print("Balace in the account is ######.##")

sav1 = Savings()
sav1.withdraw()
sav1.checkBalance()
