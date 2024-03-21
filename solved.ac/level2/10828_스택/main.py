import sys
sys.stdin = open('./solved.ac/10828_스택/input.txt', 'r')

N = int(input())

lst = [input() for _ in range(N)]
stack = []
for l in lst:
    if 'push' in l.split()[0]:
        stack.append(int(l.split()[1]))
    elif 'top' == l:
        print(stack[-1]) if stack else print(-1)
    elif 'size' == l:
        print(len(stack))
    elif 'empty' == l:
        print(0) if stack else print(1)
    elif 'pop' == l:
        print(stack.pop()) if stack else print(-1)