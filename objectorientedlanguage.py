class Employee:
    increment = 1.5
    no_of_employees=0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees+=1

    def increase(self):
        self.salary=self.salary * Employee.increment
        # return self.salary

    @classmethod
    def change_increment(cls, amount):
        cls.increment=amount

    @classmethod #class method as an alternative constructor
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname,lname,salary)

    @staticmethod
    def isopen(day):
        if day=="SUNDAY":
            return False
        else:
            return True

#inheritance

class Programmer(Employee):
    def __init__(self, fname, lname, salary, progexp, proglang):
        super().__init__(fname, lname, salary)
        self.progexp=progexp
        self.proglang=proglang

# Hanit=Programmer("Hanit", "Kumar", 346756, "4 years", "Python")
# print(Hanit.salary)
# print(Hanit.increase())
# print(Hanit.progexp)
# print(help(Programmer))
# help(Programmer)

# print(Employee.isopen("MONDAY"))
# Priyanka=Employee.from_str("Priyanka-Jhamb-65900")
# print(Priyanka.fname,"\n",Priyanka.lname,"\n",Priyanka.salary)
# print(Employee.no_of_employees)
# harry = Employee("harry","Singh", 440000)
# print(Employee.no_of_employees)
# rohan = Employee("rohan", "das" , 450000)
# print(harry.no_of_employees)
# print(harry.fname, rohan.lname)
# print(harry.salary)
# Employee.change_increment(4)
# harry.increase();
# print(harry.salary)
# print(Employee.__dict__)
# print(harry.__dict__)
# print(rohan.__dict__)



class employee:
    pass

