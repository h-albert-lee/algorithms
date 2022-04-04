#랜선 자르기
#unsolved

n, k = map(int,input().split())
A = []
for i in range(n):
    tmp=int(input())
    A.append(tmp)
'''
n = 4
k = 11
A = [802,743,457,539]
'''
max = 0
iter = min(A)
for i in range(1,iter):
    divid_list = []
    for each in A:
        divid = each // i
        divid_list.append(divid)
    if sum(divid_list) >= 11:
        if i >= max:
            max = i

print(max)
