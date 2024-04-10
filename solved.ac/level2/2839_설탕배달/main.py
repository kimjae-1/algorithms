import sys
sys.stdin = open('./solved.ac/2839_설탕배달/input.txt', 'r')

N = int(input())

cnt = 0

while N >= 0:
    if N%5==0: # 5로 나누어 떨어진다면,
        cnt += (N//5)
        print(cnt)
        break # break
    N -= 3 #  -3 
    cnt += 1 # cnt에 반영
else:
    print(-1)
    
