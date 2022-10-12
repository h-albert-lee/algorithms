#이분 검색
#success
n, m = map(int, input().split())
A = list(map(int, input().split()))
'''
n = 8
m = 32
A = [23,87,65,12,57,32,99,81]
'''
A.sort()
lt = 0
rt = n


while lt < rt:
    mid = (lt + rt)//2
    if A[mid] < m:
        lt = mid + 1
    elif A[mid] == m:
        ans = mid
        break
    elif A[mid] > m:
        rt = mid -1

print(ans + 1)
