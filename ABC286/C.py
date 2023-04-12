N, A, B = map(int,input().split())
S = input()
ans = N * B
for i in range(N):
    cost  = i*A
    for j in range(N):
        op = N-1-j
        if op < j:
            if S[(i+j)%N] !=S[(i+op)%N]:
                cost += B
    ans = min(cost,ans)
print(ans)