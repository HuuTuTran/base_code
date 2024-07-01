from tkinter import *
import ctypes    
from functools import partial

import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="tiktactoedb"
)
# def get_hashed_password(plain_text_password):
# 	print()
#     return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())
def validateLogin(username, password):
	usn = username.get()
	pwd = password.get()
	if not usn or not pwd :
		ctypes.windll.user32.MessageBoxW(0, "Please fill all the field", "Alert", 0)
	else:
		mycursor = mydb.cursor()
		mycursor.execute(f"SELECT * FROM users where usn='{usn}' and pwd ='{pwd}'")
		myresult = mycursor.fetchall()
		if len(myresult) > 0:
			ctypes.windll.user32.MessageBoxW(0, f"Welcome {usn}", "Alert", 0)
			writeFile(str(list(myresult[0])[0]))
			#writeFile("this shit")
			tkWindow.destroy()
			os.system("python main.py")
		else:
			ctypes.windll.user32.MessageBoxW(0, "Invalid credential,Please try again", "Alert", 0)
		return

def register():
	tkWindow.destroy()
	os.system("python register.py")
	#return
def writeFile(content):
	file1 = open("infor.txt", "w")
	file1.writelines(content)
	file1.close()


tkWindow = Tk()  
tkWindow.geometry('300x100')  
tkWindow.title('Login Form')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name", font=('Comic sans ms', 10), width=10, anchor='w', bg='black',
                                  fg='#ffffff').grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username, width=25).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password", font=('Comic sans ms', 10), width=10, anchor='w', bg='black',
                                  fg='#ffffff').grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*', width=25).grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  
ResetPassButton = Button(tkWindow, text="Register", command=register).grid(row=4, column=1)  



f = open("infor.txt", "r")
rsl = f.read(1)
f.close() 
if rsl:
    os.system("python main.py")
else:
    tkWindow.mainloop()
