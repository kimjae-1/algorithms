import sys
sys.stdin = open('./solved.ac/10773_제로/input.txt', 'r')

K = int(input())
lst = list(int(input()) for _ in range(K))

result = []
for num in lst:
    if num !=0:
        result.append(num)
    else:
        result.pop()
        
print(sum(result))



