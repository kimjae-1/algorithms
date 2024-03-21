import sys
from collections import deque
sys.stdin = open('./solved.ac/10866_덱/input.txt', 'r')

N = int(input())
lst = [input() for _ in range(N)]
dq = deque()

for l in lst:
    if l.split()[0] == 'push_front':
        dq.appendleft(int(l.split()[1]))
    elif l.split()[0] == 'push_back':
        dq.append(int(l.split()[1]))
    elif l == 'pop_front':
        print(dq.popleft()) if dq else print(-1)
    elif l =='pop_back':
        print(dq.pop()) if dq else print(-1)
    elif l == 'size':
        print(len(dq))
    elif l == 'empty':
        print(0) if dq else print(1)
    elif l == 'front':
        print(dq[0]) if dq else print(-1)
    elif l == 'back':
        print(dq[-1]) if dq else print(-1)
        
    
