#삼각형 만들기
#success

import sys

N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]
'''
N = 6
A = [2,3,2,3,2,4]
'''
A.sort()

answer = -1


for i in range(N-1, 1, -1):
    if A[i] < (A[i-1]+A[i-2]):
        answer = A[i] + A[i-1] + A[i-2]
        break

print(answer)
