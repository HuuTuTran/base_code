import mysql.connector

class db_connector():
    # Database connection details
    def __init__(self) :
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="quotes_data"
        )
    


    def select(self,table_name):
        mycursor = self.mydb.cursor()
        mycursor.execute(f"SELECT * FROM {table_name}")
        myresult = mycursor.fetchall()
        mycursor.close()
        self.mydb.close()
        return myresult 
    def insert(self,table_name,obj):
        mycursor = self.mydb.cursor()

        sql = f"INSERT INTO {table_name} (`name`, `born_date`, `born_location`,`des`) VALUES (%s, %s, %s, %s)"
        data = (obj['name'], obj['born_date'], obj['born_location'], obj['description'])
        mycursor.execute(sql, data)
        self.mydb.commit()
        mycursor.close()
        self.mydb.close()
      
