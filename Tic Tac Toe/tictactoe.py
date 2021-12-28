import time, os


clear = lambda : os.system("clear") # os.system("cls") for windows


def main():

    global player1
    global player2
    global board_pos
    global game_over
    global player1_positions
    global player2_positions

    clear()
    board_pos = ["Place Holder", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    game_over = False
    player1 = None
    player2 = None
    player1 = player1_choice()
    player2 = choose_player2()
    player1_positions = []
    player2_positions = []
    display_board(board_pos)
    
    while not game_over:
        choose_pos()
    replay()
    

def player1_choice():
    choice = input("Player 1: do you want to play as X or O: ")

    while choice not in ["x", "o", "X", "O"]:
        clear()
        print("Invalid choice")
        time.sleep(0.4)
        clear()
        choice = input("Player 1: do you want to play as X or O: ")
    clear()
    return choice.upper()

def choose_player2():
    if player1 == "X":
        player2 = "O"

    else:
        player2 = "X"

    return player2

def display_board(board_pos):
    clear()

    print(f" {board_pos[1]} | {board_pos[2]} | {board_pos[3]} ")
    print("-"*11)
    print(f" {board_pos[4]} | {board_pos[5]} | {board_pos[6]} ")
    print("-"*11)
    print(f" {board_pos[7]} | {board_pos[8]} | {board_pos[9]} ")

def choose_pos():
    global player1_positions
    global player2_positions

    player1_pos = int(input("\nPlayer 1: Please choose a position (1-9): "))

    while player1_pos not in range(0, 10):
        clear()
        print("Invalid Value")
        time.sleep(0.4)
        clear()
        display_board(board_pos)
        player1_pos = int(input("\nPlayer 1: Please choose a position (1-9): "))

    while player1_pos in player1_positions or player1_pos in player2_positions:
        clear()
        display_board(board_pos)
        player1_pos = int(input("\nPlayer 1: This position has already been used, please choose another position: "))

    player1_positions.append(player1_pos)

    board_pos[player1_pos] = player1


    clear()
    display_board(board_pos)

    

    choose_winner()

    if game_over == True:
        return

    if " " not in board_pos:
            tie()
            return

    player2_pos = int(input("\nPlayer 2: Please choose a position (1-9): "))

    while player2_pos not in range(0, 10):
        clear()
        print("Invalid Value")
        time.sleep(0.4)
        clear()
        display_board(board_pos)
        player2_pos = int(input("\nPlayer 2: Please choose a position (1-9): "))
    
    while player2_pos in player1_positions or player2_pos in player2_positions:
        clear()
        display_board(board_pos)
        player2_pos = int(input("\nPlayer 2: This position has already been used, please choose another position: "))

    player2_positions.append(player2_pos)

    board_pos[player2_pos] = player2

    clear()
    display_board(board_pos)

    choose_winner()

    if " " not in board_pos:
            tie()
            return
def choose_winner():
    
    if board_pos[1] == player1 and board_pos[2] == player1 and board_pos[3] == player1:
        player1_win()
    elif board_pos[4] == player1 and board_pos[5] == player1 and board_pos[6] == player1:
        player1_win()
    elif board_pos[7] == player1 and board_pos[8] == player1 and board_pos[9] == player1:
        player1_win()
    elif board_pos[1] == player1 and board_pos[4] == player1 and board_pos[7] == player1:
        player1_win()
    elif board_pos[2] == player1 and board_pos[5] == player1 and board_pos[8] == player1:
        player1_win()
    elif board_pos[3] == player1 and board_pos[6] == player1 and board_pos[9] == player1:
        player1_win()
    elif board_pos[1] == player1 and board_pos[5] == player1 and board_pos[9] == player1:
        player1_win()
    elif board_pos[3] == player1 and board_pos[5] == player1 and board_pos[7] == player1:
        player1_win()

    elif board_pos[1] == player2 and board_pos[2] == player2 and board_pos[3] == player2:
        player2_win()
    elif board_pos[4] == player2 and board_pos[5] == player2 and board_pos[6] == player2:
        player2_win()
    elif board_pos[7] == player2 and board_pos[8] == player2 and board_pos[9] == player2:
        player2_win()
    elif board_pos[1] == player2 and board_pos[4] == player2 and board_pos[7] == player2:
        player2_win()
    elif board_pos[2] == player2 and board_pos[5] == player2 and board_pos[8] == player2:
        player2_win()
    elif board_pos[3] == player2 and board_pos[6] == player2 and board_pos[9] == player2:
        player2_win()
    elif board_pos[1] == player2 and board_pos[5] == player2 and board_pos[9] == player2:
        player2_win()
    elif board_pos[3] == player2 and board_pos[5] == player2 and board_pos[7] == player2:
        player2_win()
        

def player1_win():
    global game_over

    clear()
    display_board(board_pos)
    print("\nPlayer 1 won!")
    game_over = True

def player2_win():
    global game_over

    clear()
    display_board(board_pos)
    print("\nPlayer 2 won!")
    game_over = True

def tie():
    global game_over

    clear()
    display_board(board_pos)
    print("\nTie!")
    game_over = True

def replay():
    choice = input("\nPlay again (Y or N): ")

    while choice.lower() not in ["y", "n", "yes", "no"]:
        clear()
        print("Invalid option")
        time.sleep(0.4)
        clear()
        display_board(board_pos)
        choice = input("\nPlay again (Y or N): ")

    if choice.lower() == 'y' or choice.lower() == 'yes':
        main()
    elif choice.lower() == 'n' or choice.lower() == 'no':
        quit()

main()