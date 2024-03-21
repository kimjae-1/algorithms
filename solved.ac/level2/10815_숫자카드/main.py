import sys
sys.stdin = open('./solved.ac/level2/10815_숫자카드/input.txt', 'r')
input = sys.stdin.readline

N = int(input())
card_lst = sorted(list(map(int,input().split())))
M = int(input())
check_lst = list(map(int,input().split()))

def bs(x):
    low = 0
    high = N-1

    while low <= high:
        mid = (low+high)//2
        if card_lst[mid] == x:
            return 1
        elif x < card_lst[mid]:
            high = mid -1
        else:
            low = mid + 1
    
    return 0

print(' '.join(map(str,[bs(i) for i in check_lst])))


        