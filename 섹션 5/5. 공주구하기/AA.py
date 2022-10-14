#공주 구하기
#success

from collections import deque
m, n = map(int, input().split())
'''
m = 8
n = 3
'''
A = list(range(1, m+1))
A= deque(A)
cnt = 0

while len(A) > 1:
    cnt += 1
    a = A.popleft()
    if cnt == n:
        cnt = 0
    else:
        A.append(a)

print(A[0])
