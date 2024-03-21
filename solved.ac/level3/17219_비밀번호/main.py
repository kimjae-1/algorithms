import sys
sys.stdin = open('./solved.ac/level3/17219_비밀번호/input.txt', 'r')
input = sys.stdin.readline

N,M = map(int,(input().split()))

tmp = dict()

for i in range(N):
    path, pw = input().split()
    tmp[path] = pw
    
for m in range(M):
    k = input().strip()
    print(tmp[k])
    
    
