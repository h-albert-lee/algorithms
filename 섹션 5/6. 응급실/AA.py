#응급실
#time limit
from collections import deque


n, m = map(int, input().split())
A = list(map(int,input().split()))
'''
n = 5
m = 2
A = [60,50,70,80,90]
'''
A = deque(A)
cnt = 0
ans = A[m]

while A:
    k = A.popleft()
    if k > max(A):
        cnt += 1
        if k == ans:
            break
    else:
        A.append(k)

print(cnt)
