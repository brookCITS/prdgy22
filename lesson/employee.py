class Employee:
    num_employee=0
    bonus=100.00
    def __init__(self, name, sal):
        self.name = name
        self.sal = sal
        self.email = name+"@company.com"
        Employee.num_employee += 1

    def payment (self, hours):
        return self.sal*hours + Employee.bonus

class Developer(Employee):

    #2 times the regular bonus
    def payment (self, hours):

        return self.sal*hours + 2*Employee.bonus

class Lead(Developer):

    #3 times the regular bonus
    def payment (self, hours):

        return self.sal*hours + 3*Employee.bonus
