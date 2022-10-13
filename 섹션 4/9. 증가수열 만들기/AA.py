#증가수열 만들기
#강의수강

'''
n = int(input())
A = list(map(int, input().split()))
'''
n = 5
A = [2,4,5,1,3]

cnt = 0
lr = ''
lst = 0

#초기값
if A[0] < A[-1]:
    cnt += 1
    lr += 'L'
    lst = A[0]
    A.pop(0)
else:
    cnt += 1
    lr += 'R'
    lst = A[-1]
    A.pop()
