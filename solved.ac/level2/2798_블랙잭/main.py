import sys
from itertools import combinations

sys.stdin = open('./solved.ac/2798_블랙잭/input.txt', 'r')

N,M = map(int,input().split())
lst = list(map(int,input().split()))

lst = [v for v in lst if v<M-3]

mx = 0
for cards in combinations(lst,3):
  if (sum(cards)<M) & (mx<sum(cards)):
    mx = sum(cards)

print(mx)






