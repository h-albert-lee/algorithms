#점수계산

n = int(input())
A = list(map(int, input().split()))
'''
n = 10
A = [1,0,1,1,1,0,0,1,1,0]
'''
cum = 0
sum = 0

for i in range(n):
    if A[i] == 1:
        cum += 1
        sum += cum
    else:
        cum = 0
print(sum)
