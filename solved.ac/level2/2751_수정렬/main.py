import sys
sys.stdin = open('./solved.ac/2751_수정렬/input.txt', 'r')

N = int(input())

lst = sorted([int(input()) for _ in range(N)])

for n in lst:
    print(n)