#재귀함수를 이용한 이진수 출력
#solved
def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')

if __name__=="__main__":
    k = int(input())
    DFS(k)
