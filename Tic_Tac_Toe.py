import random
from colorama import init, Fore, Style
init(autoreset=True)
def display_board(board):
    print()
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print("-----------")
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print("-----------")
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print()
def format_symbol(symbol):
    if symbol == 'X':
        return Fore.RED + symbol + Fore.RESET
    elif symbol == 'O':
        return Fore.BLUE + symbol + Fore.RESET
    else:
        return Fore.YELLOW + symbol + Fore.RESET


def player_choice():
    symbol = ''
    while symbol not in ['x', 'o']:
        symbol = input("do you want to be X or O?").lower()
        if symbol == "X":
            return ('X', 'O') 
        else:
            return ('O', 'X')

def player_move(board, symbol):
    move = -1
    while move not in range(1,10) or not board[move -1].isdigit():
         try:
            move = int(input("enter your move (1 - 9) :"))
            if move not in range(1,10) or not board[move -1].isdigit():
                print("invalid move, please try again")
         except ValueError:
            print("please enter a number between 1 and 9")
    board[move -1] = symbol

def ai_move(board,ai_symbol,player_symbol):
    for i in range (9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy,ai_symbol):
                board[i] = ai_symbol = ai_symbol
                return
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win(board_copy,player_symbol):
                board[i] = player_symbol = player_symbol
                return
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol

def check_win(board, symbol):
    win_conditions = [(0, 1, 2 ), ( 3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4 ,8), (2, 4, 6)]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
    return False
def check_full(board):
    return all(not spot.isdigit() for spot in board)
def tic_tac_toe():
    print("welcom to the ultimate game of TIC TAC TOE!")
    while True:
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9" ]
        player_symbol, ai_symbol = player_choice()
        turn = "player"
        game_on = True
        while game_on:
            display_board(board)
            if turn == "player":
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print ("congratulations! You have beaten me!")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print ("Its a tie!")
                        break
                    else:
                        turn = "AI"
            else:
                ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print ("AI has won the game")
                    game_on = False
                else:
                    if check_full(board):
                        display_board(board)
                        print ("Its a tie!")
                        break
                    else:
                        turn = "player"
        play_again = input("Do you want to play again? (Yes/No) ").lower()
        if play_again != "Yes":
           print ("Thank you for playing!")