#뮤직비디오(결정 알고리즘)
#unsolved
'''
n, m = map(int,input().split())
A = list(map(int, input().split()))
'''

n = 9
m = 3
A = [1,2,3,4,5,6,7,8,9]

def checker(input, A):
    ret = False
    if sum(A) < input:
        ret = True
    return ret
