import sys
sys.stdin = open('./solved.ac/11650_좌표정렬/input.txt', 'r')

N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]
    
lst = sorted(lst, key = lambda x : (x[0],x[1]))

for l in lst:
    print(l[0],l[1])
    
