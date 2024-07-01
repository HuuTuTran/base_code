import tkinter
from tkinter import messagebox
from playboard import TicTacToeApp, print_board
import csv
import os
class Menu:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('350x400+450+150')
        self.main_window.title('Tic-Tac-Toe (Noughts and Crosses)')
        self.main_window.configure(background='lavenderblush')

        self.icon_frame = tkinter.Frame(self.main_window)
        self.title_frame = tkinter.Frame(self.main_window)
        self.option_frame = tkinter.Frame(self.main_window)

        self.player1 = tkinter.StringVar()
        self.player2 = tkinter.StringVar()

        self.mainFrame_label = tkinter.Label(self.title_frame, text='TIC TAC TOE', font=('fixedsys', 40), bg='lightpink',
                                             fg='#ffffff')
        self.O_label = tkinter.Label(self.icon_frame, text='X - ', font=('Comic sans ms', 30), bg='whitesmoke',
                                     fg='pink')
        self.X_label = tkinter.Label(self.icon_frame, text='O', font=('Comic sans ms', 30), bg='whitesmoke', fg='lightpink')
        self.opt1_btn = tkinter.Button(self.option_frame, text='NEW GAME', font=('Comic sans ms', 12), width=14,
                                       bg='#ffffff', fg='black', relief='ridge', command=self.choose_mode)
        self.opt2_btn = tkinter.Button(self.option_frame, text='LEADER BOARD', font=('Comic sans ms', 12), width=14,
                                       bg='#ffffff', fg='black', relief='ridge', command=self.score_check)
        self.opt3_btn = tkinter.Button(self.option_frame, text='INSTRUCTION', font=('Comic sans ms', 12), width=14,
                                       bg='#ffffff', fg='black', relief='ridge', command=self.show_rules)
        self.opt4_btn = tkinter.Button(self.option_frame, text='EXIT', font=('Comic sans ms', 12), width=14,
                                       bg='#ffffff', fg='black', relief='ridge', command=self.exit)

        self.mainFrame_label.pack()
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
    def exit(self):
        self.main_window.destroy()
        os.system("python main.py")
    def show_rules(self):
        tkinter.messagebox.showinfo('Instruction',
                                    'The game starts on a 9x9 board. X go first, and each player draws their pieces on the empty field. The winner is the first person to have a continuous sequence of 4 horizontal, or vertical, or diagonal lines without any heads. If one is blocked, that person must have a sequence of 5 pieces to win. If the sequence of 5 pieces is blocked at both sides, the game continues. Once played, the pieces cannot be moved or removed from the table.')

    def choose_mode(self):
        def one_player_mode():
            self.player1_frame.pack()
            self.player2_frame.pack_forget()

        def two_player_mode():
            self.player1_frame.pack_forget()
            self.player2_frame.pack()

        self.extra_window = tkinter.Tk()
        self.extra_window.title('Choose Mode')
        self.extra_window.geometry('300x250+475+225')

        self.title = tkinter.Frame(self.extra_window)
        self.mode = tkinter.Frame(self.extra_window)
        self.player1_frame = tkinter.Frame(self.extra_window)
        self.player2_frame =tkinter.Frame(self.extra_window)
        self.start_cancel = tkinter.Frame(self.extra_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(0)
        self.title_label = tkinter.Label(self.title, text='HOW MANY PLAYERS DO YOU WANT TO PLAY:', font=('fixedsys', 11),
                                    bg='lightpink',fg='#ffffff')
        self.one_player = tkinter.Radiobutton(self.mode, text='One Player', font=('Comic sans ms', 15), variable=self.radio_var,
                                         value=1, command=one_player_mode,bg='lavenderblush')
        self.two_player = tkinter.Radiobutton(self.mode, text='Two Player', font=('Comic sans ms', 15), variable=self.radio_var,
                                         value=2, command=two_player_mode,bg='lavenderblush')
        self.player1 = tkinter.Label(self.player1_frame, text='Player1', textvariable=self.player1, width=20, bg='lavenderblush', fg='black')
        self.name1 = tkinter.Entry(self.player1_frame, width=15)
        self.player2 = tkinter.Label(self.player2_frame, text='Player2', textvariable=self.player2, width=20, bg='lavenderblush', fg='black')
        self.name2 = tkinter.Entry(self.player2_frame, width=15)
        self.start_btn = tkinter.Button(self.start_cancel, text='Start', width=10, relief='raised', command=self.play)
        self.cancel_btn = tkinter.Button(self.start_cancel, text='Main Menu', width=10, relief='raised',
                                    command=self.extra_window.destroy)

        self.title_label.pack()
        self.one_player.pack(side='left', pady=10, padx=10)
        self.two_player.pack(side='left', pady=10, padx=10)
        self.player1.pack(side='left')
        self.player2.pack(side='left')
        self.name1.pack(side='right')
        self.name2.pack(side='right')
        self.start_btn.pack(side='left', pady=10, padx=10)
        self.cancel_btn.pack(side='right', pady=10, padx=10)

        self.title.pack()
        self.mode.pack()
        self.start_cancel.pack()

        self.extra_window.mainloop()

    def play(self):
        self.player1 = self.name1.get()
        self.player2 = self.name2.get()
        if self.player1 != self.player2:
            print('ok')
            
            game_window = tkinter.Tk()
            test = TicTacToeApp(game_window,self.player2)

        else:
            tkinter.messagebox.showinfo('ERR','name')


    def score_check(self):
        self.extra_window = tkinter.Tk()
        self.extra_window.title('Leaderboard')
        self.extra_window.geometry('350x300+450+200')
        self.extra_window.configure(background='lavenderblush')

        self.player1 = self.name1.get()
        self.player2 = self.name2.get()

        print(self.player1)
        print(self.player2)

        self.cover_frame = tkinter.Frame(self.extra_window)
        self.title_frame = tkinter.Frame(self.cover_frame)
        self.table1 = tkinter.Frame(self.cover_frame)
        self.table2 = tkinter.Frame(self.cover_frame)
        self.table3 = tkinter.Frame(self.cover_frame)
        self.table4 = tkinter.Frame(self.cover_frame)
        self.table5 = tkinter.Frame(self.cover_frame)
        self.btn_frame = tkinter.Frame(self.cover_frame)
        self.test1 = self.player1
        self.test2 = self.player2

        self.title_label = tkinter.Label(self.title_frame, text='Leaderboard', width=30, height=2, anchor='w',
                                    font=('fixedsys', 20, 'bold'), fg='pink')
        self.title_tb1 = tkinter.Label(self.table1, text='RANK', font=('Comic sans ms', 10), width=10, anchor='w', bg='black',
                                  fg='#ffffff')
        self.title_tb2 = tkinter.Label(self.table1, text='NAME', font=('Comic sans ms', 10), width=15, anchor='w', bg='black',
                                  fg='#ffffff')
        self.title_tb3 = tkinter.Label(self.table1, text='WINS', font=('Comic sans ms', 10), width=10, anchor='w', bg='black',
                                  fg='#ffffff')
        self.player1 = tkinter.Label(self.table2, text='1', font=('Comic sans ms', 10), width=10, anchor='w', bg='gray',
                                fg='#ffffff')
        self.player1_name = tkinter.Label(self.table2, text= self.test1, font=('Comic sans ms', 10), width=15, anchor='w', bg='gray',
                                     fg='#ffffff')
        self.player1_win = tkinter.Label(self.table2, text='10', font=('Comic sans ms', 10), width=10, anchor='w', bg='gray',
                                    fg='#ffffff')
        self.player2 = tkinter.Label(self.table3, text='2', font=('Comic sans ms', 10), width=10, anchor='w', bg='gray',
                                fg='#ffffff')
        self.player2_name = tkinter.Label(self.table3, text= self.test2, font=('Comic sans ms', 10), width=15, anchor='w', bg='gray',
                                     fg='#ffffff')
        self.player2_win = tkinter.Label(self.table3, text='6', font=('Comic sans ms', 10), width=10, anchor='w', bg='gray',
                                    fg='#ffffff')
        self.player3 = tkinter.Label(self.table4, text='3', font=('Comic sans ms', 10), width=10, anchor='w', bg='gray',
                                fg='#ffffff')
        self.player3_name = tkinter.Label(self.table4, text='name2', font=('Comic sans ms', 10), width=15, anchor='w', bg='gray',
                                     fg='#ffffff')
        self.player3_win = tkinter.Label(self.table4, text='8', font=('Comic sans ms', 10), width=10, anchor='w', bg='gray',
                                    fg='#ffffff')
        self.player4 = tkinter.Label(self.table5, text='4', font=('Comic sans ms', 10), width=10, anchor='w', bg='gray',
                                fg='#ffffff')
        self.player4_name = tkinter.Label(self.table5, text='name2', font=('Comic sans ms', 10), width=15, anchor='w', bg='gray',
                                     fg='#ffffff')
        self.player4_win = tkinter.Label(self.table5, text='5', font=('Comic sans ms', 10), width=10, anchor='w', bg='gray',
                                    fg='#ffffff')
        self.back_btn = tkinter.Button(self.btn_frame, text='Main Menu', justify='center', command=self.extra_window.destroy)

        self.title_label.pack()
        self.title_tb1.pack(side='left')
        self.title_tb2.pack(side='left')
        self.title_tb3.pack(side='left')
        self.player1.pack(side='left')
        self.player1_name.pack(side='left')
        self.player1_win.pack(side='left')
        self.player2.pack(side='left')
        self.player2_name.pack(side='left')
        self.player2_win.pack(side='left')
        self.player3.pack(side='left')
        self.player3_name.pack(side='left')
        self.player3_win.pack(side='left')
        self.player4.pack(side='left')
        self.player4_name.pack(side='left')
        self.player4_win.pack(side='left')
        self.back_btn.pack(pady=30)

        self.cover_frame.pack(padx=20, pady=10)
        self.title_frame.pack()
        self.table1.pack(padx=10)
        self.table2.pack(padx=10)
        self.table3.pack(padx=10)
        self.table4.pack(padx=10)
        self.table5.pack(padx=10)
        self.btn_frame.pack()

        self.extra_window.mainloop()

    def loadScore(self):
        with open('test.csv', mode='w') as csvfile:
            fieldnames = ['Rank', 'Name', 'Wins']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'Rank': 1, 'Name': self.test1, 'Wins': 10})
            writer.writerow({'Rank': 2, 'Name': self.test2, 'Wins': 9})
            writer.writerow({'Rank': 3, 'Name': self.test1, 'Wins': 8})
            writer.writerow({'Rank': 4, 'Name': self.test2, 'Wins': 7})
        self.loadScore()


test = Menu()

