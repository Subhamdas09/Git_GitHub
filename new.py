class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    def ShowDetails(self):
        print("role =", self.role)
        print("department =", self.department)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name= name
        self.age= age
        super().__init__("Engineer","IT","75,000")

eng1 = Engineer("Subham das", "23")
eng1.ShowDetails()