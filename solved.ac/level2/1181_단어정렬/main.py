import sys
sys.stdin = open('./solved.ac/1181_단어정렬/input.txt', 'r')

N = int(input())  


lst = [input() for _ in range(N)]

lst = sorted(list(set(lst)))

lst.sort(key = len)

for i in lst:
    print(i)