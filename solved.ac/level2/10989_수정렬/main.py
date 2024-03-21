import sys
sys.stdin = open('./solved.ac/10989_수정렬/input.txt', 'r')

N = int(input())

for num in sorted([int(input()) for _ in range(N)]):
    print(num)
    
    