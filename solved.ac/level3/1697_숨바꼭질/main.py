import sys
from collections import deque
# sys.stdin = open('./solved.ac/level3/1697_숨바꼭질/input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
MAX = 100001
visited = [0] * MAX

Q = deque()
Q.append(N)
while Q:
    now = Q.popleft()
    if now == K:
        break
    for move in (now - 1, now + 1, now * 2):
        if 0 <= move < MAX:
            if visited[move] == 0:
                visited[move] = visited[now] + 1
                Q.append(move)
    

print(visited[now])

