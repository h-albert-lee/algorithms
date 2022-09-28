#K번째 수 문제풀이
#solved

#import sys
#sys.stdin=open("in1.txt", "r")

T = int(input())
for i in range(T):
    N,s,e,k = map(int, input().split())
    slice = list(map(int, input().split()))
    slice = slice[s-1:e]
    slice.sort()
    print('#%d %d' %(i+1, slice[k-1]))
