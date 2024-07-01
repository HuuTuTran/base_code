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
def changePwd(oldPass,rePass, newPass):
	oldP = oldPass.get()
	reP = rePass.get()
	newP = newPass.get()
	if not oldP or not reP or not newP: 
		ctypes.windll.user32.MessageBoxW(0, "Please fill all the field", "Alert", 0)
	elif oldP != reP:
		ctypes.windll.user32.MessageBoxW(0, "Please re-type your password correctly", "Alert", 0)
	else:
		current_id = readFile()
		mycursor = mydb.cursor()
		mycursor.execute(f"SELECT * FROM users where id='{current_id}' and pwd ='{oldP}'")
		myresult = mycursor.fetchall()
		if len(myresult) > 0:
			if len(newP) < 10:
				ctypes.windll.user32.MessageBoxW(0, "Your password is too weak,please enter at least 10 characters", "Alert", 0)
			else:
				mycursor = mydb.cursor()
				sql = f"UPDATE users SET pwd = '{newP}' WHERE id = '{current_id}'"
				mycursor.execute(sql)
				mydb.commit()
				ctypes.windll.user32.MessageBoxW(0, "Your password has been successfully updated", "Alert", 0)
				tkWindow.destroy()
				os.system("python main.py")
		else:
			ctypes.windll.user32.MessageBoxW(0, "Invalid credential,Please try again", "Alert", 0)
		return
def readFile():
	f = open("infor.txt", "r")
	rsl = f.read(1)
	f.close()
	return rsl
def Back():
	tkWindow.destroy()
	os.system("python main.py")

tkWindow = Tk()  
tkWindow.geometry('300x150')  
tkWindow.title('Change password Form')

#username label and text entry box
Label1 = Label(tkWindow, text="Your old password:").grid(row=0, column=0)
oldP = StringVar()
oldPassEntry = Entry(tkWindow, textvariable=oldP, show='*').grid(row=0, column=1)  

#password label and password entry box
Label2 = Label(tkWindow,text="Repeat your password:").grid(row=1, column=0)  
rePass = StringVar()
rePassEntry = Entry(tkWindow, textvariable=rePass, show='*').grid(row=1, column=1)  

Label3 = Label(tkWindow,text="Your new password:").grid(row=2, column=0)  
newP = StringVar()
newPassEntry = Entry(tkWindow, textvariable=newP, show='*').grid(row=2, column=1)  

changePwd = partial(changePwd, oldP, rePass,newP)

#login button
ChangeButton = Button(tkWindow, text="Confirm", command=changePwd).grid(row=4, column=0)  
Backbtn = Button(tkWindow, text="Back", command=Back).grid(row=4, column=1)  

tkWindow.mainloop()