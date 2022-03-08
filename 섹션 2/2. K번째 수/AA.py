#K번째 수 문제풀이

T = list(input().split())
n,s,e,k = map(int, input().split())
N = list(input().split())

list_ = N[s+1:e+1]
ans = list_.sort()
answer = ans[k+1]
print(answer)
