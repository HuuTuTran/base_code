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
def update(img,id):
	img = str(img.get())
	if not img:
		ctypes.windll.user32.MessageBoxW(0, "Please choose a photo below", "Alert", 0) 
		return
	mycursor = mydb.cursor()
	sql = f"UPDATE users SET img = '{img}' WHERE id = '{id}'"
	mycursor.execute(sql)
	mydb.commit()
	ctypes.windll.user32.MessageBoxW(0, "Success", "Alert", 0)
	tkWindow.destroy()
	os.system("python main.py")
def getImg(id):
	if id:
		mycursor = mydb.cursor()
		mycursor.execute(f"SELECT * FROM users where id={id} ")
		myresult = mycursor.fetchall()
		return str(list(myresult[0])[3])
	else:
		return False 
def Back():
	tkWindow.destroy()
	os.system("python main.py")
	
#window
tkWindow = Tk()  
tkWindow.geometry('400x300')  
tkWindow.title('Change profile picture Form')

var = StringVar()

f = open("infor.txt", "r")
rsl = f.read(1)
f.close()
if rsl:
	usernameLabel = Label(tkWindow, text="Your current photo").grid(row=0, column=0)
	image0 = Image.open(getImg(rsl)).resize((120,100), Image.ANTIALIAS)
	test0 = ImageTk.PhotoImage(image0)
	label0 = Label(image=test0).grid(row=0, column=2)
else:
	tkWindow.destroy()
	os.system("python login.py")


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

update = partial(update,var,rsl)
#login button
Submitbtn = Button(tkWindow, text="Update", command=update).grid(row=7, column=1)  
Backbtn = Button(tkWindow, text="Back", command=Back).grid(row=7, column=2)  

tkWindow.mainloop()