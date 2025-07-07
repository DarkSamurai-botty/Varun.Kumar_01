def generate_payslip():
    print("=== Varun & Co Payslip Generator ===\n")

    full_name = input("Enter employee full name: ")
    month_year = input("Enter month and year (e.g., July 2025): ")
    days_worked = int(input("Enter number of days worked (e.g., 25): "))
    total_days = int(input("Enter total days in the month (e.g., 30): "))
    emp_id = input("Enter employee ID: ")

    monthly_salary = 3000
    daily_salary = monthly_salary / total_days
    salary_earned = daily_salary * days_worked

    print("\n" + "="*30)
    print("        PAYSLIP")
    print("="*30)
    print(f"Employee Name : {full_name}")
    print(f"Employee ID   : {emp_id}")
    print(f"Month & Year  : {month_year}")
    print(f"Days Worked   : {days_worked} / {total_days}")
    print(f"Monthly Salary: ${monthly_salary:.2f}")
    print(f"Salary Earned : ${salary_earned:.2f}")
    print("="*30)
    print("Thank you for your hard work!")
    print("="*30)

generate_payslip()
