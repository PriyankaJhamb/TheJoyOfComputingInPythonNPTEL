# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:40:13 2021

@author: DELL
"""
def rock_paper_scissor(num1, num2, bit1, bit2):
    n1=int(num1[bit1])%3
    n2=int(num2[bit2])%3
    if player1[n1]=="Rock" and player2[n2]=="Paper":
        print("Player 2  won.")
    elif player1[n1]=="Rock" and player2[n2]=="Scissor":
        print("Player 1 won.")
    elif player1[n1]=="Scissor" and player2[n2]=="Rock":
        print("Player 2 won.")
    elif player1[n1]=="Scissor" and player2[n2]=="Paper":
        print("Player 1 won.")
    elif player1[n1]=="Paper" and player2[n2]=="Scissor":
        print("Player 2 won.")
    elif player1[n1]=="Paper" and player2[n2]=="Rock":
        print('Player 1 won.')
    else:
        print("Draw")

player1={0:"Rock", 1:"Paper", 2: "Scissor"}
player2={0:"Paper", 1:"Scissor", 2:"Rock"}

while(1):
    num1=input("Player 1, Enter your number: ")
    num2=input("Player 2, Enter your number: ")
    bit1=int(input("Player 1, Enter your bit position: "))
    bit2=int(input("Player 2, Enter your bit position: "))
    rock_paper_scissor(num1, num2, bit1, bit2)
    ch=input("Do you want to continue? y/n :")
    if ch=="n":
        break
 
