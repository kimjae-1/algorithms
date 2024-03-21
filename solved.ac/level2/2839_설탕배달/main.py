import sys
sys.stdin = open('./solved.ac/2839_설탕배달/input.txt', 'r')

N = int(input())

cnt = 0

while N >= 0:
    if N%5==0:
        cnt += (N//5)
        print(cnt)
        break
    N -= 3
    cnt += 1
else:
    print(-1)
    
