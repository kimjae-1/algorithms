import sys
sys.stdin = open('./solved.ac/11050_이항계수/input.txt', 'r')

input = sys.stdin.readline

N,K = map(int,input().split())

s = 1
for i in range(K):
    s *= (N-i)
    
m = 1
for j in range(K):
    m *= (j+1)
    
print(int(s/m))


