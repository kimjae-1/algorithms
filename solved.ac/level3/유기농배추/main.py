import sys
from collections import deque
sys.stdin = open('./solved.ac/level3/유기농배추/input.txt', 'r')
input = sys.stdin.readline

T = int(input().rstrup())
M,N,K = map(int,input().rstrip().split())
case_matrix = [[0] * M for _ in range(N)]
for _ in range(K):
    col, row = map(int,input().rstrip().split())
    case_matrix[row][col] = 1
    
    

def BFS(row, col):
    Q = deque()
    Q.append((row,col))
    case_matrix[row][col] = 2
    while Q:
        row, col = Q.popleft()
        for n_row