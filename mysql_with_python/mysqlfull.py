import mysql.connector

mydb = mysql.connector.connect(
    user="root",
    host="127.0.0.1",
    passwd="123456123",
    database="Employees",
)

mycursor = mydb.cursor()
#-----creating a database------
mycursor.execute("CREATE DATABASE Employees")
#------checking if the database is created-------
mycursor.execute("SHOW DATABASES")
for db in mycursor:
     print(db)
#-------to create table------------
mycursor.execute("CREATE TABLE Employees (Name VARCHAR(50),Age INTEGER(2),EmID VARCHAR(5)) ")
#--------to check table-----------
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)
#---------to enter values of the employees-----------
employees = [("Vikyath",10,"56"),
             ("Manoj",8,"08"),
             ("Harshitha",14,"14"),
             ("Shourie",14,"87")]
Formula = "INSERT INTO Employees (Name,Age,EmID) VALUES (%s,%s,%s)"
mycursor.executemany(Formula,employees)
mydb.commit()
#----------to search all values-----------
mycursor.execute("SELECT * FROM employees")
values = mycursor.fetchall()
for row in values:
    print(row)
#-------to search 1st value-------
mycursor.execute("SELECT * FROM employees")
value1 = mycursor.fetchone()
print(value1)
#--------to pick specific data using where command---------
sql = "SELECT * FROM employees WHERE name = '%s'"
mycursor.execute(sql,('Manoj'))
reqage = mycursor.fetchall()
for result in reqage:
    print(result)
#-------LIKE command------
sql1 = "SELECT * FROM employees WHERE name LIKE %s"
mycursor.execute(sql1,('%j',))
nameend = mycursor.fetchall()
for name in nameend:
    print(name)
#-------updating values--------
update = "UPDATE employees SET age = 12 WHERE name = 'Vikyath' "
mycursor.execute(update)
mydb.commit()
#--------limiting values for display------------
limit = "SELECT * FROM employees LIMIT %s"
mycursor.execute(limit,(2,))
result = mycursor.fetchall()
for lm in result:
    print(lm)
#--------to display from specific data---------
datastart = "SELECT * FROM employees LIMIT %s OFFSET %s"
mycursor.execute(datastart,(2,1,))
result1 = mycursor.fetchall()
for res in result1:
    print(res)
#-------ordering of data(for descending order use key work DESC)---------
sql2 = "SELECT * FROM employees ORDER BY name DESC"
mycursor.execute(sql2)
ascen = mycursor.fetchall()
for asc in ascen:
    print(asc)
#-------how to delete a record in database-------
delete = "DELETE FROM employees WHERE name = %s AND age = %s"
mycursor.execute(delete,('Harshitha','14'))
mydb.commit()
rems = "SELECT * FROM employees "
mycursor.execute(rems)
rem = mycursor.fetchall()
for r in rem :
    print(r)
#--------deleting a table-----------
delete_table = "DROP TABLE IF EXISTS employees"
mycursor.execute(delete_table)