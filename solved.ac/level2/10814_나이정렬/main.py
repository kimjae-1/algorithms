import sys
sys.stdin = open('./solved.ac/10814_나이정렬/input.txt', 'r')

N = int(input())

lst = []
for i in range(N):
    lst.append(list(input().split()) + [N-(N-i)])
    

lst = sorted(lst, key = lambda x : (int(x[0]),x[2]))

for i in lst:
    print(i[0], i[1])
