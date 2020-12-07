# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:04:09 2020

@author: Arpana M R
"""

#Negating the Query
def NegQuery(Q):
    Q=re.sub("\^","x",Q)
    Q=re.sub("V","^",Q)
    Q=re.sub("x","V",Q)
    
    Q=re.sub("~p","1",Q)
    Q=re.sub("~q","2",Q)
    Q=re.sub("~r","3",Q)
    Q=re.sub("~s","4",Q)
    
    
    Q=re.sub("p","~p",Q)
    Q=re.sub("q","~q",Q)
    Q=re.sub("r","~r",Q)
    Q=re.sub("s","~s",Q)
    
    Q=re.sub("1","p",Q)
    Q=re.sub("2","q",Q)
    Q=re.sub("3","r",Q)
    Q=re.sub("4","s",Q)
    return Q

    #create a list with complements
def findcomplement(ch):
    ans=[]
    for ele in ch:
        if(ele=='p'):
            ans.append('~p')
        elif(ele=='q'):
            ans.append('~q')
        elif(ele=='r'):
            ans.append('~r')
        elif(ele=='s'):
            ans.append('~s')
        elif(ele=='~p'):
            ans.append('p')
        elif(ele=='~q'):
            ans.append('q')
        elif(ele=='~r'):
            ans.append('r')
        elif(ele=='~s'):
            ans.append('s')
    return ans    

       
def resolve(ch):
    global f
    ans=[]
    for ele in ch:
        c=findcomplement(ele)
        ans.append(c)
        
    
    while(len(ch)!=0 and f!=0):
        print('KB currently is',ch)
        f=0
        #go through the given KN
        #loop 1
        for i in range(len(ch)):
            x=list(ch[i])
            #go through complement of KB
            #loop 2
            for j in range(i+1,len(ans)):
                y=list(ans[j])
                #go through each elemnt which is a realtion in KB
                #loop 3
                for k in range(len(x)):
                    #go through each element which is a realation in complemnt of KB
                    #loop 4
                    for l in range(len(y)):
                        # if complement and KB are same 
                        if(x[k]==y[l]):
                            #pop the elements from ans and ch
                            remove_indices = [i,j]
                            ans = [i for j, i in enumerate(ans) if j not in remove_indices]
                            ch = [i for j, i in enumerate(ch) if j not in remove_indices]
                                                      
                            #if the relation contains more than one , do the following operations
                            if(len(x)==2 or len(y)==2):
                                temp=[]
                                if(len(x)==2):
                                    #append 2nd element if 1st is equal else append 2nd element to temp
                                    if(k==1):
                                        temp.append(x[k-1])
                                    else:
                                        temp.append(x[k+1])
                                    
                                if(len(y)==2):
                                    if(l==1):
                                        z=findcomplement(y)
                                        temp.append(z[l-1])
                                    else:
                                        z=findcomplement(y)
                                        temp.append(z[l+1])
                                    #append the temp to list ch
                                ch.append(temp)
                                    #append the complement to list ans
                                ans.append(findcomplement(temp))
                                
                            #set f=1
                            f=1
                            #break out of loop 4
                            break
                    #break out of loop 3
                    if(f==1):
                        break
                #break out of loop 2
                if(f==1):
                    break
            #break out of loop 1
            if(f==1):
                break                
    if(len(ch)==0):
        print("Succesful!")
    else:
        print("Unsuccessful")
       
                                    
      
def Solution():
    #negate the query
    NegQ=NegQuery(Q)
    #add it to the KB
    KB.append(NegQ)
    #create a list of all the query with space seperating
    ch=[]

    for j in range(len(KB)):
        a=re.split('V', KB[j])
        ch.append(a) 
    
    resolve(ch)


import re 

print("Enter knowledgebase, seperated by commas")
x=input()
KB=re.split('[|^,]',x)
print("Enter Query")
Q=input()
f=1

#KB=['pVq','~pVr','~qVs','~s']
#Q='r'
  


Solution()   
      
     