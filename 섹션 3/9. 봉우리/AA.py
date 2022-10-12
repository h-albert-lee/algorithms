#봉우리
#success

n = int(input())
A=[list(map(int, input().split())) for _ in range(n)]

'''
n = 5
A = [[5,3,7,2,3],
    [3,7,1,6,1],
    [7,2,5,3,4],
    [4,3,6,4,1],
    [8,7,3,5,2]]
'''
def padding(A, n):
    B = [[0]*(n+2) for _ in range(n+2)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            B[i][j] = A[i-1][j-1]
    return B

def count_bong(B):
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if B[i][j] <= B[i-1][j]:
                pass
            elif B[i][j] <= B[i+1][j]:
                pass
            elif B[i][j] <= B[i][j-1]:
                pass
            elif B[i][j] <= B[i][j+1]:
                pass
            else:
                count += 1
    return count

B = padding(A, n)
print(count_bong(B))
