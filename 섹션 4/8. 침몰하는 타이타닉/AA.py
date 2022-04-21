#침몰하는 타이타닉
#solved(sol)
from collections import deque

n, m = map(int, input().split())
M = list(map(int, input().split()))
'''
n = 10
m = 150
M = [86,95,107,67,38,49,116,22,78,53]
'''
cnt = 0
M.sort()
M = deque(M)

while M:
    if len(M) == 1:
        cnt += 1
        break

    if M[0] + M[-1] > m:
        M.pop()
        cnt += 1
    else:
        M.popleft()
        M.pop()
        cnt += 1

print(cnt)
