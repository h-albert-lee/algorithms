#격자판 회문 수
#success
A=[list(map(int, input().split())) for _ in range(7)]
'''
A = [[2,4,1,5,3,2,6],
    [3,5,1,8,7,1,7],
    [8,3,2,7,1,3,8],
    [6,1,2,3,2,1,1],
    [1,3,1,3,5,3,2],
    [1,1,2,5,6,5,2],
    [1,2,2,2,2,1,5]]
'''
def do_test(x):
    ans = True
    mid = len(x)//2
    if x[mid-1] != x[mid+1]:
        ans = False
    if x[mid-2] != x[mid+2]:
        ans = False
    return ans

def horizontal_test(A):
    ans = 0
    for lst in A:
        for i in range(3):
            res = lst[i:i+5]
            if do_test(res) == True:
                ans += 1
    return ans

def vertical_test(A):
    ans = 0
    for i in range(7):
        for j in range(3):
            res = []
            res.append(A[j][i])
            res.append(A[j+1][i])
            res.append(A[j+2][i])
            res.append(A[j+3][i])
            res.append(A[j+4][i])
            if do_test(res) == True:
                ans += 1
    return ans

print(horizontal_test(A)+vertical_test(A))
