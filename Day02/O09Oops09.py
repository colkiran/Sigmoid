"""
write a code to overload all arithmetic operators

1. addition
2. subtraction
3. multiplication
4. division
5. floor division

"""

class arithmetic:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary
    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary
    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary

emp1 = arithmetic("John", 35000)
emp2 = arithmetic("Richard",15000)

print("Addition :", emp1 + emp2)
print("Substraction:", emp1 - emp2)
print("Multiplication:", emp1 * emp2)
print("Division:", emp1 / emp2)
print("floor division", emp1 // emp2)
