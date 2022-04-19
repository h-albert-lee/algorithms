#마구간 정하기
#solved(sol)

n, c = map(int, input().split())
A = []
for _ in range(n):
    a = int(input())
    A.append(a)
'''
n = 5
c = 3
A = [1,2,8,4,9]
'''

def checker(dis, list):
    cnt = 1
    stat = list[0]
    for i in range(1,n):
        if list[i] - stat >= dis:
            cnt += 1
            stat = list[i]
    return cnt

A.sort()

lt = 1
rt = max(A)


ans = 0

while lt <= rt:
    mid = (lt+rt) // 2
    if checker(mid, A) >= c:
         ans = mid
         lt = mid +1
    else:
        rt = mid -1


print(ans)
