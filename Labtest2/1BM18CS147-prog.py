# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 14:39:10 2020

@author: Arpana M R
"""

def Seperate(li):
    li = li.split("(")[1:] 
    li = "(".join(li) 
    li = li.split(")")[:-1] 
    li = ")".join(li)
    x = li.split(',')
    return x

    
def PredicateCheck(s1,s2):
    return (s1.split("(")[0]==s2.split("(")[0])


def printSolution(subs):
    print("Unification is possible")
    print("Substitution:",end=" ")
    subans=[]
    for k, v in subs.items():
        subans.append(k)
        subans.append('/')
        subans.append(v)
  
    print('unifier θ= {', end=' ')
    for i in range(len(subans)):
        if(i%3==2 and i!=len(subans)-1):
            print(subans[i],end=',')
        else:
            print(subans[i],end='')
    print(' }')
        
            
    
    
def Unify(s1,s2,const,var):
    
    if(PredicateCheck(s1,s2)==False):
        print("Predicates dont match ")
        print("Unifcation not possible")
        return
    
    a=Seperate(s1)
    b=Seperate(s2)
    len1=len(a)
    len2=len(b)
    if(len1!=len2):
        print("Mismatch in number of arguments")
        print("Unification not possible")
        return
    
    subs=[]
    flag=1
    for i in range(len(a)):
        if(a[i] in const and b[i] in const):
            if (a[i]==b[i]):
                continue
            else:
                print("constant cannot be equated")
                print("Unification is not possible")
                flag=0
                break
        elif(a[i] in const and b[i] in var):
            subs.append([b[i],a[i]])
        elif(a[i] in var and b[i] in const):
            subs.append([a[i],b[i]])
        elif(a[i] in var and b[i] in var):
            subs.append([a[i],b[i]])
    if(flag==1):
        d=dict()
        for ele in subs:
            if(ele[0] in d):
                val=d.get(ele[0])
                if(val!=ele[1]):
                    print("Different subsitutions for same variable")
                    print("Unification is not possible")
                    return
            else:
               d[ele[0]]=ele[1] 
               
        t = {val : key for key, val in d.items()} 
        subs = {val : key for key, val in t.items()} 
       
        printSolution(subs)
        

const=list(input("Enter the constants : ").split(','))
var=list(input("Enter the variables : ").split(','))

s1=input("Enter first statement : ")
s2=input("Enter second statement : ")

Unify(s1,s2,const,var)
