#K번째 수 again

n = int(input())

for i in range(n):
    N, s, e, k = map(int, input().split())
    lst = list(map(int, input().split()))
    slice = lst[s-1:e]
    slice.sort()
    ans = slice[k-1]
    print('#%d %d'%(i+1, ans))
