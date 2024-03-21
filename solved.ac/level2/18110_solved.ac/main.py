import sys
sys.stdin = open('./solved.ac/18110_solved.ac/input.txt', 'r')

n = int(input())
lst = sorted([int(input()) for _ in range(n)])

if lst:
    except_num = round(len(lst)*0.15)
    tmp = lst[except_num: n - except_num]
    print(round(sum(tmp)/len(tmp)))
else:
    print(0)
    
