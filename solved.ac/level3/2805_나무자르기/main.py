import sys
# sys.stdin = open('./solved.ac/level3/2805_나무자르기/input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # 나무 수 / 필요한 나무 길이
trees = list(map(int, input().rstrip().split()))

low = 1
high = max(trees)

while low <= high:
    mid = (low + high) // 2
    total = 0
    for i in trees:
        if i > mid:
            total += i - mid
    if total < M: # 더 잘라야함. mid 높이 낮추기
        high = mid -1
    else: #덜 잘라야함. mid 높이 올리기
        low = mid + 1
    
print(high)


        
        