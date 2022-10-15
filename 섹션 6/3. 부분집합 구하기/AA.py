#이진트리 순회
#success

'''
#이진트리순회

def DFS(n):
    if n > 7:
        return
    else:
        print(n, end = '')
        DFS(n*2)
        DFS(n*2+1)




if __name__=="__main__":
    DFS(1)
'''

#부분집합구하기

def DFS(v):
    if v>n:
        for i in range(1, n+1):
            if A[i] == 1:
                print(i, end = ' ')
        print()

    else:
        A[v] = 1
        DFS(v+1)
        A[v] = 0
        DFS(v+1)


if __name__=="__main__":
    n = int(input())
    A = [0]*(n+1)
    DFS(1)
