import sys
sys.stdin = open('./solved.ac/1018_체스판/input.txt', 'r')

N, M = map(int, input().split()) 
data = []
for _ in range(N):
    data.append(input())
    
for i in range(N-7):
    for j in range(M-7):
        tmp = 


















print(data)

N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))




