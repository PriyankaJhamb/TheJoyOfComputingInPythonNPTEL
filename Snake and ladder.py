# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 16:43:12 2021

@author: DELL
"""

from PIL import Image
import random
end=100
def show_board():
    img=Image.open('sal.jfif')
    img.show()
def check_snake(points):
    if points==98:
        print("Snake")
        return 79
    elif points==95:
        print("Snake")
        return 75
    elif points==93:
        print("Snake")
        return 73
    elif points==87:
        print("Snake")
        return 24
    elif points==64:
        print("Snake")
        return 60
    elif points==62:
        print("Snake")
        return 19
    elif points==54:
        print("Snake")
        return 
    elif points==14:
        print("Snake")
        return 4
    else:
        #not a ladder
        return points
def check_ladder(points):
    if points==80:
        print("ladder")
        return 100
    elif points==71:
        print("ladder")
        return 91
    elif points==28:
        print("ladder")
        return 84
    elif points==51:
        print("ladder")
        return 67
    elif points==9:
        print("ladder")
        return 31
    elif points==4:
        print("ladder")
        return 14
    elif points==1:
        print("ladder")
        return 38
    elif points==21:
        print("ladder")
        return 42
    else:
        #not a ladder
        return points
def reached_end(points):
    if points==end:
        return True
    else:
        return False
    
def play():
    p1_name=input('Player 1, please enter your name: ')
    p2_name=input('Player 2, please enter your name: ')
    pp1=0
    pp2=0
    turn=0
    while(1):
        if(turn%2==0):
            #player 1 turns
            print(p1_name,'Your turn')
            #ask player1's choice to continue
            c=input('Press 1 to continue, 0 to quit: ')
            if c==0:
                print(p1.name,'scored',pp1)
                print(p2_name,'scored',pp2)
                print('Quiting the game, thanks for playing')
                break
            #generate a random number from 1,2, 3,4,5,6
            dice=random.randint(1,6)
            print('Dice showed: ', dice)
            pp1=pp1+dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            if pp1>end:
                pp1=end
            print(p1_name, 'Your score: ',pp1)
            if(reached_end(pp1)):
                print(p1_name, 'won')
                break
        else:
            #player 2 turns
            print(p2_name,'Your turn')
            #ask player2's choice to continue
            c=input('Press 1 to continue, 0 to quit: ')
            if c==0:
                print(p1.name,'scored',pp1)
                print(p2_name,'scored',pp2)
                print('Quiting the game, thanks for playing')
                break
            #generate a random number from 1,2, 3,4,5,6
            dice=random.randint(1,6)
            print('Dice showed: ', dice)
            pp2=pp2+dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            if pp2>end:
                pp2=end
            print(p2_name, 'Your score: ',pp2)
            if(reached_end(pp2)):
                print(p2_name, 'won')
                break
        turn=turn+1
                
show_board()
play()