import sys
sys.stdin = open('./solved.ac/level3/11047_동전/input.txt', 'r')

N,K = map(int,input().split())

lst = sorted([int(input()) for _ in range(N)], reverse = True)

cnt = 0
for c in lst:
    if K == 0:
        break
    cnt += K//c
    K %= c
    
print(cnt)
        
    
    
    
    
    