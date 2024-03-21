import sys
sys.stdin = open('./solved.ac/2869_달팽이/input.txt', 'r')

# 낮 A미터 / 밤 B 미터 / 높이 V 미터

A,B,V = map(int,input().split())


if (V - B) % (A - B) == 0:
    print((V - B) // (A - B))
else:
    print((V - B) // (A - B) + 1)
    
    

