import sys
from collections import deque
# sys.stdin = open('./solved.ac/level3/21736_헌내기/input.txt', 'r')
input = sys.stdin.readline

# Input
N, M = map(int, input().rstrip().split())
# Matirx
matrix = [[i for i in input().rstrip()] for _ in range(N)]
# 도연 좌표 구하기
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'I':
            coor = (i,j)
            break
# count 초기화
cnt = 0
# 방문 기록
Q = deque()
Q.append(coor)
while Q:
    row, col = Q.popleft()
    for n_row, n_col in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
        # X 일때는 막혀서 못지나가므로...
        if 0 <= n_row < N and 0 <= n_col < M and matrix[n_row][n_col] != 'X':
            # 지나간 후 1로 표시, 해당 좌표 append
            if matrix[n_row][n_col] == 'O':
                matrix[n_row][n_col] = 1
                Q.append((n_row,n_col))
            # 친구 만나면 cnt + 1, 해당 좌표 append
            elif matrix[n_row][n_col] == 'P':
                cnt += 1
                matrix[n_row][n_col] = 1
                Q.append((n_row,n_col))
               
print(cnt if cnt > 0 else 'TT')

  

