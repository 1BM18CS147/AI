# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 14:24:18 2020

@author: Arpana M R
"""

def Seperator(l):
    l = l.split("(")[1:] 
    l = "(".join(l) 
    l = l.split(")")[:-1] 
    l = ")".join(l)
    ch = l.split(',')
    return ch

    
def Functions(l1,l2):
    return (l1.split("(")[0]==l2.split("(")[0])


def printSolution(sub):
    print("Unification is possible for substitution:")
    ans=[]
    for key, val in sub.items():
        ans.append(key)
        ans.append('/')
        ans.append(val)
      
    #print(ans)
    print('unifier θ= {', end=' ')
    for i in range(len(ans)):
        if(i%3==2 and i!=len(ans)-1):
            print(ans[i],end=',')
        else:
            print(ans[i],end='')
    print(' }')
        
            
    
    
def Unification(l1,l2,const,var):
    
    if(Functions(l1,l2)==False):
        print("Functions dont match Unifcation not possible")
        return
    
    x=Seperator(l1)
    y=Seperator(l2)
    lenx=len(x)
    leny=(len(y))
    if(lenx!=leny):
        print("unequal numer of attributes Unification not possible")
        return
    
    sub=[]
    f=1
    for i in range(len(x)):
        if(x[i] in const and y[i] in const):
            #print("Both not const")
            if (x[i]==y[i]):
                continue
            else:
                print("constant cannot be equated Unification is not possible")
                f=0
                break
        elif(x[i] in const and y[i] in var):
            sub.append([y[i],x[i]])
        elif(x[i] in var and y[i] in const):
            sub.append([x[i],y[i]])
        elif(x[i] in var and y[i] in var):
            sub.append([x[i],y[i]])
    if(f==1):
        d=dict()
        for ele in sub:
            if(ele[0] in d):
                val=d.get(ele[0])
                if(val!=ele[1]):
                    print("Different subsitutions for same variable")
                    print("Unification not possible")
                    return
            else:
               d[ele[0]]=ele[1] 
               
        temp = {val : key for key, val in d.items()} 
        sub = {val : key for key, val in temp.items()} 
       
        printSolution(sub)
        
            


const=list(input("Enter constants : ").split(','))
var=list(input("Enter variables : ").split(','))

l1=input("Enter first sentence : ")
l2=input("Enter second sentence : ")
#l1=['prime(x),g(x)']
#l2=['prime(y),g(11)']
#const=['11','12']
#var=['x','y']
Unification(l1,l2,const,var)

#Seperator(l1)
#Seperator(l2)