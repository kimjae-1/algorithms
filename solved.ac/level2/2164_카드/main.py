import sys
from collections import deque

sys.stdin = open('./solved.ac/2164_카드/input.txt', 'r')

from collections import deque
N = int(input())

dq = deque([i for i in range(1,N+1)])
while len(dq) != 1:
    dq.popleft()
    dq.append(dq.popleft())




