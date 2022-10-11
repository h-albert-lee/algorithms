#곳감
#success

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

def rotate(a,b,c,A):
    a = int(a) -1
    if b == 0:
        K = A[a]
        for _ in range(c):
            i = K.pop(0)
            K.append(i)
        A[a] = K
    elif b == 1:
        K = A[a]
        for _ in range(c):
            i = K.pop()
            K.insert(0, i)
        A[a] = K
    return A


m = int(input())

for _ in range(m):
    a,b,c = map(int, input().split())
    A = rotate(a,b,c,A)

mid = n//2 + 1
upper = n
lower = 0
sum = 0
for i in range(n):
    if upper >= lower:
        lines = A[i]
        lines = lines[lower:upper]
        for each in lines:
            sum += each
        upper -= 1
        lower += 1
    else:
        lines = A[i]
        lines = lines[upper-1:lower+1]
        for each in lines:
            sum += each
        upper -= 1
        lower += 1
print(sum)
