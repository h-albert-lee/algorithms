#스도쿠 검사
#solved

A = [list(map(int, input().split())) for _ in range(9)]
'''
A = [[1,4,3,6,2,8,5,7,9]
    , [5,7,2,1,3,9,4,6,8]
    , [9,8,6,7,5,4,2,3,1]
    , [3,9,1,5,4,2,7,8,6]
    , [5,6,8,9,1,7,3,5,2]
    , [7,2,5,8,6,3,9,1,4]
    , [2,3,7,4,8,1,6,9,5]
    , [6,1,9,2,7,5,8,4,3]
    , [8,5,4,3,9,6,1,2,7]]
'''

right = {1,2,3,4,5,6,7,8,9}
Ans = True
for i in range(0,9,3):
    id_1 = i
    id_2 = i+1
    id_3 = i+2
    for j in range(0,9,3):
        ans_list = []
        ld_1 = j
        ld_2 = j+1
        ld_3 = j+2
        ans_list.append(A[id_1][ld_1])
        ans_list.append(A[id_1][ld_2])
        ans_list.append(A[id_1][ld_3])
        ans_list.append(A[id_2][ld_1])
        ans_list.append(A[id_2][ld_2])
        ans_list.append(A[id_2][ld_3])
        ans_list.append(A[id_3][ld_1])
        ans_list.append(A[id_3][ld_2])
        ans_list.append(A[id_3][ld_3])
        check = set(ans_list)
        if check != right:
            Ans = False

if Ans == True:
    print('YES')
elif Ans == False:
    print('NO')
