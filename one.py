emp = {}

names = input('')
while True:
    
    employee_name = input("Enter employee name: ")
    
    if employee_name.lower() == 'no':
        break 
    employee_salary = float(input("Enter employee salary: "))
    emp[employee_name] = employee_salary