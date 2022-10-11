#2차원 배열의 합
'''
n, m = map(int, input().split())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))
'''
n = 2
m = 3
A = [[1,2,4], [8,16,32]]

#누적합 행렬 구하기
psum = [[0 for _ in range(m)] for _ in range(n)]
psum[0][0] = A[0][0]
for i in range(1,m):
    psum[0][i] = A[0][i] + psum[0][i-1]
for i in range(1,n):
    psum[i][0] = A[i][0] + psum[i-1][0]
print(psum)
for i in range(1, n):
    for j in range(1, m):
        if psum[i][j] != 0:
            pass
        else:
            psum[i][j] = A[i][j] + psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1]

'''
k = int(input())
a,b,c,d = map(int, input().split())
'''
k = 3
a = 1
b = 3
c = 2
d = 3
ans = 0
for _ in range(k):
    if (a==1) and (b==1):
        ans = psum[c-1][d-1]
    elif (a==1) and (b!=1):
        ans = psum[c-1][d-1] - psum[c-1][b-2]
    elif (a!=1) and (b==1):
        ans = psum[c-1][d-1] - psum[a-2][d-1]
    else:
        ans = psum[c-1][d-1] - psum[c-1][b-2] - psum[a-2][d-1] + psum[a-2][b-2]
    print(ans)
