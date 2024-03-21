import sys
sys.stdin = open('./solved.ac/1259_팰린드롬수/input.txt', 'r')

while True:
    n = input()
    if n == '0':
        break
    if n == n[::-1]:
        print('yes')
    else:
        print('no')
        