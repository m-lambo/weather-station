import mariadb
from mariadb import Error
import sys


def establish_connection():
    try:
        connection = mariadb.connect(
        host = 'localhost',
        user = 'mitchellsPi',
        password = 'winter06',
        )
        return connection
    except Error as e:
        print(f"Error connected to MariaDB Platform: {e}")
        sys.exit(1)
        
def setCursor(connection):
    cursor = connection.cursor()
    return cursor

