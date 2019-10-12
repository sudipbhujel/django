import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'letsmakecomplexsimple',
    database = 'linkedin_db'
)

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM comments')

for i,j,k,l,m in mycursor:
    print(j)