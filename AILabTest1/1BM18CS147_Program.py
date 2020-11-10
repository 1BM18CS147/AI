# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:33:33 2020

@author: Arpana M R
"""

# Left and right move function
def Right(state):
    if state[0]=='L':
        state[0]='R'
        print("Moving to right state:",state)
    return state

def Left(state):
    if state[0]=='R':
        state[0]='L'
        print("Moving to left state:",state)
    return state

# Suck dirt
def suckDirt(state):
    if(state[0]=='R' and state[3]=='Dirty'):
        if(state[4]=='0'):
            state[4]='1'
        elif(state[4]=='1'):
            state[4]='2'
            state[3]='Clean'
    

    elif(state[0]=='L' and state[1]=='Dirty'):
        if(state[2]=='0'):
            state[2]='1'
        elif(state[2]=='1'):
            state[2]='2'
            state[1]='Clean'
        
        
    print("Sucking Dirt:",state)
    
    return state

# this function checks if the place has been cleaned twice, and then says the place is clean
def vaccumCleaner(state):
    if(state[1]=='Clean' and state[3]=='Clean'):
        print("All Cleaned!!")
    else:
         while(True):
            if state[1]=='Clean' and state[3]=='Clean' and state[2]=='2' and state[4]=='2':
                print("All Cleaned!!")
                break
            if(state[0]=='L'):
                if(state[1]=='Dirty'):
                    state=suckDirt(state)
                if(state[2]=='2'):
                    state=Right(state)
                    
            else:
                if(state[3]=='Dirty'):
                    state=suckDirt(state)
                if(state[4]=='2'):
                    state=Left(state)
    
  
    '''
    the percept sequence is as such
    [which place cleaner is in, if Left place is clean or dirty,how many times it has been clean, if Right place is clean or dirty,how many times it has been clean ]
    a place is clean only if it has been cleaned TWICE
    '''
             
state=['L','Dirty','1','Dirty','0']
print(state)
vaccumCleaner(state)
