#두 리스트 합치기
#success

n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
'''

n = 10
A = [1,10,27,39,50,61,65,70,93,93]
m = 7
B = [7,51,65,66,70,82,93]
'''
res = []
while len(A) > 0 and len(B)>0:
    if A[0] < B[0]:
        k = A.pop(0)
        res.append(k)
    else:
        k = B.pop(0)
        res.append(k)
if len(A)>0:
    for each in A:
        res.append(each)
else:
    for each in B:
        res.append(each)

for each in res:
    print(each, end = ' ')
