class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    def display(self):
        print(f"Employee ID : {self.emp_id}")
        print(f"Name        : {self.name}")
        print(f"Department  : {self.department}")
        print(f"Salary      : ₹{self.salary}")
        print("-" * 30)


class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} hired successfully.")

    def fire(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                print(f"{employee.name} removed successfully.")
                return

        print("Employee not found.")

    def search(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee

        return None

    def give_bonus(self, percent):
        for employee in self.employees:
            employee.increase_salary(percent)

        print(f"Bonus of {percent}% given to all employees.")

    def display_all(self):
        print(f"\nCompany : {self.company_name}")
        print("=" * 30)

        if len(self.employees) == 0:
            print("No employees found.")
            return

        for employee in self.employees:
            employee.display()


# ---------------- Driver Code ----------------

e1 = Employee(101, "Aadhi", "Testing", 450000)
e2 = Employee(102, "Rahul", "Development", 700000)
e3 = Employee(103, "Priya", "HR", 550000)

company = Company("Google")

company.hire(e1)
company.hire(e2)
company.hire(e3)

company.display_all()

company.give_bonus(10)

company.display_all()

company.fire(102)

company.display_all()

result = company.search(101)

if result:
    print("\nEmployee Found")
    result.display()
else:
    print("Employee not found.")