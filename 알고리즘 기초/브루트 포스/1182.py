#부분 수열의 합
#success

import sys
from itertools import combinations
'''
n, s = map(int,sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
'''

n = 5
s = 0
A = [-7, -3, -2, 5, 8]

ans = 0

for i in range(1,n+1):
    for each in list(combinations(A,i)):
        if sum(each) == s:
            ans +=1

print(ans)
