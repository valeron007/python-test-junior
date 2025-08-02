import psycopg2
from config import load_config

def create_table(conn):
    table_sql = """
        CREATE TABLE IF NOT EXISTS employees (
            id              Serial PRIMARY KEY,
            name            varchar(80) UNIQUE,
            position        varchar(100),
            salary          numeric(10, 2)
        );    
    """
        
    cur.execute(table_sql)                
    
def create_records(conn):
    record_sql = """
        INSERT INTO employees (name, position, salary)
        VALUES 
        ('John', 'manager', 120000),
        ('Valeron', 'programmist', 150000),
        ('Semen', 'director', 200000),
        ('Иван', 'operator', 40000),
        ('Анна', 'operator', 30000)
    """
    
    cur.execute(record_sql)                

def truncate_table(conn, name):
    clear_sql = "truncate {0}".format(name)
    
    cur.execute(clear_sql)

def get_employess(conn, salary = 50000):
    employyes_sql = "select * from employees where salary > {0};".format(salary)
        
    cur.execute(employyes_sql)                
    employees = cur.fetchall()
    print(employees)    

def delete_record(conn, name):    
    delete_sql = "delete from employees where name='{0}';".format(name)
    
    cur.execute(delete_sql)                

def update_salary(conn, name, salary):
    update_sql = "UPDATE employees SET salary = {0} where name = '{1}';".format(salary, name)
    
    cur.execute(update_sql)                    

try:    
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:            
            create_table(conn=conn)        
            truncate_table(conn, 'employees')
            create_records(conn=conn)        
            delete_record(conn=conn, name="Анна")
            get_employess(conn=conn, salary=10000)
            update_salary(conn=conn, name="Иван", salary=60000)   
            get_employess(conn=conn, salary=10000)
except (psycopg2.DatabaseError, Exception) as error:
    print(error)

