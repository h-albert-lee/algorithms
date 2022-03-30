#격자판 회문 수
#time limit exceed
A = [list(map(int, input().split())) for _ in range(9)]
'''
A = [[2,4,1,5,3,2,6]
    , [3,5,1,8,7,1,7]
    , [8,3,2,7,1,3,8]
    , [6,1,2,3,2,1,1]
    , [1,3,1,3,5,3,2]
    , [1,1,2,5,6,5,2]
    , [1,2,2,2,2,1,5]]
'''
def check_hwemun(test):
    Ans = True
    center = len(test)//2
    for i in range(center+1):
        if test[center-i] != test[center+i]:
            Ans = False
    return Ans

cnt = 0
for i in range(3):
    for j in range(7):
        check = []
        check.append(A[i][j])
        check.append(A[i+1][j])
        check.append(A[i+2][j])
        check.append(A[i+3][j])
        check.append(A[i+4][j])
        if check_hwemun(check) == True:
            cnt += 1
        check = []
        check.append(A[j][i])
        check.append(A[j][i+1])
        check.append(A[j][i+2])
        check.append(A[j][i+3])
        check.append(A[j][i+4])
        if check_hwemun(check) == True:
            cnt += 1
print(cnt)
