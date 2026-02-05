#Employee Payroll System

class Employee():
    def __init__(self,emp_id,name):
        self.emp_id=emp_id
        self.name=name
    def calculate_salary(self,):
        raise NotImplementedError("Subclasses must implement this method")
class FullTimeEmployee(Employee):
    def __init__(self,emp_id,name,monthly_salary):
        super().__init__(emp_id,name)
        self.monthly_salary=monthly_salary
        
    def calculate_salary(self):
        return self.monthly_salary

class ContractEmployee(Employee):
    def __init__(self,emp_id,name,hourly_rate,hours_worked):
        super().__init__(emp_id,name)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked
    def calculate_salary(self):
        return self.hourly_rate*self.hours_worked

def process_payroll(employees):
    for emp in employees:
        salary = emp.calculate_salary()
        print(f"Employee: {emp.name}, Salary: {salary}")

emp1 = FullTimeEmployee(101, "Sampath", 60000)
emp2 = ContractEmployee(102, "Ravi", 500, 120)

employees = [emp1, emp2]
process_payroll(employees)


