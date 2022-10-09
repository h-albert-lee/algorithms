# 세 수, 두 M
#success

import sys

N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]
'''

N = 5
A = [100,234,430,120,489]
'''
A.sort()

def calculator(a,b,c):
    meann = a+b+c
    median = 3*b
    return abs(meann - median)

ans = 0
for i in range(1,N-1):
    ans = max(ans, calculator(A[0], A[i], A[i+1]))
    ans = max(ans, calculator(A[i-1],A[i], A[N-1]))
print(ans)
