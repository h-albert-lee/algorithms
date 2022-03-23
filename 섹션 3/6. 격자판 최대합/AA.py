#격자판 최대합
#solved

n=int(input())
A=[list(map(int, input().split())) for _ in range(n)]
'''
n = 5
A = [[10,13,10,12,15],
    [12,39,30,23,11],
    [11,25,50,53,15],
    [19,27,29,37,27],
    [19,13,30,13,19]]
'''
max = 0
#세로

for i in range(n):
    sum1 = 0
    for j in range(n):
        sum1 += A[i][j]
    if sum1 > max:
        max = sum1
#가로
sum2 = 0
for i in range(n):
    sum2 = sum(A[i])
if sum2 > max:
    max = sum2

#대각선 1
sum3 = 0
for i in range(n):
    sum3 += A[i][i]
if sum3 > max:
    max = sum3

#대각선 2
sum4 = 0
for i in range(n):
    sum4 += A[i][n-i-1]
if sum4 > max:
    max = sum4

print(max)
