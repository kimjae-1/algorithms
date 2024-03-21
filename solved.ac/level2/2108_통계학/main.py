import sys
sys.stdin = open('./solved.ac/2108_통계학/input.txt', 'r')

N = int(input())

lst = sorted([int(input()) for _ in range(N)])

# avg
print(int(round(sum(lst)/len(lst),0)))

# mid
print(lst[int(N/2)])

# mode
unique = set(lst)
cnt = {i:lst.count(i) for i in unique} 
max_cnt = max(cnt.values())
max_lst = sorted(k for k,v in cnt.items() if v ==max_cnt) 
if len(max_lst)>1:
    print(max_lst[1])
else:
    print(max_lst[0])
    
# range
print(lst[-1] - lst[0])

