import os
from random import randint

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def create_board():
    board = [[" "  for i in range(0, 3)] for j in range(0, 3)]
    return(board)

def print_board(board):
    clear()
    for row in board: 
        print(f"{row[0]} | {row[1]} | {row[2]}")

def player(board, row, column, n):
    if n == 0:
        board[row][column] = "x"
    else:
        board[row][column] = "o"
    
def verify(board, row, column):
    if row <= 2 and column <= 2 and board[row][column]  == " ":
        return True
    else:
        return False

def verify_winning(board):
    for player in ["x", "o"]:
        for i in range(3):
            if (board[i][0] == board[i][1] == board[i][2] == player or
                board[0][i] == board[1][i] == board[2][i] == player):
                return True

            if (board[0][0] == board[1][1] == board[2][2] == player or
                board[0][2] == board[1][1] == board[2][0] == player):
                return True

    return False
    
def winner(player):
    print(f"\n{player} won!")

def random():
    return randint(0, 2)

def someone(board):
    while not verify_winning(board):
        print_board(board)

        print("\nPlayer I\n")
        row = int(input("Row: "))
        column = int(input("Column: "))

        while not verify(board, row, column):
            print("\nInvalid place! Try again.")
            row = int(input("Row: "))
            column = int(input("Column: "))

        player(board, row, column, 0)
        win = "Player I"
        if verify_winning(board):
            break

        print_board(board)

        print("\nPlayer II\n")
        row = int(input("Row: "))
        column = int(input("Column: "))
        
        while not verify(board, row, column):
            print("\nInvalid place! Try again.")
            row = int(input("Row: "))
            column = int(input("Column: "))
        
        player(board, row, column, 1)
        win = "Player II"

    print_board(board)
    winner(win)

def machine(board):
    while not verify_winning(board):
        print_board(board)

        print("\nPlayer I\n")
        row = int(input("Row: "))
        column = int(input("Column: "))

        while not verify(board, row, column):
            print("\nInvalid place! Try again.")
            row = int(input("Row: "))
            column = int(input("Column: "))

        player(board, row, column, 0)
        win = "Player I"
        if verify_winning(board):
            break

        print_board(board)

        print("\nMachine\n")
        row = random()
        column = random()
        
        while not verify(board, row, column):
            row = random()
            column = random()
        
        
        player(board, row, column, 1)
        win = "Machine"

    print_board(board)
    winner(win)

def main():
    clear()
    board = create_board()
    print("=" * 50)
    print(f"{"Tic Tac Toe":^50}")
    print("=" * 50, "\n" * 2)
    print("How do you want to play?")
    c = int(input("[0] Against someone\n[1] Against the machine\n\nYour choice: "))
    if c == 0:
        someone(board)
    elif c == 1:
        machine(board)
    else:
        print("\nInvalid Option")

if __name__ == "__main__": 
    main()