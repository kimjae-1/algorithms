import sys
from collections import deque

sys.stdin = open('./solved.ac/11866_요세푸스/input.txt', 'r')

N,K = map(int,input().split())

dq = deque([i for i in range(1,N+1)])
result = []
while len(dq) != 0:
    for _ in range(K-1):
        dq.append(dq.popleft())
    result.append(dq.popleft())
    
print("<", end='')
print(', '.join(map(str,result)), end='')
print(">")



