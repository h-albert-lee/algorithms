#뮤직비디오
#success

m, n = map(int, input().split())
A = list(map(int, input().split()))
'''
m = 9
n = 3
A = [1,2,3,4,5,6,7,8,9]
'''
def do_test(x, A):
    cnt = 1
    repo = 0
    for each in A:
        repo += each
        if repo > x:
            repo = each
            cnt += 1
    return cnt

lt = 0
rt = 10000
ans = -1

while lt<= rt:
    mid = (lt+rt)//2
    if do_test(mid, A) <= n:
        rt = mid - 1
        ans = mid
    else:
        lt = mid +1

print(ans)
