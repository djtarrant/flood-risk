# python -m pip install mysql-connector
import mysql.connector as conn
from mysql.connector import Error


dbConfig = {
    'host' : 'your-host',	
    'database' : 'your-database',
    'user' : 'your-user',	
    'password' : 'your-password'
}

myconnection = conn.connect(**dbConfig)
mycursor = myconnection.cursor()

#mycursor.execute("your sql;")