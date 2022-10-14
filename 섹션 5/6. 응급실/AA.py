#응급실
#success

n, m = map(int, input().split())
A = list(map(int, input().split()))
'''
n = 6
m = 0
A = [60, 60, 90, 60, 60, 60, 60]
'''
B = []
for i in range(n):
    l = (A[i], i)
    B.append(l)

cnt = 0

def return_max(A):
    max = 0
    for a, e in A:
        if a > max:
            max = a
    return max

while True:
    a = B.pop(0)
    if a[0] >= return_max(B):
        cnt +=1
        if a[1] == m:
            break
    else:
        B.append(a)

print(cnt)
