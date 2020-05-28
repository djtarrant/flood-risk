# python -m pip install mysql-connector
import mysql.connector


dbConfig = {
    'host' : 'your-host',	
    'database' : 'your-database',
    'user' : 'your-user',	
    'password' : 'your-password'
}

myconnection = mysql.connector.connect(**dbConfig)
mycursor = myconnection.cursor()

#mycursor.execute("your sql;")