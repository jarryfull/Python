import mysql.connector

conn = mysql.connector.connect(user='jaimeale', 
                               password='Jaimeale123!',
                               host='127.0.0.1',
                               database='angular')
cursor = conn.cursor()

query = ("SELECT * FROM angular.user")

data = cursor.execute(query)
for data in cursor:
    print(data)

conn.close()
