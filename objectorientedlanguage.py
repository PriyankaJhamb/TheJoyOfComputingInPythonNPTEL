class Employee:
    increment = 1.5
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    def increase(self):
        self.salary=self.salary * Employee.increment

harry = Employee("harry","Singh", 440000)
rohan = Employee("rohan", "das" , 450000)

print(harry.fname, rohan.lname)
print(harry.salary)
harry.increase();
print(harry.salary)
print(Employee.__dict__)
print(harry.__dict__)
print(rohan.__dict__)



class employee:
    pass

