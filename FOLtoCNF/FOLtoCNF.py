# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:27:35 2020

@author: Arpana M R
"""
import re

def getAttributes(st):
    expr = '\([^)]+\)'
    matches = re.findall(expr, st)
    return [m for m in str(matches) if m.isalpha()]

def getPredicates(st):
    expr = '[a-z~]+\([A-Za-z,]+\)'
    return re.findall(expr, st)

def DeMorgan(x):
    st = ''.join(list(x).copy())
    st = st.replace('~~','')
    flag = '[' in st
    st = st.replace('~[','')
    st = st.strip(']')
    for predicate in getPredicates(st):
        st = st.replace(predicate, f'~{predicate}')
    s = list(st)
    for i, c in enumerate(st):
        if c == '|':
            s[i] = '&'
        elif c == '&':
            s[i] = '|'
    st = ''.join(s)    
    st = st.replace('~~','')
    return f'[{st}]' if flag else st

def Skolemization(x):
    SKOLEM_CONSTANTS = [f'{chr(c)}' for c in range(ord('A'), ord('Z')+1)]
    stmt = ''.join(list(x).copy())
    matches = re.findall('[∀∃].', stmt)
    for match in matches[::-1]:
        stmt = stmt.replace(match, '')
        stmts = re.findall('\[\[[^]]+\]]', stmt)
        for s in stmts:
            stmt = stmt.replace(s, s[1:-1])
        for predicate in getPredicates(stmt):
            attributes = getAttributes(predicate)
            if ''.join(attributes).islower():
                stmt = stmt.replace(match[1],SKOLEM_CONSTANTS.pop(0))
            else:
                aU = [a for a in attributes if not a.islower()][0]
                stmt = stmt.replace(aU, f'{SKOLEM_CONSTANTS.pop(0)}({match[1]})')
    return stmt
    
def toCNF(l):
    stmt = l.replace("<=>", "_")
    while '_' in stmt:
        i = stmt.index('_')
        new_stmt = '[' + stmt[:i] + '=>' + stmt[i+1:] + ']&['+ stmt[i+1:] + '=>' + stmt[:i] + ']'
        stmt = new_stmt
    stmt = stmt.replace("=>", "-")
    expr = '\[([^]]+)\]'
    stmts = re.findall(expr, stmt)
    for i, s in enumerate(stmts):
        if '[' in s and ']' not in s:
            stmts[i] += ']'
    for s in stmts:
        stmt = stmt.replace(s, toCNF(s))
    while '-' in stmt:
        i = stmt.index('-')
        br = stmt.index('[') if '[' in stmt else 0
        new_stmt = '~' + stmt[br:i] + '|' + stmt[i+1:]
        stmt = stmt[:br] + new_stmt if br > 0 else new_stmt
    while '~∀' in stmt:
        i = stmt.index('~∀')
        stmt = list(stmt)
        stmt[i], stmt[i+1], stmt[i+2] = '∃', stmt[i+2], '~'
        stmt = ''.join(stmt)
    while '~∃' in stmt:
        i = stmt.index('~∃')
        s = list(stmt)
        s[i], s[i+1], s[i+2] = '∀', s[i+2], '~'
        stmt = ''.join(s)
    stmt = stmt.replace('~[∀','[~∀')
    stmt = stmt.replace('~[∃','[~∃')
    expr = '(~[∀|∃].)'
    stmts = re.findall(expr, stmt)
    for s in stmts:
        stmt = stmt.replace(s, toCNF(s))
    expr = '~\[[^]]+\]'
    stmts = re.findall(expr, stmt)
    for s in stmts:
        stmt = stmt.replace(s, DeMorgan(s))
    return stmt

l=input("Enter FOL sentence : ")

ans=toCNF(l)

var='∃'
var2='∀'
if var or var2 in ans:
    ans=Skolemization(ans)
print("The CNF form is ",ans)  
#^-and
#v-or
#~-not
#=> implies
#<=> double implications
#∀ forall
#∃ there exists