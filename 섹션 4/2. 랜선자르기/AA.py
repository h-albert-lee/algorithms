#랜선 자르기
#success

n, m = map(int, input().split())
A = []
for _ in range(n):
    A.append(int(input()))
'''

n = 5
m = 10
A = [273, 401, 753, 345, 105]
'''
def num_of_parts(x, A):
    num = 0
    for each in A:
        k = each//x
        num += k
    return num

lt = 0
rt = max(A)
ans = -1

while lt <= rt:
    mid = (lt+rt)//2
    if num_of_parts(mid,A)>= m:
        lt = mid + 1
        ans = mid
    else:
        rt = mid -1

print(ans)
