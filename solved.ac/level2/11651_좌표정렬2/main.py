import sys
sys.stdin = open('./solved.ac/11651_좌표정렬2/input.txt', 'r')

N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]
lst = sorted(lst,key = lambda x : (x[1],x[0]))
    
for l in lst:
    print(l[0],l[1])
    
    
