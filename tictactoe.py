
board = [' '] * 9
moves = ['1','2','3','4','5','6','7','8','9']
pmoves = []
compmoves = []
av_moves = len(moves)
import random
def printboard():
    print( board[0]+'|'+board[1]+'|'+board[2])
    print('-----')
    print( board[3]+'|'+board[4]+'|'+board[5])
    print('-----')
    print( board[6]+'|'+board[7]+'|'+board[8]+'\n')


def show_comp_m():
        movetdel = random.choice(moves)
        print("computer move is:",movetdel)
        moves.remove(movetdel)
        compmoves.append(movetdel)
        board[int(movetdel)-1] = 'O'

def playerm():
    pmove = int(input("Enter a number from 1-9 to make your move:"))
    while pmove < 1 or pmove > 9 or (str(pmove) not in moves) :
        pmove = int(input("Enter a number from 1-9 to make your move:"))
    moves.remove(str(pmove))
    pmoves.append(str(pmove))
    board[int(pmove)-1] = 'X'
    
def playerwincond():
    if ((board[0]=='X' and board [1]=='X' and board[2]=='X')or
    (board[3]=='X' and board[4] =='X' and board[5] == 'X')or
    (board[6]=='X' and board[7] =='X' and board[8] == 'X')or
    (board[0]=='X' and board[3] == 'X' and board[6] == 'X')or
    (board[1]=='X' and board[4] == 'X' and board[7] == 'X')or
    (board[2]=='X' and board[5] == 'X' and board[8] == 'X')or
    (board[0]=='X' and board[4] == 'X' and board[8] == 'X')or
    (board[2]=='X' and board[4] == 'X' and board[6] == 'X')):
        return "player won"
        

def computerwincond():
    if  ((board[0]=='O' and board [1]=='O' and board[2]=='O')or
    (board[3]=='O' and board[4] =='O' and board[5] == 'O')or
    (board[6]=='O' and board[7] =='O' and board[8] == 'O')or
    (board[0]=='O' and board[3] == 'O' and board[6] == 'O')or
    (board[1]=='O' and board[4] == 'O' and board[7] == 'O')or
    (board[2]=='O' and board[5] == 'O' and board[8] == 'O')or
    (board[0]=='O' and board[4] == 'O' and board[8] == 'O')or
    (board[2]=='O' and board[4] == 'O' and board[6] == 'O')):
        return "Computer won"
    
while av_moves > 0:
    playerm()
    av_moves -=1
    printboard()
    if playerwincond() == "player won":
        print("Player won")
        break
    if av_moves == 0 and ( playerwincond() != "player won"):
        print("Tie")
        break
    show_comp_m()
    av_moves -=1
    printboard()
    if computerwincond() == "Computer won":
        print("Computer won")
        break
