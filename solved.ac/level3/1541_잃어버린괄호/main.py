import sys
# sys.stdin = open('./solved.ac/level3/1541_잃어버린괄호/input.txt', 'r')
input = sys.stdin.readline

case = input().rstrip().split('-')

tmp = []
for c in case:
    cnt = 0
    for element in c.split('+'):
        cnt += int(element)
    tmp.append(cnt)
        
answer = tmp[0]
for num in tmp[1:]:
    answer -= num
    
print(answer)
