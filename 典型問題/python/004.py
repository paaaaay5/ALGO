H, W = map(int,input().split())

M = [[0] * W for _ in range(H)]
M_H = [0] * H
M_W = [0] * W

for i in range(H):
    A = list(map(int,input().split()))
    for j in range(len(A)):
        M[i][j] = A[j]

#横
for i in range(H):
    M_H[i] = sum(M[i])
#縦
for i in range(H):
    for j in range(W):
        M_W[j] += M[i][j]

for i in range(H):
    ans = []
    for j in range(W):
        ans.append(M_H[i] + M_W[j] - M[i][j])
    print(*ans)