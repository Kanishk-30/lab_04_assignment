class EmployeeTable:
    def __init__(self):
        self.data = [
            {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary": 56000},
            {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary": 67500},
            {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary": 82100},
            {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary": 55000},
            {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary": 44000},
        ]

    def search_by_age(self, age):
        results = [employee for employee in self.data if employee["Age"] == age]
        return results

    def search_by_name(self, name):
        results = [employee for employee in self.data if employee["Name"] == name]
        return results

    def search_by_salary(self, operator, salary):
        if operator == ">":
            results = [employee for employee in self.data if employee["Salary"] > salary]
        elif operator == "<":
            results = [employee for employee in self.data if employee["Salary"] < salary]
        elif operator == ">=":
            results = [employee for employee in self.data if employee["Salary"] >= salary]
        elif operator == "<=":
            results = [employee for employee in self.data if employee["Salary"] <= salary]
        else:
            results = []
        return results

    def print_results(self, results):
        if not results:
            print("No matching records found.")
        else:
            print("Matching records:")
            for employee in results:
                print(f"Employee ID: {employee['Employee ID']}")
                print(f"Name: {employee['Name']}")
                print(f"Age: {employee['Age']}")
                print(f"Salary: {employee['Salary']}")

def main():
    employee_table = EmployeeTable()

    print("Choose search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")
    choice = input("Enter your choice: ")

    if choice == "1":
        age = int(input("Enter age to search: "))
        results = employee_table.search_by_age(age)
    elif choice == "2":
        name = input("Enter name to search: ")
        results = employee_table.search_by_name(name)
    elif choice == "3":
        operator = input("Enter operator (> < <= >=): ")
        salary = int(input("Enter salary to search: "))
        results = employee_table.search_by_salary(operator, salary)
    else:
        print("Invalid choice")
        return

    employee_table.print_results(results)

if __name__ == "__main__":
    main()