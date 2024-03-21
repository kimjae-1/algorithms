import sys

sys.stdin = open('./solved.ac/4153_직각삼각형/input.txt', 'r')


while True:
    lst = sorted(list(map(int,input().split())))
    if sum(lst)== 0:
        break
    c = lst[-1]
    a = lst[0]
    b = lst[1]
    print('right' if c**2 == a**2 + b**2 else 'wrong')
    


    
    