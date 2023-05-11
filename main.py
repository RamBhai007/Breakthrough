
import sys
import pygame
import random

paleyellow=(253,253,150)
black=(0,0,0)
white=(255,255,255)
green=(57,255,20)
screen=''
cell=''
BREATH=''
LENGTH=''
clock=''

switch={
    'Y':'B',
    'B':'Y'
}
choice=1



Y_valid=[(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)]
B_valid=[(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7)]
    
Y_Pos=[(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7)]
B_Pos=[(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(7,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7)]
mat=[
        ['Y','Y','Y','Y','Y','Y','Y','Y'],
        ['Y','Y','Y','Y','Y','Y','Y','Y'],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        ['B','B','B','B','B','B','B','B'],
        ['B','B','B','B','B','B','B','B']
    ]
temp_mat=mat

MAX=(100000,100000)
MIN=(-100000,-100000)

def isBlackWinner(B_Pos):
    for i in B_Pos:
        if i[0] == 1 or i[0] == 0:
            return True

def isYellowWinner(Y_Pos):
    for i in Y_Pos:
        if i[0] == 6 or i[0] == 7:
            return True

def min_Max_Alpha_Beta_mode(Depth,index,maxturn,moves,TDepth,alpha,beta,heuristic_mode,mat,player):
    if (Depth == TDepth):
        return moves[index]
    elif (maxturn):
        alpha_heuristic_i = Heuristic(player)
        best = min_Max_Alpha_Beta_mode(Depth + 1, index * 2+1,False, moves, TDepth,alpha,beta,heuristic_mode,mat,player)
        
        alpha = min(alpha, best)
        alpha_heuristic=alpha_heuristic_i
        if heuristic_mode=='offensive1':
            alpha_heuristic = offensive_Heuristic_1(player)
        elif heuristic_mode=='offensive2':
            alpha_heuristic = offensive_Heuristic_2(player)
        elif heuristic_mode=='deffensive1':
            alpha_heuristic = defensive_Heuristic_1(player)
        elif heuristic_mode=='deffensive2':
            alpha_heuristic = defensive_Heuristic_2(player)
        if alpha_heuristic_i<alpha_heuristic:
            return alpha
        else:
            return best
    else:
        beta_heuristic_i = Heuristic(player)
        best = min_Max_Alpha_Beta_mode(Depth + 1, index * 2+1,True, moves, TDepth,alpha,beta,heuristic_mode,mat,player)
        beta = max(beta, best)
        beta_heuristic=beta_heuristic_i
        if heuristic_mode=='offensive1':
            beta_heuristic = offensive_Heuristic_1(player)
        elif heuristic_mode=='offensive2':
            beta_heuristic = offensive_Heuristic_2(player)
        elif heuristic_mode=='deffensive1':
            beta_heuristic = defensive_Heuristic_1(player)
        elif heuristic_mode=='deffensive2':
            beta_heuristic = defensive_Heuristic_2(player)
        if beta_heuristic_i>beta_heuristic:
            return beta
        else:
            return best


def min_Max_Alpha_Beta(Depth,index,maxturn,moves,TDepth,alpha,beta):
    
    if (Depth == TDepth):
        return moves[index]
    elif (maxturn):
        best = min_Max_Alpha_Beta(Depth + 1, index * 2+1,False, moves, TDepth,alpha,beta)
        alpha = max(alpha, best)
        return alpha
    else:
        best = min_Max_Alpha_Beta(Depth + 1, index * 2+1,True, moves, TDepth,alpha,beta)
        beta = min(beta, best)
        return beta

def min_Max(Depth,index,maxturn,moves,TDepth):
    
    if (Depth == TDepth):
        return moves[index]
    if (maxturn):
        return max(min_Max(Depth + 1, index * 2,False, moves, TDepth),min_Max(Depth + 1, index * 2 + 1,False, moves, TDepth))
    else:
        return min(min_Max(Depth + 1, index * 2,True, moves, TDepth),min_Max(Depth + 1, index * 2 + 1,True, moves, TDepth))



def Heuristic(player):
    s=0
    for i in mat:
        s+=i.count(player)
        s-=i.count(switch[player])
    return s
def defensive_Heuristic_1(player):
    s=0
    for i in mat:
        s+=i.count(player)
    number_of_own_pieces_remaining=s
    return 2*(number_of_own_pieces_remaining) + random.random()

def offensive_Heuristic_1(player):
    s=0
    player=switch[player]
    for i in mat:
        s+=i.count(player)
    number_of_opponent_pieces_remaining=s
    return 2*(30 - number_of_opponent_pieces_remaining) + random.random()  

def defensive_Heuristic_2(player):
    s=0
    for i in mat:
        s+=i.count(player)
    number_of_own_pieces_remaining=s
    return number_of_own_pieces_remaining+ random.random()  

def offensive_Heuristic_2(player):
    s=0
    player=switch[player]
    for i in mat:
        s+=i.count(player)
    number_of_opponent_pieces_remaining=s
    return  number_of_opponent_pieces_remaining+ random.random()  




def select_move_black():
    moves = [(-1,-1), (-1 ,0) , (-1, 1) ]
    return random.choice(moves)

def select_move_paleyellow():
    moves = [(1,-1), (1 ,0) , (1, 1) ]
    return random.choice(moves)

def pick_one_black():
    return random.choice(B_valid)

def pick_one_paleyellow():
    return random.choice(Y_valid)

def update_Valid_Pos_B():
    global B_valid
    B_valid_temp=[]
    for i in B_Pos:
        for k in [move((-1,-1),i), move((-1 ,0),i) , move((-1, 1),i)]:
            if is_validPos(k) and ( mat[k[0]][k[1]]==' ' or mat[k[0]][k[1]]=='Y' ):
                B_valid_temp.append(i)
                break
    B_valid=B_valid_temp

def update_Valid_Pos_Y():
    global Y_valid
    Y_valid_temp=[]
    for i in Y_Pos:
        for k in [move((1,-1),i), move((1 ,0),i) , move((1, 1),i)]:
            if is_validPos(k) and ( mat[k[0]][k[1]]==' ' or mat[k[0]][k[1]]=='B' ):
                Y_valid_temp.append(i)
                break
    Y_valid=Y_valid_temp

def is_validPos(Pos):
    if ( Pos[0]>=0 and Pos[0]<=7 ) and ( Pos[1]>=0 and Pos[1]<=7 ):
        return True
    else:
        return False

def valid_B_Pos(Pos):
    if Pos in B_Pos:
        return False
    return True

def valid_Y_Pos(Pos):
    if Pos in Y_Pos:
        return False
    return True

def update_black(PreviousPos,NewPos):
    mat[PreviousPos[0]][PreviousPos[1]]=' '
    B_valid.remove(PreviousPos)
    B_Pos.remove(PreviousPos)
    mat[NewPos[0]][NewPos[1]]='B'
    B_valid.append(NewPos)
    B_Pos.append(NewPos)
    update_Valid_Pos_B()



def update_yellow(PreviousPos,NewPos):
    mat[PreviousPos[0]][PreviousPos[1]]=' '
    Y_valid.remove(PreviousPos)
    Y_Pos.remove(PreviousPos)
    mat[NewPos[0]][NewPos[1]]='Y'
    Y_valid.append(NewPos)
    Y_Pos.append(NewPos)
    update_Valid_Pos_Y()

def move(x,y):
    return (x[0]+y[0],x[1]+y[1])



def Black_Move():
    if len(B_valid)>0:  
            black_Pos=pick_one_black()
            b_move=(-1,-1)
            new_Pos=(-1,-1)       
            while(not is_validPos(new_Pos)):
                b_move=select_move_black()
                new_Pos=move(b_move,black_Pos)
                if new_Pos[1]==black_Pos[1] and mat[new_Pos[0]][new_Pos[1]]=='Y':
                    new_Pos=(-1,-1)
            if is_validPos(new_Pos) and valid_B_Pos(new_Pos):
                update_black(black_Pos,new_Pos)

def Yellow_Move():
    if len(Y_valid)>0:  
            yellow_Pos=pick_one_paleyellow()
            y_move=(-1,-1)
            new_Pos=(-1,-1)       
            while(not is_validPos(new_Pos)):
                y_move=select_move_paleyellow()
                new_Pos=move(y_move,yellow_Pos)
                if new_Pos[1]==yellow_Pos[1] and mat[new_Pos[0]][new_Pos[1]]=='B':
                    new_Pos=(-1,-1)
            if is_validPos(new_Pos) and valid_Y_Pos(new_Pos):
                update_yellow(yellow_Pos,new_Pos)

def isBlackWinner():
    for i in B_Pos:
        if i[0] == 1 or i[0] == 0:
            return True

def isYellowWinner():
    for i in Y_Pos:
        if i[0] == 6 or i[0] == 7:
            return True

def main():
    
    global screen,cell,BREATH,LENGTH,clock,paleyellow,white,black
    



    pygame.init()
    cell=80
    BREATH=len(mat)*cell
    LENGTH=len(mat[0])*cell
    screen = pygame.display.set_mode((LENGTH, BREATH),pygame.RESIZABLE)

    clock = pygame.time.Clock()
    flag=True
    pygame.display.set_caption("BreakThru")
    
    
    clock = pygame.time.Clock()
    
    turn=True
    winner=False
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(6)
        screen.fill((0, 0, 0))
        if flag:
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    pygame.draw.rect(screen,paleyellow,(j *cell, i * cell, cell, cell),1)
                    if mat[i][j]=='Y':
                        pygame.draw.circle(screen, paleyellow,[j *cell+35, i * cell+35], 15, 0)
                    elif mat[i][j]=='B':
                        pygame.draw.circle(screen, white,[j *cell+35, i * cell+35], 15, 0)                   
            pygame.display.flip()
        pygame.display.update()
        
        if not winner:
            if choice==1:
                turn=matchup_1(turn)
            elif choice==2:
                turn=matchup_2(turn)
            elif choice==3:
                turn=matchup_3(turn)
            elif choice==4:
                turn=matchup_4(turn)
            elif choice==5:
                turn=matchup_5(turn)
            elif choice==6:
                turn=matchup_6(turn)
            else:
                turn=matchup_7(turn)
            if isBlackWinner():
                msg="White is winner"
                winner=True
                pygame.mixer.music.load('over.mp3')
                pygame.mixer.music.play(1)
            elif isYellowWinner():
                msg="Yellow is winner"
                winner=True  
                pygame.mixer.music.load('over.mp3')
                pygame.mixer.music.play(1)
            
        else:
            font=pygame.font.Font('rt.ttf', 70)
            txt = font.render(msg, True, green)
            screen.blit(txt,(BREATH//2 - txt.get_width() // 2, LENGTH//2 - txt.get_height() // 2))
            pygame.display.flip()
            pygame.display.update()


def Random_Ai(turn):
    if turn:
        Black_Move()
        turn=False
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
        Yellow_Move()
        turn=True
    return turn
def Black_Move_Minmax_():
    if len(B_valid)>0:  
            black_Pos=min_Max(0,0,False,B_valid,3)
            b_move=(-1,-1)
            new_Pos=(-1,-1)       
            while(not is_validPos(new_Pos)):
                b_move=select_move_black()
                new_Pos=move(b_move,black_Pos)
                if not valid_B_Pos(new_Pos):
                    continue
                if new_Pos[1]==black_Pos[1] and mat[new_Pos[0]][new_Pos[1]]=='Y':
                    new_Pos=(-1,-1)
            update_Valid_Pos_B()
            if is_validPos(new_Pos) and valid_B_Pos(new_Pos):
                update_black(black_Pos,new_Pos)
            else:
                Black_Move_Minmax_()
def Black_Move_Minmax(mode):
    if len(B_valid)>0:  
            black_Pos=min_Max_Alpha_Beta_mode(0,0,True,B_valid,3,MAX,MIN,mode,mat,'B')
            
            b_move=(-1,-1)
            new_Pos=(-1,-1)       
            while(not is_validPos(new_Pos)):
                b_move=select_move_black()
                new_Pos=move(b_move,black_Pos)
                if not valid_B_Pos(new_Pos):
                    continue
                if new_Pos[1]==black_Pos[1] and mat[new_Pos[0]][new_Pos[1]]=='Y':
                    new_Pos=(-1,-1)
            update_Valid_Pos_B()
            if is_validPos(new_Pos) and valid_B_Pos(new_Pos):
                update_black(black_Pos,new_Pos)
            else:
                Black_Move_Minmax(mode)

def Yellow_Move_Minmax(mode):
    if len(Y_valid)>0:  
            yellow_Pos=min_Max_Alpha_Beta_mode(0,-1,True,Y_valid,3,MAX,MIN,mode,mat,'Y')
            y_move=(-1,-1)
            new_Pos=(-1,-1)       
            while(not is_validPos(new_Pos)):
                y_move=select_move_paleyellow()
                new_Pos=move(y_move,yellow_Pos)
                if not valid_Y_Pos(new_Pos):
                    continue
                if new_Pos[1]==yellow_Pos[1] and mat[new_Pos[0]][new_Pos[1]]=='B':
                    new_Pos=(-1,-1)
            update_Valid_Pos_Y()
            if is_validPos(new_Pos) and valid_Y_Pos(new_Pos):
                update_yellow(yellow_Pos,new_Pos)
            else:
                Yellow_Move_Minmax(mode)
            
          
def Yellow_Move_alphaBeta():
    if len(Y_valid)>0:  
            yellow_Pos=min_Max_Alpha_Beta(0,-1,False,Y_valid,3,MIN,MAX)
            y_move=(-1,-1)
            new_Pos=(-1,-1)       
            while(not is_validPos(new_Pos)):
                y_move=select_move_paleyellow()
                new_Pos=move(y_move,yellow_Pos)
                if not valid_Y_Pos(new_Pos):
                    continue
                if new_Pos[1]==yellow_Pos[1] and mat[new_Pos[0]][new_Pos[1]]=='B':
                    new_Pos=(-1,-1)
            update_Valid_Pos_Y()
            if is_validPos(new_Pos) and valid_Y_Pos(new_Pos):
                update_yellow(yellow_Pos,new_Pos)
            else:
                Yellow_Move_alphaBeta()
            

def Random_Ai_Minmax(turn):
    if turn:
        Black_Move_Minmax()
        turn=False
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
        Yellow_Move()
        turn=True
    return turn

def min_Max_Alpha_Beta_Ai_Test_1(turn):
    if turn:
        Yellow_Move_Minmax('offensive1')
        
        turn=False
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
        Black_Move_Minmax('offensive1')
        turn=True
    return turn

def min_Max_Alpha_Beta_Ai(turn):
    if turn:
        Black_Move_Minmax()
        turn=False
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
        Yellow_Move_alphaBeta()
        turn=True
    return turn
#deffensive1 white vs random ai yellow
def Test_1(turn):
    if turn:
        Black_Move_Minmax('deffensive1')
        turn=False
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
        Yellow_Move()
        turn=True
    return turn
#offensive2 white vs random ai yellow
def Test_2(turn):
    if turn:
        Black_Move_Minmax('offensive1')
        turn=False
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
        Yellow_Move()
        turn=True
    return turn
#deffensive2 white vs random ai yellow
def Test_3(turn):
    if turn:
        Black_Move_Minmax('deffensive2')
        turn=False
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
        Yellow_Move()
        turn=True
    return turn
#offensive2 white vs random ai yellow
def Test_4(turn):
    if turn:
        Black_Move_Minmax('offensive2')
        turn=False
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
        Yellow_Move()
        turn=True
    return turn
#SIX MATCHUPS
#MATCHUP 1
def matchup_1(turn):
    if turn:
        Black_Move_Minmax_()
        turn=False
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
        Yellow_Move_Minmax('offensive1')
        turn=True
    return turn

#MATCHUP 2
def matchup_2(turn):
    if turn:
        Black_Move_Minmax('offensive2')
        turn=False
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
        Yellow_Move_Minmax('deffensive1')
        turn=True
    return turn

#MATCHUP 3
def matchup_3(turn):
    if turn:
        Black_Move_Minmax('deffensive2')
        turn=False
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
        Yellow_Move_Minmax('offensive1')
        turn=True
    return turn

#MATCHUP 4
def matchup_4(turn):
    if turn:
        Black_Move_Minmax_('offensive2')
        turn=False
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
        Yellow_Move_Minmax('offensive1')
        turn=True
    return turn

#MATCHUP 5
def matchup_5(turn):
    if turn:
        Black_Move_Minmax('deffensive2')
        turn=False
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
        Yellow_Move_Minmax('deffensive1')
        turn=True
    return turn

#MATCHUP 6
def matchup_6(turn):
    if turn:
        Black_Move_Minmax('offensive2')
        turn=False
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
        Yellow_Move_Minmax('deffensive2')
        turn=True
    return turn

#MATCHUP 7
def matchup_7(turn):
    if turn:
        Black_Move()
        turn=False
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
    else:
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play(1)
        Yellow_Move()
        turn=True
    return turn
print('''
    SELECT MATCHUP
    (1) Minimax (Offensive Heuristic 1) vs Alpha-beta (Offensive Heuristic 1)
    (2) Alpha-beta (Offensive Heuristic 2) vs Alpha-beta (Defensive Heuristic 1)
    (3) Alpha-beta (Defensive Heuristic 2) vs Alpha-beta (Offensive Heuristic 1)
    (4) Alpha-beta (Offensive Heuristic 2) vs Alpha-beta (Offensive Heuristic 1)
    (5) Alpha-beta (Defensive Heuristic 2) vs Alpha-beta (Defensive Heuristic 1)
    (6) Alpha-beta (Offensive Heuristic 2) vs Alpha-beta (Defensive Heuristic 2)
    (7) Random AI vs Random AI
    or type -1 to exit
    ''')

choice=int(input())
main()
