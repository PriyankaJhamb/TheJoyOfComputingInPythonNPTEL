# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:59:22 2021

@author: DELL
"""
import random
movies=["MATRIX", "JUNGLEBOOK", "ANAND"]
def unlock(mf_qn,picked_m,let):
    mq=list(mf_qn)
    letters=list(picked_m)
    n=len(picked_m)
    temp=[]
    for i in range(n):
        if letters[i]==let or letters[i]==' ':
            temp.append(letters[i])
        elif mq[i]=='_':
            temp.append("_")
        else:
            temp.append(letters[i])
    qn=''.join(str(x) for x in temp)
    return qn
            
    

def create_question(picked_movie):
    n=len(picked_movie)
    letters=list(picked_movie)
    temp=[]
    for i in range(n):
        if letters[i]==" ":
            temp.append(" ")
        else:
            temp.append("_")
    qn=''.join(str(x) for x in temp)
    return qn
  
def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
    

    
def play():
    p1name=input("Player 1! Please enter your name: ")
    p2name=input("Player 2! Please enter your name: ")
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
       
        if turn%2==0:
            #player 1
            print(p1name,' Your turn ')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said_person=True
            max_turn=0
            while not_said_person:
                letter=input('Your Letter: ')
                if(is_present(letter, picked_movie)):
                     #unlock
                     modified_qn=unlock(modified_qn,picked_movie,letter)
                     print(modified_qn)
                     d=int(input("Press 1 to guess the movie or 0 to unlock the other letter: "))
                     if d==1:
                         answer=input("Your answer: ")
                         if answer==picked_movie:
                             pp1=pp1+1
                             print("Your answer is correct.")
                             not_said_person=False
                             print(p1name,"Your score is: ",pp1)
                         else:
                             max_turn=max_turn+1
                             print("Your answer is wrong. Try again.") 
                             if max_turn==2:
                                  print("Max guess has done by you.")
                                  not_said_person=False
                                  
                                  
                               
                else:
                     print(letter, 'not found')
                     max_turn=max_turn+1
                     if max_turn==2:
                          print("Max guess has done by you.")
                          not_said_person=False
                        
                     else:
                         c=int(input("Press 1 to continue or 0 to quit:"))
                         if c==0:
                             print(p1name, 'Your score: ',pp1)
                             print(p2name, 'Your score: ',pp2)
                             print('Thanks for playing guys. \n Have a nice day')
                             not_said_person=False
                             willing=False
        else:
            #player 2
            print(p2name,' Your turn ')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            max_turn=0
            while not_said:
                letter=input('Your Letter: ')
                if(is_present(letter, picked_movie)):
                     #unlock
                     modified_qn=unlock(modified_qn,picked_movie,letter)
                     print(modified_qn)
                     d=int(input("Press 1 to guess the movie or 0 to unlock the other letter: "))
                     if d==1:
                         answer=input("Your answer: ")
                         if answer==picked_movie:
                             pp2=pp2+1
                             print("Your answer is correct.")
                             not_said=False
                             print(p2name,"Your score is: ",pp2)
                         else:
                             max_turn=max_turn+1
                             print("Your answer is wrong. Try again.") 
                             if max_turn==2:
                                 print("Max guess has done by you.")
                                 not_said=False
                                                         
                else:
                     print(letter, 'not found')
                     max_turn=max_turn+1
                     if max_turn==2:
                         print("Max guess has done by you.")
                         not_said=False
                         
                     else:
                         c=int(input("Press 1 to continue or 0 to quit:"))
                         if c==0:
                             print(p1name, 'Your score: ',pp1)
                             print(p2name, 'Your score: ',pp2)
                             print('Thanks for playing. \n Have a nice day')
                             not_said=False
                             willing=False
                     #if else ends
        turn=turn+1
           
           
           
                     
                 


play()
        



