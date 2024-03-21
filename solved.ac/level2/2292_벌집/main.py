import sys

sys.stdin = open('./solved.ac/2292_벌집/input.txt', 'r')

n = int(input())

nums = 1 
cnt = 1
while n > nums :
    nums += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1 
print(cnt)





