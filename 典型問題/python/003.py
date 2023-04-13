import sys
sys.setrecursionlimit(10**6)
N = int(input())

al = [[] for _ in range(N)]

for i in range(N-1):
    A,B = map(int,input().split())
    A-=1
    B-=1
    al[A].append(B)
    al[B].append(A)

dist = [0] * N

def dfs(x,last=-1):
    global dist
    for to in al[x]:
        if to == last:
            continue
        dist[to] = dist[x] + 1
        dfs(to,x)

dfs(0)
max_dist = max(dist)
fartest = dist.index(max_dist)

dist = [0] * N
dfs(fartest)
print(max(dist) + 1)