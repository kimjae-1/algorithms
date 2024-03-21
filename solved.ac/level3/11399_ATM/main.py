import sys
sys.stdin = open('./solved.ac/level3/11399_ATM/input.txt', 'r')

N = int(input())
lst = sorted(list(map(int,input().split())),reverse = True)

time = []
for i in range(N):
    time.append((i+1) * lst[i])
    
print(sum(time))
    
    
    