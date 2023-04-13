N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split())) + [L]


def ok(l):
    left_ind = 0
    for i in range(K+1):
        right_ind = left_ind
        while (right_ind < len(A) and A[right_ind] - A[left_ind] < l):
            right_ind += 1
        if right_ind == len(A):
            return False
        left_ind = right_ind
    return True

bottom, top = 0, L+1

while (top - bottom) > 1:
    mid = (top + bottom)//2
    if ok(mid):
        bottom = mid
    else:
        top = mid

print(bottom)