#두 리스트 합치기
#time limit exceed

n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))
#n = 3
#N = [1,3,5]
#m = 5
#M = [2,3,6,7,9]

#pointer
p1 = 0
p2 = 0
ans_list = []

while p1<n and p2<m:
    if N[p1] <= M[p2]:
        ans_list.append(N[p1])
        p1 += 1
    elif N[p1] > M[p2]:
        ans_list.append(M[p2])
        p2 += 1

if p1<n:
    ans_list = ans_list + N[p1:]

if p2<m:
    ans_list = ans_list + M[p2:]

for i in ans_list:
    print(i, end = ' ')
