#이분검색
#solved

n,m = map(int, input().split())
A = list(map(int, input().split()))
'''
n = 8
m = 32
A = [23,87,65,12,57,32,99,81]
'''
A.sort()
index = 0
for index, value in enumerate(A):
    if value == m:
        ans = index

ans += 1
print(ans)
