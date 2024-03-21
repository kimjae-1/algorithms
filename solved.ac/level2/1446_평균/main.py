
N = int(input())
lst = list(map(int, input().split()))
M = max(lst)

new_lst = [i/M*100 for i in lst]

print(sum(new_lst)/N)