from lesson.employee import Employee, Developer, Lead

# your code here
#---------------------------------------------------------------

#create class
class Payroll:

    #init function
    def __init__(self, company_name):
        self.company_name = company_name
        self.employee_list = []

    #add_employee method
    def add_employee(self, employee):
        self.employee_list.append(employee)

    #get_payroll method
    def get_payroll(self):
        for employee in self.employee_list:
            print("Name: "+employee.name+" | Salary: "+ str(employee.payment(80)))



# ---------------------------------------------------------------



payroll = Payroll("Code Works")

payroll.add_employee(Employee('John', 20))
payroll.add_employee(Developer('Jane', 22))
payroll.add_employee(Lead('Molly', 25))

payroll.get_payroll()
