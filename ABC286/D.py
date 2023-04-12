N,X = map(int,input().split())
coins = []
for i in range(N):
    A, B = map(int,input().split())
    for j in range(B):
        coins.append(A)

result = [False] * (X+1)
result[0] = True
r2 = result.copy()

for c in coins:
    for amnt in range(len(result)):
        if (amnt - c >= 0):    
            if r2[amnt - c]:
                result[amnt] =True
    r2 = result.copy()

if result[-1]:
	print("Yes")
else:
  	print("No")