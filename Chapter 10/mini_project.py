"""
Create a program that allows adding, viewing, and 
deleting employee details using OOP principles.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def view_employee(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}\n")

class EmployeeManager:

    employees = []

    def __init__(self):
        self.operation()

    def operation(self):
        print("\n1. Add employee\n2. View all employees\n3. Delete an employee\n")
        user_operation = int(input("Select operation: "))
        if user_operation == 1:
            self.add_employee()
        elif user_operation == 2:
            self.view_employees()
        elif user_operation == 3:
            self.delete_employee()

    def add_employee(self):
        name = input("Enter employee name: ")
        age = input("Enter employee age: ")
        employee_id = int(input("Enter employee ID: "))
    
        # create a new employee instance/object
        new_employee = Employee(name, age, employee_id)
        # save the created employee to list
        self.employees.append(new_employee)

        self.operation()

    def view_employees(self):
        for employee in self.employees:
            employee.view_employee()

        self.operation()

    def delete_employee(self):
        employee_id = int(input("Enter employee ID to be deleted: "))
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)

        self.operation()

manager = EmployeeManager()