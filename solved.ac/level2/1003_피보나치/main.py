import sys
sys.stdin = open('./solved.ac/1003_피보나치/input.txt', 'r')

T = int(input())

def fibonacci(n):
    if n == 0:
        return 0
    elif n  == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)