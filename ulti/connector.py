import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="1234567",
database="information_schema",
port=3307
)

mycursor = mydb.cursor()

# Execute a query
mycursor.execute("select * from ADMINISTRABLE_ROLE_AUTHORIZATIONS;")

# Fetch results (if applicable)
myresult = mycursor.fetchall()
print(myresult)
# Close the connection
mycursor.close()
mydb.close()