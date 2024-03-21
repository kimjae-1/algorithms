import sys
sys.stdin = open('./solved.ac/level3/1620_포켓몬/input.txt', 'r')
input = sys.stdin.readline

N,M = map(int, input().split())
num_dict = {}
pocketmon_dict = {}

for i in range(N):
    name = input().rstrip()
    num_dict[i+1] = name
    pocketmon_dict[name] = i+1


for _ in range(M):
    data = input().rstrip()
    if data.isdigit():
        print(num_dict[int(data)])
    else:
        print(pocketmon_dict[data])
      


