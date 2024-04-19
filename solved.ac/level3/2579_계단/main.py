import sys
# sys.stdin = open('./solved.ac/level3/2579_계단/input.txt', 'r')
input = sys.stdin.readline

n = int(input())

# 계단의 숫자 초기화
stairs = [0] * 301
for i in range(1, n+1):
    stairs[i] = int(input())
    
# dp 배열 초기화
dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

"""
n-1 계단 : dp[n-3] + stairs[n-1] + stairs[n]
n-2 계단 : dp[n-2] + stairs[n]    
"""
# 점화식
for i in range(4, n+1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

print(dp[n])