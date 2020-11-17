# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:37:30 2020

@author: Arpana M R
"""

possibilities=[(True,True,True),(True,True,False),(True,False,True),(False,True,True),(False,False,True),(False,True,False),(True,False,False),(False,False,False)]
variables={'p':0,'q':1,'r':2}
knowledgeBase=''
query=''
priority={'v':1,'^':2,'~':3}

def user_input():
    global knowledgeBase,query
    knowledgeBase=(input("Enter the rule:"))
    query=(input("Enter the query:"))
    
def entailment():
    global knowledgeBase,query
    print("The truth Table reference is")
    print('KB    ','alpha')
    print('_'*12)
    for p in possibilities:
        s=evaluatePostfix(toPostfix(knowledgeBase),p)
        f=evaluatePostfix(toPostfix(query),p)
        print(s,'|',f)
        print('_'*12)
        if s and not f:
            return False
    return True
    
def isOperand(o):
    return o.isalpha() and o!='v'

def isLeftParenthesis(o):
    return o =='('

def isRightParenthesis(o):
    return o ==')'

def isEmpty(stack):
    return len(stack)==0

def peek(stack):
    return stack[-1]

def hasLessorEqualPriority(x,y):
    try:
        return priority[x]<=priority[y]
    except KeyError:
        return False
    
def toPostfix(infix):
    Stack=[]
    postfix=''
    for ch in infix:
        if isOperand(ch):
            postfix+=ch
        else:
            if isLeftParenthesis(ch): Stack.append(ch)
            elif isRightParenthesis(ch):
                op=Stack.pop()
                while not isLeftParenthesis(op):
                    postfix +=op
                    op=Stack.pop()
            else:
                while (not isEmpty(Stack)) and hasLessorEqualPriority(ch,peek(Stack)):
                    postfix+=Stack.pop()
                Stack.append(ch)
    while(not isEmpty(Stack)):
        postfix+=Stack.pop()
    return postfix
                    

def evaluatePostfix(expr,c):
    Stack=[]
    for e in expr:
        if isOperand(e):
            Stack.append(c[variables[e]])
        elif e =='~':
            v1=Stack.pop()
            Stack.append(not v1)
        else:
            v1=Stack.pop()
            v2=Stack.pop()
            Stack.append(evaluate(e,v2,v1))
            
    return Stack.pop()
    
def evaluate(e,x,y):
    if e=='^':
        return x and y
    return x or y

user_input()
ans= entailment()
if ans:
    print("The knowledge base entails query")
else:
    print("The knowledge base doesnt not entail query")
            