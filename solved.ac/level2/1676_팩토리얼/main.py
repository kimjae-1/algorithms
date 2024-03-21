import sys
sys.stdin = open('./solved.ac/1676_팩토리얼/input.txt', 'r')

N = int(input())

result = 1
for i in range(N):
    result *= (i+1)

cnt = 0
while str(result)[-1]=='0':
    cnt += 1
    result = str(result)[:-1]

print(cnt)


