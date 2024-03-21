import sys
from collections import deque

sys.stdin = open('./solved.ac/4949_균형/input.txt', 'r')

while True:
    word = input()
    stack = []
    
    if word =='.':
        break
    for w in word:
        if w == '(' or w == '[':
            stack.append(w)
        elif w == ')':
            if stack[-1] == '(' and len(stack) != 0:
                stack.pop()
            else:
                stack.append(w)
                break
        elif w == ']':
            if stack[-1] == '[' and len(stack) != 0:
                stack.pop()
            else:
                stack.append(w)
                break
       
    if len(stack)==0: 
        print('yes')
    else:
        print('no')  
        
        
        
        