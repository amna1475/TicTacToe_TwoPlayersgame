import random
from math import floor

print("Welcome to Tic Tac Toe")
gl_1 = "1"
gl_2 = "2"
gl_3 = "3"
gl_4 = "4"
gl_5 = "5"
gl_6 = "6"
gl_7 = "7"
gl_8 = "8"
gl_9 = "9"
print(f"{gl_1}|  {gl_2}|  {gl_3}|\n{gl_4}|  {gl_5}|  {gl_6}|\n{gl_7}|  {gl_8}|  {gl_9}|")
first_player = input("Enter your name, first player: ")
second_player = input("Enter your name, second player: ")
select_toss = input(first_player + ", select heads or tails: ")
print(first_player, ", your symbol is X and", second_player," your symbol is O")
toss = floor(random.randint(1, 9))\
    
if select_toss == "heads":
    print(first_player + ", have selected heads")
    if toss % 2 == 0:
        win_player = first_player
        loser_player = second_player
        print(win_player + ", have won the toss")
        loser_player = second_player
        winner_symbol = "X"
        loser_symbol = "O"
    else:
        win_player = second_player
        loser_player = first_player
        print(win_player + ", have won the toss")
        winner_symbol = "O"
        loser_symbol = "X"
else:
    print(second_player + ", have selected heads")
    if toss % 2 == 0:
        win_player = second_player
        loser_player = first_player
        print(win_player + ", have won the toss")
        winner_symbol = "O"
        loser_symbol = "X"
    else:
        win_player = first_player
        loser_player = second_player
        print(win_player + ", have won the toss")
        winner_symbol = "X"
        loser_symbol = "O"
        
#Code For First Turn of Toss Winner
print(f"{gl_1}|  {gl_2}|  {gl_3}|\n{gl_4}|  {gl_5}|  {gl_6}|\n{gl_7}|  {gl_8}|  {gl_9}|")
turn = 0
played = 0
while turn<8:
    if played == 0:
        move = input(f"{win_player}, enter your desired number: ")
        played = 1
        turn = turn + 1
        if move == gl_1:
            gl_1 = winner_symbol
        elif move ==gl_2:
            gl_2 = winner_symbol
        elif move ==gl_3:
            gl_3=winner_symbol
        elif move ==gl_4:
            gl_4=winner_symbol
        elif move ==gl_5:
            gl_5= winner_symbol
        elif move ==gl_6:
            gl_6=winner_symbol
        elif move ==gl_7:
            gl_7 = winner_symbol
        elif move ==gl_8:
            gl_8 = winner_symbol
        elif move ==gl_9:
            gl_9 = winner_symbol
        print(f"{gl_1}|  {gl_2}|  {gl_3}|\n{gl_4}|  {gl_5}|  {gl_6}|\n{gl_7}|  {gl_8}|  {gl_9}|")
        if (gl_1 == gl_2 == gl_3) or (gl_4 == gl_5 == gl_6) or (gl_7 == gl_8 == gl_9) or (gl_1 == gl_4 == gl_7) or (gl_2 == gl_5 == gl_8) or (gl_3 == gl_6 == gl_9) or (gl_1 == gl_5 == gl_9) or (gl_3 == gl_5 == gl_7):
            print(f"{win_player} has won the game")
            break
    elif played == 1:
        move = input(f"{loser_player}, enter your desired number: ")
        played = 0
        turn = turn + 1
        if move == gl_1:
            gl_1 = loser_symbol
        elif move ==gl_2:
            gl_2 = loser_symbol
        elif move ==gl_3:
            gl_3=loser_symbol
        elif move ==gl_4:
            gl_4=loser_symbol
        elif move ==gl_5:
            gl_5= loser_symbol
        elif move ==gl_6:
            gl_6=loser_symbol
        elif move ==gl_7:
            gl_7 = loser_symbol
        elif move ==gl_8:
            gl_8 = loser_symbol
        elif move ==gl_9:
            gl_9 = loser_symbol
        print(f"{gl_1}|  {gl_2}|  {gl_3}|\n{gl_4}|  {gl_5}|  {gl_6}|\n{gl_7}|  {gl_8}|  {gl_9}|")
        if (gl_1 == gl_2 == gl_3) or (gl_4 == gl_5 == gl_6) or (gl_7 == gl_8 == gl_9) or (gl_1 == gl_4 == gl_7) or (gl_2 == gl_5 == gl_8) or (gl_3 == gl_6 == gl_9) or (gl_1 == gl_5 == gl_9) or (gl_3 == gl_5 == gl_7):
            print(f"{loser_player} has won the game")
            break