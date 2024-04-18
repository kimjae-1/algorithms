import sys
sys.stdin = open('./solved.ac/level3/2579_계단/input.txt', 'r')
input = sys.stdin.readline

# 계단의 개수
T = int(input().rstrip())

stair = [0]*301
for i in range(T):
    stair[i]=int(input())

stair

'''
dp : i 번째 까지 왔을 때의 최댓값

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = (stair[1] + stair[2]) or (stair[0] or stair[2])
DP[4] = stair[0] + stair[1] + stair[3] + stair[4] 혹은 stair[0] + stair[2] + stair[4]
'''
