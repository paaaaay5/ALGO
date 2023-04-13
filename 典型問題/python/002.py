from itertools import combinations

N = int(input())

if N % 2 == 1:
    exit()

def check(opens):
    l =0
    r = 0
    s = ''
    for i in range(N):
        if i in opens:
            l+=1
            s += '('
        else:
            r+=1
            s += ')'
        if r > l:
            return
    print(s)

for opens in combinations(list(range(N)), N//2):
    check(opens)