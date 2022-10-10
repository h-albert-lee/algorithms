from itertools import permutations
#success

'''
n = int(input())
A = list(map(int, input().split()))
'''

n = 6
A = [20,1,15,8,4,10]
max = 0
for each in list(permutations(A)):
    a = 0
    for i in range(1, n):
        a += abs(each[i-1]-each[i])
    if a > max:
        max = a


print(max)
