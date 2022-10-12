#스도쿠 검사
#success
A=[list(map(int, input().split())) for _ in range(9)]

'''
A = [[1,2,3,4,5,6,7,8,9],
    [2,1,4,3,6,5,8,9,7],
    [3,4,1,2,7,8,9,5,6],
    [4,3,2,1,8,9,6,7,5],
    [5,6,7,8,9,1,2,3,4],
    [6,5,8,9,1,7,3,4,2],
    [7,8,9,5,2,3,4,6,1],
    [8,9,6,7,4,2,5,1,3],
    [9,7,5,6,3,4,1,2,8]]
'''
eval_set = set([1,2,3,4,5,6,7,8,9])

def horizon_test(A):
    ans = True
    for lst in A:
        test = set(lst)
        if test != eval_set:
            ans = False
    return ans

def vertical_test(A):
    ans = True
    for i in range(9):
        lst = []
        for j in range(9):
            lst.append(A[j][i])
        test = set(lst)
        if test != eval_set:
            ans = False
    return ans

def partition_test(A):
    ans = True
    for i in range(3):
        i = i*3
        for j in range(3):
            lst = []
            j = j*3
            lst.append(A[i][j])
            lst.append(A[i][j+1])
            lst.append(A[i][j+2])
            lst.append(A[i+1][j])
            lst.append(A[i+1][j+1])
            lst.append(A[i+1][j+2])
            lst.append(A[i+2][j])
            lst.append(A[i+2][j+1])
            lst.append(A[i+2][j+2])
            test = set(lst)
            if test != eval_set:
                ans = False
    return ans

if (horizon_test(A) == True) and (vertical_test(A)==True) and (partition_test(A) == True):
    print("YES")
else:
    print("NO")
