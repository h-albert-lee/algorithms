#수들의 합
#solved, time limit exceed

n, m = map(int, input().split())
A =  list(map(int, input().split()))


count = 0

for i in range(0,n):
    for j in range(i+1, n+1):
        check = sum(A[i:j])
        if check == m:
            count += 1

print(count)
