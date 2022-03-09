#K번째 수 문제풀이
T = int(input())
for i in range(T):
    N,s,e,k = map(int, input().split()))
    list = list(map(int, input().split()))
    list_ = list[s-1:e-1]
    ans = list_.sort()
    answer = int(ans[k-1])
    print('#' + 'T+1' + ' ' + answer)
