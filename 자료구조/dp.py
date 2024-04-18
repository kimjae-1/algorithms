memo = {} 
def fibo(n):
    if n == 1 or n == 2:
        return 1
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

fibo(7)


# Top-down
# 재귀를 활용하여 위에서 아래로 값을 구하는 방식

# Bottom-up
