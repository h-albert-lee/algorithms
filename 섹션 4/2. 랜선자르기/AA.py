#랜선 자르기
#solved(sol)

k, n = map(int,input().split())
A = []
for i in range(k):
    tmp=int(input())
    A.append(tmp)

'''
k = 4
n = 11
A = [802,743,457,539]
large = 802
'''
def checker(len, list):
    cnt = 0
    for each in list:
        cnt += (each//len)
    return cnt

small = 1
big = max(A)
ans = 0

while small <= big:
    len = (small + big) // 2
    if checker(len, A) >= n:
        ans = len
        small = len +1
    else:
        big = len - 1

print(ans)
