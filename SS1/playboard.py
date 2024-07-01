from tkinter import *
from tkinter import messagebox
import itertools
import ctypes    
from rsl import Table

SIZE = 9
board = [None] * (SIZE*SIZE)


class TicTacToeApp(Frame):
    def __init__(self, master=None,p2name=''):
        super().__init__(master)
        self.pack()
        self.players = itertools.cycle(['X', 'O'])
        self.player = next(self.players)
        self.p2name = p2name
        messagebox.showinfo('Game Over', p2name.format(self.player))
        self.create_board()

    def get_command_fn(self, button, row, col):
        def on_click():
            position = row * SIZE + col
            button['text'] = board[position] = self.player
            button.config(state=DISABLED)
            isDraw = False
            if has_won(board, self.player):
                messagebox.showinfo('Game Over', 'Player {} has won'.format(self.player))
                self.master.destroy()
                t = Table(self.p2name,self.player,isDraw)
            if is_draw(board):
                messagebox.showinfo('Game Over', 'Game Drawn')
                isDraw = True
                self.master.destroy()
                t = Table(self.p2name,self.player,isDraw)

            self.player = next(self.players)
        return on_click

    def create_board(self):
        for position in range(SIZE*SIZE):
            btn = Button(self, text=' ',bg="lavenderblush", fg="Black", width=1, height=1, font=('Helvetica', '15'))
            row = position // SIZE
            column = position % SIZE
            btn.grid(row=row, column=column)
            btn['command'] = self.get_command_fn(btn, row, column)
            btn.config(width=5, height=2)




def print_board(board):
    for index, cell in enumerate(board, start=1):
        print('{:^3}'.format(cell if cell else index), end='\n\n' if index % SIZE == 0 else ' ')

#
# def do_turn(board, player):
#     position = int(input('Player {}. Enter the position to play: '.format(player))) - 1
#     board[position] = player


def is_draw(board):
    return all(board[position] is not None for position in range(SIZE*SIZE))


def has_won(board, player):
    def has_combination(combination, symbol):
        return all(board [row*SIZE + col] == symbol for row, col in combination)

    winning_pattern = [
        lambda row, col: [(row-2, col), (row-1, col), (row, col), (row+1, col), (row+2, col)] if 1 < row < SIZE-2 else None,
        lambda row, col: [(row, col-2), (row, col-1), (row, col), (row, col+1), (row, col+2)] if 1 < col < SIZE-2 else None,
        lambda row, col: [(row-2, col-2), (row-1, col-1), (row, col), (row+1, col+1), (row+2, col+2)] if 1 < row < SIZE-2 and 1 < col < SIZE-2 else None,
        lambda row, col: [(row-2, col+2), (row-1, col+1), (row, col), (row+1, col-1), (row+2, col-2)] if 1 < row < SIZE-2 and 1 < col < SIZE-2 else None
    ]

    combinations = (pattern(position // SIZE, position % SIZE) for pattern in winning_pattern for position in range(SIZE*SIZE))
    return any(has_combination(combination, player) for combination in combinations if combination is not None)

if __name__ == '__main__':
    root = Tk()
    game = TicTacToeApp(master=root)
    game.mainloop()