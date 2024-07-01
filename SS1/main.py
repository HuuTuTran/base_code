import os
from tkinter import *
import tkinter
from tkinter import messagebox
import mysql.connector
from playboard import TicTacToeApp, print_board
import csv
from PIL import Image, ImageTk

class Menu:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="tiktactoedb"
    )
    def __init__(self,_id):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('350x500')
        self.main_window.title('Tic-Tac-Toe (Noughts and Crosses)')
        self.main_window.configure(background='lavenderblush')

        self.icon_frame = tkinter.Frame(self.main_window)
        self.title_frame = tkinter.Frame(self.main_window)
        self.option_frame = tkinter.Frame(self.main_window)

        self.player1 = tkinter.StringVar()
        self.player2 = tkinter.StringVar()
        self.mainFrame_label = tkinter.Label(self.title_frame, text='TIC TAC TOE', font=('fixedsys', 40), bg='lightpink',
                                             fg='#ffffff')
        self.O_label = tkinter.Label(self.icon_frame, text='X   -', font=('Comic sans ms', 30), bg='whitesmoke',
                                     fg='pink')
        self.X_label = tkinter.Label(self.icon_frame, text='O', font=('Comic sans ms', 30), bg='whitesmoke', fg='lightpink')
        mycursor = self.mydb.cursor()
        mycursor.execute(f"SELECT * FROM users where id={_id} ")
        myresult = mycursor.fetchall()
        image0 = Image.open(str(list(myresult[0])[3])).resize((120,100), Image.ANTIALIAS)
        test0 = ImageTk.PhotoImage(image0)
        self.img_label = tkinter.Label(self.icon_frame, text="Hello,"+str(list(myresult[0])[1]), font=('lightpink', 20), bg='whitesmoke',
                                     fg='pink')
        self.label0 = tkinter.Label(self.title_frame,image=test0, bg='lightpink')

        self.opt1_btn = tkinter.Button(self.option_frame, text='Play GAME', font=('Comic sans ms', 12), width=14,
                                       bg='#ffffff', fg='black', relief='ridge', command=self.Play)
        self.opt2_btn = tkinter.Button(self.option_frame, text='Update Info', font=('Comic sans ms', 12), width=14,
                                       bg='#ffffff', fg='black', relief='ridge', command=self.UpdateInfo)
        self.opt3_btn = tkinter.Button(self.option_frame, text='Change password', font=('Comic sans ms', 12), width=14,
                                       bg='#ffffff', fg='black', relief='ridge', command=self.changepwd)
        self.opt4_btn = tkinter.Button(self.option_frame, text='Logout', font=('Comic sans ms', 12), width=14,
                                       bg='#ffffff', fg='black', relief='ridge', command=self.Logout)

        self.mainFrame_label.pack()
        self.label0.pack()
        self.img_label.pack()
        self.O_label.pack(side='left')
        self.X_label.pack(side='right')
        self.opt1_btn.pack()
        self.opt2_btn.pack()
        self.opt3_btn.pack()
        self.opt4_btn.pack()

        self.title_frame.pack(pady=8)
        self.icon_frame.pack(pady=15)
        self.option_frame.pack()

        tkinter.mainloop()

    def Play(self):
        self.main_window.destroy()
        os.system("python test.py")
        
    def changepwd(self):
        self.main_window.destroy()
        os.system("python changepwd.py")

    def UpdateInfo(self):
        self.main_window.destroy()
        os.system("python updateImage.py")

    def Logout(self):
        open('infor.txt', 'w').close()
        self.main_window.destroy()
        os.system("python login.py")


f = open("infor.txt", "r")
rsl = f.read(1)
f.close() 
if rsl:
    test = Menu(rsl)
else:
    os.system("python login.py")

