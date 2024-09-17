
from abc import  ABC, abstractmethod
class Employee(ABC):

    def doJob(self):
        pass


class Manager(Employee):

    def doJob(self):
        print("Mangers Job......")

class Developer(Employee):

    def doJob(self):
        print("Developers Job.......")

def BankJob(emp):
    print("Bank Job started......")
    emp.doJob()
    print("Bank Job ended......")
    print("-" * 60)

mike = Manager()
david = Developer()

BankJob(mike)       # managers job
BankJob(david)      # developers job