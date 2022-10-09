#나무자르기
#success

import sys

N = int(sys.stdin.readline())
H = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))
'''
N = 5
H = [1,3,2,4,6]
A = [2,7,3,4,1]
'''
I = list(range(N))

indice = sorted(I, key = lambda i:A[i])

ans = 0

for i in range(N):
    index = indice[i]
    ans += H[index] + i*A[index]
print(ans)
