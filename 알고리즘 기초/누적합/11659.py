#구간합 구하기 4
#success


import sys
m, n = map(int,sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

psum = [0]*m
for i in range(m):
    if i == 0:
        psum[i] = A[i]
    else:
        psum[i] = psum[i-1] + A[i]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a==1:
        ans = psum[b-1]
    else:
        ans = psum[b-1] - psum[a-2]
    print(ans)
    
