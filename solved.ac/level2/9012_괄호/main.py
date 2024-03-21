import sys
sys.stdin = open('./solved.ac/9012_괄호/input.txt', 'r')

T = int(input())

for _ in range(T):
    lst = input()
    stack = []
    for i in lst:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                stack.append(i)
                break
            else:
                stack.pop()
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
        
        

