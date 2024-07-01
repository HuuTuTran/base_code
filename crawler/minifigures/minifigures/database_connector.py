import mysql.connector

class db_connector():
    # Database connection details
    def __init__(self) :
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mini_data"
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

        sql = f"INSERT INTO {table_name} (`name`, `SKU`, `cates`,`tag`,`price`,`img_url`) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (obj['name'], obj['SKU'], obj['cates'], obj['tag'], obj['price'], obj['img_url'])
        mycursor.execute(sql, data)
        self.mydb.commit()
        mycursor.close()
        self.mydb.close()
      
