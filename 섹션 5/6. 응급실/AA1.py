#응급실
#time limit
from collections import deque


n, m = map(int, input().split())
A = list(map(int,input().split()))

A = [(index, val) for index, val in enumerate(A)]
A = deque(A)
cnt = 0

while A:
    check = A.popleft()
    if any(check[1]< x[1] for x in A):
        A.append(check)
    else:
        cnt += 1
        if check[0] == m:
            print(cnt)
            break
