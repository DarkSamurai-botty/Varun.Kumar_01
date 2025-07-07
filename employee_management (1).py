employees = {}

def add_employee():
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    position = input("Enter employee position: ")
    employees[emp_id] = {"name": name, "position": position}
    print("Employee added.\n")

def view_employees():
    if not employees:
        print("No employees to show.\n")
    else:
        print("=== Employee List ===")
        for emp_id, info in employees.items():
            print(f"ID: {emp_id}, Name: {info['name']}, Position: {info['position']}")
        print()

def delete_employee():
    emp_id = input("Enter employee ID to delete: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted.\n")
    else:
        print("EMPLOYEE NOT HERE BROTHER.\n")

def menu():
    while True:
        print("=== Employee Management Menu ===")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Delete Employee")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            delete_employee()
        elif choice == "4":
            print("CYA MAN!")
            break
        else:
            print("NOT WORKING BRO! TRY AGAIN!\n")

# Start the program
menu()
