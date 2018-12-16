import mysql.connector

conn = mysql.connector.connect(user='USERNAME', 
                               password='PASSWORD',
                               host='IP_SERVER_DB',
                               database='DATABASE')
cursor = conn.cursor()

query = ("SELECT * FROM user")

data = cursor.execute(query)
for data in cursor:
    print(data)

conn.close()
