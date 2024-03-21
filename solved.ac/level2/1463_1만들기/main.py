import sys
sys.stdin = open('./solved.ac/1463_1만들기/input.txt', 'r')

X = int(input())

cnt = 0
while X != 1:
    if X % 3 == 0:
        X /= 3
        cnt += 1
    elif (X-1) % 3 == 0:
        X -= 1
        cnt += 1
    elif X % 2 == 0:
        X /= 2
        cnt += 1
    elif (X-1) % 2 == 0:
        X -= 1
        cnt += 1

print(cnt)
    