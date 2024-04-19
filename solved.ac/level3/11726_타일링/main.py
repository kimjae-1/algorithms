import sys
# sys.stdin = open('./solved.ac/level3/11726_타일링/input.txt', 'r')
input = sys.stdin.readline

n = int(input().rstrip())

case = dict()

case[1] = 1
case[2] = 2

for i in range(3,n+1):
    if i not in case:
        case[i] = case[i-2] + case[i-1]

print(case[n]%10007)


