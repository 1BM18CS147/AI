# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 14:24:18 2020

@author: Arpana M R
"""

def Seperator(l):
    ch=[]
    for ele in l:
        s=""
        c=list(ele)
        opening=['(']
        closing=[')']
        Close=[i for i in range(len(c)) if c[i] in closing]
        Open=[i for i in range(len(c)) if c[i] in opening]
        for k in range(len(Close)):
            j=Close[k]
            i=Open[k]
            temp=c[i+1:j]
            st=s.join(temp)
            ch.append(st)
    
    return ch

def printSolution(sub):
    print("Unification is possible for substitution:")
    ans=[]
    for ele in sub:
        if (ele[0]=='1'):
            
            ans.append(ele[1])
            ans.append('/')
            ans.append(ele[2])
        else:
            ans.append(ele[1])
            ans.append('=')
            ans.append(ele[2])
    #print(ans)
    print('unifier θ= {', end=' ')
    for i in range(len(ans)):
        if(i%3==2 and i!=len(ans)-1):
            print(ans[i],end=',')
        else:
            print(ans[i],end='')
    print(' }')
        
            
    
    
def Unification(l1,l2,const,var):
    x=Seperator(l1)
    y=Seperator(l2)
    sub=[]
    f=1
    for i in range(len(x)):
        if(x[i] in const and y[i] in const):
            #print("Both not const")
            if (x[i]==y[i]):
                continue
            else:
                print("Unification is not possible")
                f=0
                break
        elif(x[i] in const and y[i] in var):
            sub.append(['1',y[i],x[i]])
        elif(x[i] in var and y[i] in const):
            sub.append(['1',x[i],y[i]])
        elif(x[i] in var and y[i] in var):
            sub.append(['2',x[i],y[i]])
    if(f==1):
        printSolution(sub)
            


const=list(input("Enter constants : ").split(','))
var=list(input("Enter variables : ").split(','))

l1=list(input("Enter first sentence with expressions seperated by commas : ").split(','))
l2=list(input("Enter second sentence with expressions seperated by commas : ").split(','))
#l1=['prime(x),g(x)']
#l2=['prime(y),g(11)']
#const=['11','12']
#var=['x','y']
Unification(l1,l2,const,var)