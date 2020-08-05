import mysql.connector
from mysql.connector import Error

def establish_connection(hostName, userName, userPassword):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostName,
            user = userName,
            passwd = userPassword
            )
        print("Connection to MySQL DB succesfully established")
    except Error as e:
        print(f"The error '{e}' occured")
        
    return connection

connection = establish_connection("localhost", "mitchellsPi", "winter06")