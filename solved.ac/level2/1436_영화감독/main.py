import sys
sys.stdin = open('./solved.ac/1436_영화감독/input.txt', 'r')

N = int(input())

devil = 666

cnt = 0
while cnt != N:
    if '666' in str(devil):
        devil += 1
        cnt += 1

print(devil)
        