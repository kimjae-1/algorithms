import sys
sys.stdin = open('./solved.ac/level2/1654_랜선자르기/input.txt', 'r')
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





K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
low = 1
high = max(lan)

while low <= high:  # 이분 탐색 시작
    mid = (low + high) // 2  # 중간 길이 계산
    count = sum([x // mid for x in lan])  # 현재 길이로 만들 수 있는 랜선의 개수 계산
    
    if count >= N:  # 현재 길이로 만들 수 있는 랜선의 개수가 N보다 많거나 같으면
        low = mid + 1  # 길이를 늘려서 더 큰 범위를 탐색
    else:  # 현재 길이로 만들 수 있는 랜선의 개수가 N보다 작으면
        high = mid - 1  # 길이를 줄여서 더 작은 범위를 탐색

print(high)  # 최대 길이 출력



