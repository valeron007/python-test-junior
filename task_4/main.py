import csv
import psycopg2
from config import load_config

def create_records_with_scv():    
    with open('employee.csv') as employee_file:
        reader = csv.reader(employee_file)
        next(reader)
        employees = ','.join(cur.mogrify("(%s,%s,%s)", i).decode('utf-8')
                    for i in reader)
        
        cur.execute("INSERT INTO employees (name, position, salary) VALUES " + (employees))
    
def search_position(position):
    sql = "select * from employees where position = '{0}';".format(position)
        
    cur.execute(sql)                
    employees = cur.fetchall()
    print(employees)    
    
def update_salary(name, salary):
    update_sql = "UPDATE employees SET salary = {0} where name = '{1}';".format(salary, name)
    
    cur.execute(update_sql)                    

if __name__ == '__main__':            
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:                                
                # create_records_with_scv()                
                # search_position("manager")
                update_salary("Valeron", 200000)
                
                
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
    
    
