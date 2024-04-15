import sys
from collections import deque

sys.stdin = open('./solved.ac/level3/2606_바이러스/input.txt', 'r')
input = sys.stdin.readline
# 컴퓨터 수 
T = int(input().rstrip())
# 연결된 쌍 개수
C = int(input().rstrip())
# 밤문한 컴퓨터인지
visited = [0]* (T+1)
# adjacency matrix(input)
network = [[] for _ in range(T+1)]
# network 업데이트
for _ in range(C):
    a, b = map(int, input().rstrip().split())
    network[a].append(b)
    network[b].append(a)
 
# 1번 컴퓨터 : 방문    
visited[1] = 1
#
Q = deque([1])
while Q:
    com = Q.popleft()
    for c in network[com]:
        if visited[c] == 0:
            Q.append(c)
            visited[c] = 1

# 1번 컴퓨터 제외           
print(sum(visited)-1)