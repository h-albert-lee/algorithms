#재귀함수를 이용한 이진수 출력
#solved
def DFS(x):
    if x == 0:
        pass
    else:
        DFS(x//2)
        print(x%2, end = '')


k = int(input())
DFS(k)
