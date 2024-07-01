from tkinter import *
import tkinter
from datetime import date
import mysql.connector
import os
import ctypes 
class Table:
    def __init__(self,pname='',Winner='',isDraw = False):
        self.main_window = tkinter.Tk()
        f = open("infor.txt", "r")
        rsl = f.read(1)
        f.close()
        mycursor = mydb.cursor()
        mycursor.execute(f"SELECT * FROM users where id={rsl} ")
        myresult = mycursor.fetchall()
        _name = str(list(myresult[0])[1]) 
        today = date.today()
        lst =[("Time",'Player 1','Player 2','Winner')]
        if isDraw:
            lst.append((today,_name,pname,'Draw'))
        else:
            if Winner=='X':
                lst.append((today,_name,pname,_name))                   
            elif Winner=='O' :
                lst.append((today,_name,pname,pname))                             
        total_rows = len(lst)
        total_columns = len(lst[0])
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(self.main_window, width=10, font=('fixedsys', 15), bg='lightpink')
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
        PlayButton = Button(self.main_window, text="Play Again",command=self.Play, width=10, font=('fixedsys', 15), bg='lightpink').grid(row=4, column=1)  
        ExitButton = Button(self.main_window, text="Exit",command=self.Exit, width=10, font=('fixedsys', 15), bg='lightpink').grid(row=4, column=2) 
        tkinter.mainloop()
    def Play(self):
        self.main_window.destroy()
        os.system("python Test.py")
    def Exit(self):
        self.main_window.destroy()
        os.system("python main.py")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="tiktactoedb"
)




# t = Table()
