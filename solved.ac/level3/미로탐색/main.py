
import sys
from collections import deque
sys.stdin = open('./solved.ac/level3/미로탐색/input.txt', 'r')
input = sys.stdin.readline

N, M = map(int,input().rstrip().split())
case_matrix = []
for _ in range(N):
    case_matrix.append(list(map(int, input().rstrip())))

Q = deque()
Q.append((0, 0))  
while Q:
    row, col = Q.popleft()
    for n_row, n_col in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
        if 0 <= n_row < N and 0 <= n_col < M:
            if case_matrix[n_row][n_col] == 1:
                case_matrix[n_row][n_col] = case_matrix[row][col] + 1  
                Q.append((n_row,n_col))

print(case_matrix[N-1][M-1])
            
    