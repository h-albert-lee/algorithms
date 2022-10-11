#사과나무 again
#success

n = int(input())
A=[list(map(int, input().split())) for _ in range(n)]

'''
n = 5
A = [[10,13,10,12,15],
    [12,39,30,23,11],
    [11,25,50,53,15],
    [19,27,29,37,27],
    [19,13,30,13,19]]
'''
mid = n//2 + 1
iter = n//2 + 1

sum = 0
for i in range(0, iter):
    lst = A[i][mid-i-1:mid+i]
    for each in lst:
        sum += each
for i in range(iter,n):
    index = n-1-i
    lst = A[i][mid-index-1:mid+index]
    for each in lst:
        sum += each
print(sum)
