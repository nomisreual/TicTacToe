import random
#from elements import Board, Player
from board import Board
from player import Player

class Game:
    def __init__(self):
        self.__board = Board()
        self.__player1 = Player(id = 1)
        self.__player2 = Player(id = -1)
        self.__first = None
        self.__second = None
        self.__won = False

    @property
    def board(self):
        return self.__board

    @property
    def player1(self):
        return self.__player1

    @property
    def player2(self):
        return self.__player2

    @property
    def first(self):
        return self.__first
    
    @first.setter
    def first(self, player):
        self.__first = player

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, player):
        self.__second = player

    @property
    def won(self):
        return self.__won
    
    @won.setter
    def won(self, hasWon):
        if isinstance(hasWon, bool):
            self.__won = hasWon

    def setUp(self):
        # Set player names:
        players = {1: self.player1, 2: self.player2}
        print("Welcome to Tic-Tac-Toe")
        for id, player in players.items():
            player.name = input(f"Player {id}, what is your name? ")
        # Who plays first?
        print("Who plays first?")
        print(
        f"""
        1. {self.player1.name}, enter 1
        2. {self.player2.name}, enter 2
        3. Random, enter 3     
        """
        )
        while True:
            first = input()
            if first in ("1", "2", "3"):
                if first == "1":
                    self.first = self.player1
                    self.second = self.player2
                    break
                elif first == "2":
                    self.first = self.player2
                    self.second = self.player1
                    break
                else:
                    ran = random.randint(1, 2)
                    if ran == 1:
                        self.first = self.player1
                        self.second = self.player2
                        break
                    else:
                        self.first = self.player2
                        self.second = self.player1
                        break
            else:
                print("Not a valid option. Try again.")
    def play(self):

        players = [self.first, self.second]
        playOn = True
        numMoves = 0

        while playOn:
            for player in players:
                self.board.display()

                print(f"Make a move, {player.name}:")    
                while True:
                    row, col, id = player.makeMove()
                    if self.board.board[row][col].value is None:
                        self.board.set_field(row, col, id)
                        won = self.board.hasWon(row, col)
                        break
                    else:
                        print("Not a valid move")
                numMoves += 1

                if won:
                    self.board.display()
                    print(f"{player.name} has won!")
                    playOn = False
                    break
                if numMoves == 9:
                    self.board.display()
                    print("It's a draw.")
                    playOn = False
                    break
            
    #def displayBoard(self):
    #    pass

    #def hasWon(self):
    #    pass

    #def setField(self):
    #    pass

