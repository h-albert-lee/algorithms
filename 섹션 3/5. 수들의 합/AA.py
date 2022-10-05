#수들의 합
#시간복잡도 해결 필요

n, m = map(int, input().split())
A = list(map(int,input().split()))
'''
n = 8
m = 3
A = [1,2,1,3,1,1,1,2]
'''
ans = 0
for i in range(0, len(A)):
    for j in range(i+1,len(A)+1):
        if sum(A[i:j]) == m:
            ans += 1
print(ans)
