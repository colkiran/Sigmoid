
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C++', 'Java', 'Spring', 'Hibernate', 'Angular JS', 'React JS', 'Ext JS']

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    def append(self, tech):
        self.tech.append(tech)


    def __iter__(self):
        # return self.tech.__iter__()
        return iter(self.tech)


    def __setitem__(self, index, value):
        self.tech[index] = value


    def __getitem__(self, index):
        return self.tech[index]



emp1 = Employee("Peter", 75000)
print(emp1)

print("-" * 60)

print([emp for emp in emp1])

print("-" * 60)

emp1.append("Python")

print([emp for emp in emp1])

print("-" * 60)

emp1[3] = "J2EE"

print([emp for emp in emp1])

print("-" * 60)

tech = emp1[-1]

print(tech)


