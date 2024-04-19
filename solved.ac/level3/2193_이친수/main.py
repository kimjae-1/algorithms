import sys
# sys.stdin = open('./solved.ac/level3/2193_이친수/input.txt', 'r')
input = sys.stdin.readline

N = int(input())

case = dict()

case[1] = 1
case[2] = 1

for i in range(3, N + 1):
    if i not in case:
        case[i] = case[i-2] + case[i-1]

print(case[N])
