import sys
sys.stdin = open('./solved.ac/11723_집합/input.txt', 'r')

S = set()
M= int(input())

for _ in range(M):
    tmp = input().split()
    if len(tmp) == 1:
        cal = str(tmp)
    else:
        cal, num = tmp
        
    if cal == "add":
        S.add(int(num))

    elif cal == "remove":
        if int(num) in S:
            S.remove(int(num))

    elif cal == "check":
        if int(num) in S:
            print(1)
        else:
            print(0)

    elif cal == "toggle":
        if int(num) in S:
            S.remove(int(num))
        else:
            S.add(int(num))

    elif cal == "all":
        S = set([i for i in range(1,21)])

    else:
        S.clear()

   