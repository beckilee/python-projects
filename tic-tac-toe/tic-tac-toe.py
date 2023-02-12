# Tic-Tac-Toe!
# Two players take turns entering X or O into squares on the tic-tac-toe board. When someone gets three squares in a row, in a column, or diagonally, they win. The game keeps score of how many games each player has won. The score is reset when the script exits.

# Define starting board
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
board = [ row1, row2, row3 ]

# Display current board
def display_board():
    print(" " + row1[0] + " | " + row1[1] + " | " + row1[2])
    print("-----------")
    print(" " + row2[0] + " | " + row2[1] + " | " + row2[2])
    print("-----------")
    print(" " + row3[0] + " | " + row3[1] + " | " + row3[2])

# Display which numbers correspond to which cells of the grid
def display_map():
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")

# Create the board: Internal logic for the game
def create_board():
    # Initialize variables for tally of games won
    x_count = 0
    o_count = 0
    # Loop X and O turns until someone wins or there's a tie, in which case ask if they want to play again; if they do, keep looping; otherwise exit loop
    while True:
        # X plays a move
        x_turn()
        # Check the winner; if X has won, increase the tally by one, print score, ask if the user wants to play again (if so, repeat loop)
        winner = check_winner(board)
        if winner == "X":
            x_count += 1
            print("X WINS! Score: X has won", x_count, "game(s). O has won", o_count, "game(s).")
            again = input("Play again? Y for yes, or anything else to exit: ")
            if again.lower() == "y" or again.lower() == "yes":
                reset(board)
                continue
            break
        # If there's a tie, ask if user wants to play again (if so, repeat loop)
        elif winner == "N":
            print("No winners. It's a tie!")
            again = input("Play again? Y for yes, or anything else to exit: ")
            if again.lower() == "y" or again.lower() == "yes":
                reset(board)
                continue
            break
        # If there's no winner and no tie after X's turn, it must be O's turn to play, so execute else statement
        else:
            # O plays a move
            o_turn()
            # Check the winner; if O has won, increase the tally by one, print score, ask if the user wants to play again (if so, repeat loop)
            winner = check_winner(board)
            if winner == "O":
                o_count += 1
                print("O WINS! Score: X has won", x_count, "game(s). O has won", o_count, "game(s).")
                again = input("Play again? Y for yes, or anything else to exit: ")
                if again.lower() == "y" or again.lower() == "yes":
                    reset(board)
                    continue
                break
            # If there's no winner and no tie after O's turn, it must be X's turn to play (so start the loop over)
            else:
                continue

# On X's turn, loop until the user enters a number corresponding to an empty grid cell; otherwise give an error message
def x_turn():
    while True:
        move = input("X, enter a number from 1 to 9 to play: ")
        if move == "1" and board[0][0] == " ":
            board[0][0] = "X"
            break
        elif move == "2" and board[0][1] == " ":
            board[0][1] = "X"
            break
        elif move == "3" and board[0][2] == " ":
            board[0][2] = "X"
            break
        elif move == "4" and board[1][0] == " ":
            board[1][0] = "X"
            break
        elif move == "5" and board[1][1] == " ":
            board[1][1] = "X"
            break
        elif move == "6" and board[1][2] == " ":
            board[1][2] = "X"
            break
        elif move == "7" and board[2][0] == " ":
            board[2][0] = "X"
            break
        elif move == "8" and board[2][1] == " ":
            board[2][1] = "X"
            break
        elif move == "9" and board[2][2] == " ":
            board[2][2] = "X"
            break
        else:
            print("Sorry, that's not an option; please try again!")
            continue
    # Display the board after the player's turn
    display_board()

# On O's turn, loop until the user enters a number corresponding to an empty grid cell; otherwise give an error message
def o_turn():
    while True:
        move = input("O, enter a number from 1 to 9 to play: ")
        if move == "1" and board[0][0] == " ":
            board[0][0] = "O"
            break
        elif move == "2" and board[0][1] == " ":
            board[0][1] = "O"
            break
        elif move == "3" and board[0][2] == " ":
            board[0][2] = "O"
            break
        elif move == "4" and board[1][0] == " ":
            board[1][0] = "O"
            break
        elif move == "5" and board[1][1] == " ":
            board[1][1] = "O"
            break
        elif move == "6" and board[1][2] == " ":
            board[1][2] = "O"
            break
        elif move == "7" and board[2][0] == " ":
            board[2][0] = "O"
            break
        elif move == "8" and board[2][1] == " ":
            board[2][1] = "O"
            break
        elif move == "9" and board[2][2] == " ":
            board[2][2] = "O"
            break
        else:
            print("Sorry, that's not an option; please try again!")
            continue
    # Display the board after the player's turn
    display_board()

# If X gets three in a row, return X; if O gets three in a row, return O; if every space is filled but there are no winners, return N (tie); otherwise, return " "
def check_winner(board):
    if ((board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or
        (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or
        (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or
        (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or
        (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or
        (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") or
        (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or
        (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X")):
        return "X"
    elif ((board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or
        (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or
        (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or
        (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or
        (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") or
        (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O") or
        (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or
        (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O")):
        return "O"
    elif board[0].count(" ") == 0 and board[1].count(" ") == 0 and board[2].count(" ") == 0:
        return "N"
    else:
        return " "

# Reset all board values to " " in order to play again
def reset(board):
    for column in range(0, len(board)):
        for row in range(0, len(board[0])):
            board[column][row] = " "
    return board

# Display "map" of which numbers correspond to which cell of grid, then create the board
print("=================================TIC-TAC-TOE================================")
print("INSTRUCTIONS: When it's your turn, enter a number corresponding to a square: ")
display_map()
create_board()
print("Thanks for playing!")
