#이진트리 순회
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

def DFS(n):
    if n>3:
        return



if __name__=="__main__":
    n = 3
    DFS(1)
    A = [0]*n
