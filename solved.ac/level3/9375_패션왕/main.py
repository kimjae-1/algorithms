import sys
from collections import Counter
sys.stdin = open('./solved.ac/level3/9375_패션왕/input.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    tmp = []

    for _ in range(n):
        clo, typ = input().split()
        tmp.append(typ)
        
    test = Counter(tmp)
    cnt = 1
    
    for k in test:
        cnt *= test[k] +1
    
    print(cnt -1)



            
 
