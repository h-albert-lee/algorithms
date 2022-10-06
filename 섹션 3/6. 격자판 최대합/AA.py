#격자판 최대합
#수정 필요

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

for each in A:
    if sum(each) > 0:
        max = sum(each)

for i in range(n):
    summ = 0
    for j in range(n):
        summ += A[j][i]
    if summ > max:
        max = summ

summ2 = 0
for i in range(n):
    summ2 += A[i][i]
if summ2 > max:
    max = summ2
summ3 = 0
for i in range(n):
    summ3 += A[i][n-1-i]
if summ3 > max:
    max = summ3

print(max)
