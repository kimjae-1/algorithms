import sys
from collections import deque
sys.stdin = open('./solved.ac/10845_큐/input.txt', 'r')

N = int(input())

lst = [input() for _ in range(N)]
dq = deque()

for l in lst:
    if 'push' in l.split()[0]:
        dq.append(int(l.split()[1]))
    elif l == 'pop':
        print(-1) if len(dq) == 0 else dq.popleft()  
    elif l =='size':
        print(len(dq))
    elif l == 'empty':
        print(1) if len(dq) == 0 else print(0)
    elif l =='front':
        print(int(dq[0])) if len(dq) != 0 else print(-1)
    elif l == 'back':
        print(int(dq[-1])) if len(dq) != 0 else print(-1)
        
        
       