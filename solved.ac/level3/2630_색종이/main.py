import sys
sys.stdin = open('./solved.ac/level3/2630_색종이/input.txt', 'r')
input = sys.stdin.readline

N = int(input().rstrip())

matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]

white = 0  # 흰색 색종이 개수
blue = 0  # 파란색 색종이 개수

# 2차원 배열이 모두 같은 색으로 이루어졌는지 검사하는 재귀 함수
def valid(matrix):
    global white
    global blue
    l = len(matrix)
    total = l**2

    # 색종이의 총 합을 계산하여 모두 0인 경우 흰색 색종이 개수를 증가시키고, 모두 1인 경우 파란색 색종이 개수를 증가
    s = 0
    for row in matrix:
        s += sum(r for r in row)
    if s == 0 or s == total:
        if matrix[0][0]:
            blue += 1
        else:
            white += 1
    else:
        # 색종이를 4등분하여 각각에 대해 재귀적으로 검사.
        valid([a[:l//2] for a in matrix[:l//2]])
        valid([a[l//2:] for a in matrix[:l//2]])
        valid([a[:l//2] for a in matrix[l//2:]])
        valid([a[l//2:] for a in matrix[l//2:]])


# valid 함수 호출하여 흰색 색종이 개수와 파란색 색종이 개수 계산
valid(matrix)
print(white)
print(blue)
