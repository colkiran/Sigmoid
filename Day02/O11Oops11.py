
class Employee:

    def __init__(self, name):
        self.__name = name              # private variable
        self.tech =  self.tech = ['C++', 'Java', 'Spring', 'Hibernate', 'Angular JS', 'React JS', 'Ext JS']

    def __str__(self):
        return self.__name + " -- " + " ".join([str(st) for st in self.tech])

emp1 = Employee("Danny")
print(emp1)

print("-" * 60)
print(emp1.__dict__)

print(emp1._Employee__name)

emp1._Employee__name = "Micheal"

print("-" * 60)
print(emp1)


