import random
import sys
board = [' '] * 9
moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
pmoves = []
compmoves = []
av_moves = len(moves)
def menu(av_moves):
    choice = int(input("""
    Tic Tac Toe

    print("1: Start the game")
    print("2: Help")
    print("3: Credits")
    print("4: Exit")
    
    Enter your choice: """))
    if choice == 1:
        diff = int(input("""
        
    print("1: Easy")
    print("2: Medium")
    print("3: Hard")
        
    Enter your choice: """
                         ))
        if diff == 1:
            while av_moves > 0:
                playerm()
                av_moves -= 1
                printboard()
                if playerwincond() == "player won":
                    print("Player won")
                    break
                if av_moves == 0 and (playerwincond() != "player won"):
                    print("Tie")
                    break
                show_comp_m()
                av_moves -= 1
                printboard()
                if computerwincond() == "Computer won":
                    print("Computer won")
                    break
            menu(av_moves)
        elif diff == 2:
            print("midium")
            menu(av_moves)
        elif diff == 3:
            print("Hard")
            menu(av_moves)
        else:
            print("Invalid Choice try again")
            menu()
    elif choice == 2:
        print("Help\n", "This a simple tic tac toe game")
        menu(av_moves)
    elif choice == 3:
        print("Credits\nKostas Karagiorgos")
        menu(av_moves)
    elif choice == 4:
        print("Exit")
        sys.exit()
    else:
        print("Invalid Choice try again")
        menu()
def printboard():
    print(board[0]+'|'+board[1]+'|'+board[2])
    print('-----')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-----')
    print(board[6]+'|'+board[7]+'|'+board[8]+'\n')
def show_comp_m():
    movetdel = random.choice(moves)
    print("computer move is:", movetdel)
    moves.remove(movetdel)
    compmoves.append(movetdel)
    board[int(movetdel)-1] = 'O'
def playerm():
    pmove = int(input("Enter a number from 1-9 to make your move:"))
    while pmove < 1 or pmove > 9 or (str(pmove) not in moves):
        pmove = int(input("Enter a number from 1-9 to make your move:"))
    moves.remove(str(pmove))
    pmoves.append(str(pmove))
    board[int(pmove)-1] = 'X'
def playerwincond():
    if  ((board[0] == 'X' and board[1] == 'X' and board[2] == 'X')or
         (board[3] == 'X' and board[4] == 'X' and board[5] == 'X')or
         (board[6] == 'X' and board[7] == 'X' and board[8] == 'X')or
         (board[0] == 'X' and board[3] == 'X' and board[6] == 'X')or
         (board[1] == 'X' and board[4] == 'X' and board[7] == 'X')or
         (board[2] == 'X' and board[5] == 'X' and board[8] == 'X')or
         (board[0] == 'X' and board[4] == 'X' and board[8] == 'X')or
         (board[2] == 'X' and board[4] == 'X' and board[6] == 'X')):
        return "player won"
def computerwincond():
    if  ((board[0] == 'O' and board[1] == 'O' and board[2] == 'O')or
         (board[3] == 'O' and board[4] == 'O' and board[5] == 'O')or
         (board[6] == 'O' and board[7] == 'O' and board[8] == 'O')or
         (board[0] == 'O' and board[3] == 'O' and board[6] == 'O')or
         (board[1] == 'O' and board[4] == 'O' and board[7] == 'O')or
         (board[2] == 'O' and board[5] == 'O' and board[8] == 'O')or
         (board[0] == 'O' and board[4] == 'O' and board[8] == 'O')or
         (board[2] == 'O' and board[4] == 'O' and board[6] == 'O')):
        return "Computer won"
menu(av_moves)