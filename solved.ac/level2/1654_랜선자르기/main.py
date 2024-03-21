import sys
sys.stdin = open('./solved.ac/1654_랜선자르기/input.txt', 'r')
input = sys.stdin.readline

K, N = map(int,input().split())
lan = [int(input()) for _ in range(K)]
low = 1
high = max(lan)
while low < high:
    mid = (low+high)//2 + 1
    s = sum([x//mid for x in lan]) #총 몇 개의 lan 선을 만들 수 있는지
    if s >= N:
        low = mid
    else:
        high = mid - 1
print(low)   



