#뮤직비디오(결정 알고리즘)
#solved(sol)

n, m = map(int,input().split())
A = list(map(int, input().split()))
'''

n = 9
m = 3
A = [1,2,3,4,5,6,7,8,9]
'''
def checker(input, A):
    cnt = 1
    sum = 0
    for each in A:
        if (sum+each) > input:
            cnt += 1
            sum = each
        else:
            sum += each
    return cnt

lt = 1
rt = sum(A)
ans = 0
while lt <= rt:
    mid = (lt+rt)//2
    if checker(mid, A) <= m:
        ans = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(ans)
