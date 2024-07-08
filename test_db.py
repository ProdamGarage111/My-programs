import _sqlite3
connection = _sqlite3.connect("employee.db")
cursor = connection.cursor()
#cursor.execute("""
#CREATE TABLE employees (first_name text, last_name text, salary integer)
#""")
#cursor.execute(""" 
#INSERT INTO employees(first_name, last_name, salary) VALUES ('Ivan', 'Ivanov', '2')
#""")
cursor.execute("""
SELECT * FROM employees
""")
data = cursor.fetchall()
print(data)
connection.commit()
connection.close()
