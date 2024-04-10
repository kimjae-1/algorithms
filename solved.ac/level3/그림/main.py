import sys
from collections import deque
# sys.stdin = open('./solved.ac/level3/그림/input.txt', 'r')
input = sys.stdin.readline

def BFS(row,col):
    Q = deque()
    Q.append((row,col))
    case_matrix[row][col] = 2
    s = 1
    while Q:
        row, col = Q.popleft()
        for n_row, n_col in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            # 좌표 벗어나는지?
            if 0 <= n_row < n and 0 <= n_col < m:
                # 방문하지 않은 영역이라면?
                if case_matrix[n_row][n_col] == 1:
                    case_matrix[n_row][n_col] = 2
                    Q.append((n_row,n_col))
                    s += 1
    return 1,s

cnt = 0
space = []
n, m = map(int,input().rstrip().split()) # 세로, 가로
case_matrix = [list(map(int,input().rstrip().split())) for _ in range(n)] # input

for row in range(n):
    for col in range(m):
        if case_matrix[row][col] == 1:
            c, s = BFS(row,col)
            cnt += c
            space.append(s)
            
print(cnt)
print(max(space) if cnt >= 1 else 0)
