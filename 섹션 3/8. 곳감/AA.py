# 곳감(모래시계)
# solved(sol)

n=int(input())
A=[list(map(int, input().split())) for _ in range(n)]
'''
n = 5
A = [[10,13,10,12,15],
    [12,39,30,23,11],
    [11,25,50,53,15],
    [19,27,29,37,27],
    [19,13,30,13,19]]
'''

k = int(input())

for each in range(k):
    h, t, l  = map(int, input().split())
    if t == 0:
        for _ in range(l):
            A[h-1].append(A[h-1].pop(0))
    else:
        for _ in range(l):
            A[h-1].insert(0, A[h-1].pop())

center = n//2
idx_up  = n -1
idx_down = 0
ans = 0

for i in range(n):
    for j in range(idx_down, idx_up +1):
        ans += A[i][j]
    if i < center:
        idx_down = idx_down + 1
        idx_up  = idx_up - 1
    else:
        idx_down  = idx_down - 1
        idx_up = idx_up + 1

print(ans)
