class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

harry = Employee("harry","Singh", 440000)
rohan = Employee("rohan", "das" , 450000)

print(harry.fname, rohan.lname)
