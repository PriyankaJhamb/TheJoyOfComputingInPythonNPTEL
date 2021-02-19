# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:46:38 2021

@author: Priyanka Jhamb
"""
import random
def choose():
    words=['Reverse','Word','priyanka','Jhamb','Daughter','Sister','Computer','Science','Engineering','Technology']
    pick=random.choice(words)
    return pick
def jumble(words):
    jumbled="".join(random.sample(words, len(words)))
    return jumbled
def thank(p1n,p2n,p1,p2):
    print(p1n,"Your score is : ",p1)
    print(p2n,"Your score is : ",p2)
    print("Thankyou for participating in this game. Have a great day!")
def play():
    p1name=input('Player 1 Name :  ')
    p2name=input("Player 2 Name :  ")
    p1p=0#player 1 points
    p2p=0#player 2 points
    turn=0 
    while 1:
        #computer task
        picked_word=choose()
        #create the question
        qn=jumble(picked_word)
        
        print("Write your answer letters in small but first letter should be capital.")
        print(qn)
        
        if(turn%2!=0):
            print(p1name, "Your turn!")
            answer=input('What is on my mind?')
            if answer==picked_word:
                p1p=p1p+1
                print('Your score is :', p1p)
                turn=turn+1
            else:
                print("Your answer is wrong. I thought: ",picked_word, ". Better luck next time.")
            c=input('Press 1 to continue and 0 to quit.')
            c=int(c)
            if c==0:
                thank(p1name, p2name, p1p, p2p) 
                break
        else:
            print(p2name, "Your turn!")
            answer=input('What is on my mind?')
            if answer==picked_word:
                p2p=p2p+1
                print('Your score is :', p2p)
                turn=turn+1
            else:
                print("Your answer is wrong. I thought: ",picked_word, ". Better luck next time.")
            c=input('Press 1 to continue and 0 to quit.')
            c=int(c)
            if c==0:
                thank(p1name, p2name, p1p, p2p)
                break
            
    
play()

