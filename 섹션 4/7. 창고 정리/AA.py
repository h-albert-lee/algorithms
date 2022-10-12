#창고정리
#success
l = int(input())
A = list(map(int, input().split()))
m = int(input())
'''

l = 10
A = [69,42,68,76,40,87,14,65,76,81]
m = 50
'''
for _ in range(m):
    A.sort()
    A[0] = A[0]+1
    A[l-1] = A[l-1]-1

print(max(A)- min(A))
