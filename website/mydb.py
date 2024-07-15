import mysql.connector
dataBase = msql.connector(
    host = 'localhost',
    user = 'root',
    password = 'password123',
)
cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE customer")
print("All done!")
