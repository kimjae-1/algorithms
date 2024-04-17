import sys
from collections import deque
# sys.stdin = open('./solved.ac/level3/11659_구간합/input.txt', 'r')
input = sys.stdin.readline

# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

N, M = map(int,input().rstrip().split()) # N : 수의 개수 / M : 합을 구해야 하는 횟수
lst = list(map(int,input().rstrip().split()))

for n in range(N-1):
    lst[n+1] += lst[n]

lst = [0] + lst
    
for _ in range(M):
    i, j = map(int,input().rstrip().split())
    print(lst[j] - lst[i-1])
