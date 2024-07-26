def board(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    space = [[a1,a2,a3],
             [a4,a5,a6],
             [a7,a8,a9]]
    print(space[0][0],"|",space[0][1],"|",space[0][2])
    print("----------")
    print(space[1][0],"|",space[1][1],"|",space[1][2])
    print("----------")
    print(space[2][0],"|",space[2][1],"|",space[2][2])


switch = "X"
def switchplayer(switch):
    if switch == "X":
        return "O"
    else:
        return "X"

def check_winner():
    if a1==a2==a3!=" " or a4==a5==a6!=" " or a7==a8==a9!=" " or a1==a5==a9!=" " or a3==a5==a7!=" " or a1==a4==a7!=" " or a2==a5==a8!=" " or a3==a6==a9!=" ":
        return 1
    else:
        return 0
    
def check_tie():
    if a1!=" " and a2!=" " and a3!=" " and a4!=" " and a5!=" " and a6!=" " and a7!=" " and a8!=" " and a9!=" ":
        return 1
    else:
        return 0

def check_player(switch,player):
    if switch == "X":
        return 1
    else:
        return 2
    
print("WELCOME TO TIC-TAC-TOE")
print("JUST REFER TO THE BOARD BELOW TO GET THE BOX NUMBERS AND PLAY ACCORDINGLY")
print("WE WISH YOU ALL THE BEST")
print("THE GAME REQUIRES TWO PLAYERS")
print("HAPPY GAMING")
print()
a1 = ' '
a2 = ' '
a3 = ' '
a4 = ' '
a5 = ' '
a6 = ' '
a7 = ' '
a8 = ' '
a9 = ' '
board(1,2,3,4,5,6,7,8,9)
print()
print()

player = 2
player1_pts = 0
player2_pts = 0
print("")
turns = int(input("ENTER OF NUMBER OF GAMES U WANT TO PLAY : "))
for i in range(turns):
    a1 = ' '
    a2 = ' '
    a3 = ' '
    a4 = ' '
    a5 = ' '
    a6 = ' '
    a7 = ' '
    a8 = ' '
    a9 = ' '
    print()
    print("START OF NEW MATCH....")
    while check_tie!=0 or check_winner!=0:
        player = check_player(switch,player)
        print()
        print("It is player",player,"move")
        ch = int(input("Enter the box number : "))
        print()
        print()
        if ch==1:
            a1 = switch
            board(a1,a2,a3,a4,a5,a6,a7,a8,a9)
        elif ch==2:
            a2 = switch
            board(a1,a2,a3,a4,a5,a6,a7,a8,a9)
        elif ch==3:
            a3 = switch
            board(a1,a2,a3,a4,a5,a6,a7,a8,a9)
        elif ch==4:
            a4 = switch
            board(a1,a2,a3,a4,a5,a6,a7,a8,a9)
        elif ch==5:
            a5 = switch
            board(a1,a2,a3,a4,a5,a6,a7,a8,a9)
        elif ch==6:
            a6 = switch
            board(a1,a2,a3,a4,a5,a6,a7,a8,a9)
        elif ch==7:
            a7 = switch
            board(a1,a2,a3,a4,a5,a6,a7,a8,a9)
        elif ch==8:
            a8 = switch
            board(a1,a2,a3,a4,a5,a6,a7,a8,a9)
        elif ch==9:
            a9 = switch
            board(a1,a2,a3,a4,a5,a6,a7,a8,a9)
        else:
            print("Wrong input entered")
        print()
        print()
        if check_winner()==1:
            if player==1:
                print()
                print("Player One is the WINNER")
                player1_pts = player1_pts+1
            else:
                print()
                print("Player Two is the WINNER")
                player2_pts = player2_pts+1
            break
        if check_tie()==1:
            print()
            print("It is a TIE")
            break
        switch = switchplayer(switch)

print()
print("END OF GAME")
print("THE SCORES ARE..")
print("PLAYER 1 : ",player1_pts)
print("PLAYER 2 : ",player2_pts)
if player2_pts>player1_pts:
    print("WINNER OF THIS SERIES IS PALYER 2")
elif player2_pts<player1_pts:
    print("WINNER OF THIS SERIES IS PLAYER 1")
else:
    print("THE SERIES IS TIED")

print()
print("THANKS FOR PLAYING THE GAME")