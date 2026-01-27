import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='MOULY@2005',
    database='Employee'
)

my_cursor = conn.cursor()
print("Connected with database")

def insert_employee():
    name = input("Enter name: ")
    dept = input("Enter department: ")
    salary = int(input("Enter salary: "))

    sql = "INSERT INTO employee (name, department, salary) VALUES (%s, %s, %s)"
    values = (name, dept, salary)

    my_cursor.execute(sql, values)
    conn.commit()
    print("Employee inserted")


def view_employee():
    my_cursor.execute("SELECT * FROM employee")
    result = my_cursor.fetchall()

    for row in result:
        print(row)


def update_employee():
    emp_id = int(input("Enter employee id: "))
    salary = int(input("Enter new salary: "))

    sql = "UPDATE employee SET salary=%s WHERE emp_id=%s"
    my_cursor.execute(sql, (salary, emp_id))
    conn.commit()
    print("Employee updated")


def delete_employee():
    emp_id = int(input("Enter employee id: "))

    sql = "DELETE FROM employee WHERE emp_id=%s"
    my_cursor.execute(sql, (emp_id,))
    conn.commit()
    print("Employee deleted")


while True:
    print("\n1.Insert")
    print("2.View")
    print("3.Update")
    print("4.Delete")
    print("5.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_employee()
    elif choice == 2:
        view_employee()
    elif choice == 3:
        update_employee()
    elif choice == 4:
        delete_employee()
    elif choice == 5:
        print("Program ended")
        break
    else:
        print("Invalid choice")


conn.close()
print("Database connection closed")
