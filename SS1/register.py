from tkinter import *
import ctypes    
import os
from functools import partial
import mysql.connector
from PIL import Image, ImageTk

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="tiktactoedb"
)
def Register(username, password,img):
	usn = username.get()
	pwd = password.get()
	img = str(img.get())
	if not usn or not pwd :
		print("Please fill all the field")
		ctypes.windll.user32.MessageBoxW(0, "Please fill all the field", "Alert", 0)
	else:
		mycursor = mydb.cursor()
		mycursor.execute(f"SELECT * FROM users where usn='{usn}'")
		myresult = mycursor.fetchall()
		if len(myresult) > 0:
			ctypes.windll.user32.MessageBoxW(0, "This username has arealdy been taken", "Alert", 0)
		else:
			if len(pwd) < 10:
				ctypes.windll.user32.MessageBoxW(0, "Your password is too weak,at least 10 characters", "Alert", 0)
			else:
				mycursor = mydb.cursor()
				sql = "INSERT INTO users (usn, pwd,img) VALUES (%s, %s,%s)"
				val = (usn, pwd,img)
				mycursor.execute(sql, val)
				mydb.commit()
				ctypes.windll.user32.MessageBoxW(0, "You have Registered successfully", "Alert", 0)
				tkWindow.destroy()
				os.system("python login.py")

def Back():
	tkWindow.destroy()
	os.system("python login.py")
	return
#window
tkWindow = Tk()  
tkWindow.geometry('500x300')  
tkWindow.title('Register Form')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

var = StringVar()
R1 = Radiobutton(tkWindow, text="Option 1", variable=var, value="img/images.png").grid(row=2, column=0)  
image1 = Image.open("img/images.png").resize((60,50), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = Label(image=test).grid(row=2, column=1)

R2 = Radiobutton(tkWindow, text="Option 2", variable=var, value="img/0e517eb57cb5a992ef3230b0e0d792af.jpg").grid(row=3, column=0)  
image2 = Image.open("img/0e517eb57cb5a992ef3230b0e0d792af.jpg").resize((60,50), Image.ANTIALIAS)
test2 = ImageTk.PhotoImage(image2)
label2 = Label(image=test2).grid(row=3, column=1)

R3 = Radiobutton(tkWindow, text="Option 3", variable=var, value="img/profile_picture.png").grid(row=4, column=0)  
image3 = Image.open("img/profile_picture.png").resize((60,50), Image.ANTIALIAS)
test3 = ImageTk.PhotoImage(image3)
label3 = Label(image=test3).grid(row=4, column=1) 

R4 = Radiobutton(tkWindow, text="Option 4", variable=var, value="img/images.jpg").grid(row=2, column=2)  
image4 = Image.open("img/images.jpg").resize((60,50), Image.ANTIALIAS)
test4 = ImageTk.PhotoImage(image4)
label4 = Label(image=test4).grid(row=2, column=3) 

R5 = Radiobutton(tkWindow, text="Option 5", variable=var, value="img/game_face-01_4x.png").grid(row=3, column=2)  
image5 = Image.open("img/game_face-01_4x.png").resize((60,50), Image.ANTIALIAS)
test5 = ImageTk.PhotoImage(image5)
label5 = Label(image=test5).grid(row=3, column=3) 

R6 = Radiobutton(tkWindow, text="Option 6", variable=var, value="img/images1.jpg").grid(row=4, column=2)  
image6 = Image.open("img/images1.jpg").resize((60,50), Image.ANTIALIAS)
test6 = ImageTk.PhotoImage(image6)
label6 = Label(image=test6).grid(row=4, column=3) 

Register = partial(Register, username, password,var)
#login button
Submitbtn = Button(tkWindow, text="Register", command=Register).grid(row=7, column=0)  
Backbtn = Button(tkWindow, text="Back", command=Back).grid(row=7, column=2)  

tkWindow.mainloop()