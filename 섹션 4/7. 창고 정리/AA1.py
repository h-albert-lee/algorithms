#창고정리
#solved

l = int(input())
L = list(input().split())
m = int(input())
'''

l = 10
L = [69,42,68,76,40,87,14,65,76,81]
m = 50
'''
L.sort()

for _ in range(m):
    L[l-1] = L[l-1] - 1
    L[0] = L[0] + 1
    L.sort()


print(L[l-1] - L[0])
