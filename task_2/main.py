from functools import reduce

def filter_employees(employees):
    employee_sal = list(filter(lambda employee: employee['salary'] > 50000, employees))
    employee_names = list(map(lambda employee: employee["name"], employee_sal))    
    average_salary = reduce(lambda a, b: a + b["salary"], employees, 0) / len(employees)
    employees.sort(reverse=True, key=lambda employee: employee["salary"])
        
    return (employee_names, average_salary, employees)

if __name__ == '__main__':    
    employees = [ 
        {"name": "Иван", "position": "разработчик", "salary": 55000}, 
        {"name": "Анна", "position": "аналитик", "salary": 48000}, 
        {"name": "Петр", "position": "тестировщик", "salary": 52000}, 
    ] 
    
    print(filter_employees(employees))    
    