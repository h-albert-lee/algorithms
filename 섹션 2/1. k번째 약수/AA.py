#K번째 약수 again

n, k= map(int, input().split())
'''
n = 6
k = 3
'''
lst = []
for i in range(1, n+1):
    if n % i == 0:
        lst.append(i)

if len(lst) < k:
    print(-1)
else:
    print(lst[k-1])
