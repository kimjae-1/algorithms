import sys
sys.stdin = open('./solved.ac/10816_숫자카드/input.txt', 'r')

N = int(input())
cards = sorted(list(map(int,input().split())))
M = int(input())
cnt_cards = list(map(int,input().split()))

result = []
for cnt in cnt_cards:
    result.append(cards.count(cnt))


print(' '.join(map(str, result)))



# counter
import sys
from collections import Counter

sys.stdin = open('./solved.ac/10816_숫자카드/input.txt', 'r')
input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int,input().split())))
M = int(input())
cnt_cards = list(map(int,input().split()))

C = Counter(cards)
print(' '.join(f'{C[m]}' if m in C else '0' for m in cnt_cards))
