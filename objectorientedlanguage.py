class Employee:
    increment = 1.5
    no_of_employees=0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees+=1

    @property
    def email(self):
        if self.fname==None and self.lname==None:
            return 'Email not set'
        else:
            return self.fname +'.'+ self.lname +'@gmail.com'

    @email.setter
    def email(self, given_email):
        name_list = given_email.split("@")[0].split(".")
        self.fname=name_list[0]
        self.lname=name_list[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None


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


    # Magic Functions (Dundar Methods)

    def __add__(self, other):
        return self.salary+other.salary

    def __repr__(self):
        return 'Employee({} {} {})'.format(self.fname,self.lname,self.salary)
    def __str__(self):
        return "The name of the Employee is {}".format(self.fname)

sonu=Employee("SOnu","Kakkar", 234235454)
print(sonu.email)
sonu.lname="Kaur"
print(sonu.email)
sonu.email="kakkar.sonu@gmail.com"
print(sonu.email)
del sonu.email
print(sonu.email)
# Neha=Employee("Neha","Kakkar", 23343235454)
# a=4
# print(a.__add__(34))
# print(sonu+Neha)
# print(repr(sonu))
# print(str(sonu))
# print(Neha)


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
# print(Employee.__dict__)#to know how may functions or methods are in this..class
# print(harry.__dict__)
# print(rohan.__dict__)



class employee:
    pass#it is the way to tell to the python interpreter that this will be defined later on and I know it so, don't show any error for this.

