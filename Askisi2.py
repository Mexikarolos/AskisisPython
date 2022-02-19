# __Global Var__
import random

move = 0
sum = 0

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]


# 100 Games
for i in range(100):

 sum = sum + move

# Game Still Going
 game_still_going = True
# Move Reset
 move = 0
# Board Reset
 board = ["_", "_", "_",
          "_", "_", "_",
          "_", "_", "_"]


 def display_board():
     print(board[0] + " | " + board[1] + " | " + board[2])
     print(board[3] + " | " + board[4] + " | " + board[5])
     print(board[6] + " | " + board[7] + " | " + board[8])


 def play_game():
         display_board()

         while game_still_going:
             handle_turn()

             check_if_game_over()


 def handle_turn():
     print("Position Given:")
     # Chooses Random Board Position
     position = random.randint(0, 8)
     print(position)
     if board[position] == "_":

         kapakia = ['1', '2', '3']
         print("Kapaki Size: ")
         # If Board Position Blank, Chooses Random Kapaki Size
         board[position] = random.choice(kapakia)
         print(board[position])
         moves()
         display_board()

     elif board[position] == '1':
         print("Kapaki Size: ")
         kapakia1 = ['2', '3']
         # If Board Position Already Has A Small Kapaki Size, Adds A Random Bigger One
         board[position] = random.choice(kapakia1)
         print(board[position])
         moves()
         display_board()

     elif board[position] == '2':
         print("Kapaki Size: ")
         # If Board Position Already Has A Medium Sized Kapaki, Adds The Large One
         board[position] = '3'
         print(board[position])
         moves()
         display_board()

     elif board[position] == '3':
         print("Kapaki Size: ")
         print(board[position])
         display_board()


 def check_if_game_over():
     check_if_win()


 def check_if_win():
     check_rows()

     check_columns()

     check_diagonals()

     return


 def check_rows():
     # Set Up Global Variables
     global game_still_going
     # Check Rows
     row_1 = board[0] == board[1] == board[2] != "_"
     row_2 = board[3] == board[4] == board[5] != "_"
     row_3 = board[6] == board[7] == board[8] != "_"
     if row_1 or row_2 or row_3:
         game_still_going = False
     elif board[0] == '1' and board[1] == '2' and board[2] == '3':
         game_still_going = False
     elif board[3] == '1' and board[2] == '2' and board[1] == '3':
         game_still_going = False
     elif board[3] == '1' and board[4] == '2' and board[5] == '3':
         game_still_going = False
     elif board[5] == '1' and board[4] == '2' and board[3] == '3':
         game_still_going = False
     elif board[0] == '1' and board[1] == '2' and board[2] == '3':
         game_still_going = False
     elif board[3] == '1' and board[2] == '2' and board[1] == '3':
         game_still_going = False

     return


 def check_columns():
     # Set Up Global Variables
     global game_still_going
     # Check Columns
     col_1 = board[0] == board[3] == board[6] != "_"
     col_2 = board[1] == board[4] == board[7] != "_"
     col_3 = board[2] == board[5] == board[8] != "_"
     if col_1 or col_2 or col_3:
         game_still_going = False
     elif board[0] == '1' and board[3] == '2' and board[6] == '3':
         game_still_going = False
     elif board[6] == '1' and board[3] == '2' and board[0] == '3':
         game_still_going = False
     elif board[1] == '1' and board[4] == '2' and board[7] == '3':
         game_still_going = False
     elif board[7] == '1' and board[4] == '2' and board[1] == '3':
         game_still_going = False
     elif board[2] == '1' and board[5] == '2' and board[8] == '3':
         game_still_going = False
     elif board[8] == '1' and board[5] == '2' and board[2] == '3':
         game_still_going = False

     return


 def check_diagonals():
     # Set Up Global Variables
     global game_still_going
     # Check Columns
     diag_1 = board[0] == board[4] == board[8] != "_"
     diag_2 = board[6] == board[4] == board[2] != "_"

     if diag_1 or diag_2:
         game_still_going = False
     elif board[0] == '1' and board[4] == '2' and board[8] == '3':
         game_still_going = False
     elif board[8] == '1' and board[4] == '2' and board[0] == '3':
         game_still_going = False
     elif board[2] == '1' and board[4] == '2' and board[6] == '3':
         game_still_going = False
     elif board[6] == '1' and board[4] == '2' and board[2] == '3':
         game_still_going = False

     return


 def moves():
     # Moves Per Game
     global move
     move = move + 1
     print("Move: ")
     print(move)

     return

 play_game()

# Average Moves Per Game
avg = sum/100
print("Average Moves Per Game: ")
print(int(avg))

