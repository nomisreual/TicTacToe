# Tic-Tac-Toe
# by Simon Lauer
#

import elements as el
import random

def main():
    board = el.Board()
    print("Welcome to Tic-Tac-Toe")
    print("Player 1, what is your name?")
    name1 = input()
    player1 = el.Player(name1, id = 1)
    print("Player 2, what is your name?")
    name2 = input()
    player2 = el.Player(name2, id = -1)
    print("Who plays first?")
    print(
    f"""
1. {name1}, enter 1
2. {name2}, enter 2
3. random, enter 3     
    """
    )
    while True:
        first = input()
        if first in ("1", "2", "3"):
            break
        else:
            print("Not a valid option. Try again.")
    if first == "1":
        first_player = player1
        second_player = player2
    elif first == "2":
        first_player = player2
        second_player = player1
    else:
        ran = random.randint(1, 2)
        if ran == 1:
            first_player = player1
            second_player = player2
        else:
            first_player = player2
            second_player = player1
    
    won = False

    while True:
        board.display()
        print(f"Make a move, {first_player.name}:")    
        while True:
            row, col, id = first_player.makeMove()
            if board.board[row][col].value is None:
                board.set_field(row, col, id)
                won = board.hasWon(row, col)
                break
            else:
                print("Not a valid move")
        if won:
            board.display()
            print(f"{first_player.name} has won!")
            break

        board.display()
        print(f"Make a move, {second_player.name}:")
        while True:
            row, col, id = second_player.makeMove()
            if board.board[row][col].value is None:
                board.set_field(row, col, id)
                won = board.hasWon(row, col)
                break
            else:
                print("Not a valid move")
        if won:
            board.display()
            print(f"{second_player.name} has won!")
            break

if __name__ == "__main__":
    main()
