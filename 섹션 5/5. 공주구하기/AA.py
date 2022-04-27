#공주구하기
#sol
n, k = map(int, input().split())
'''
n = 8
k = 3
'''
que = list(range(1,n+1))


while que:
    for _ in range(k-1):
        d = que.pop(0)
        que.append(d)
    que.pop(0)
    if len(que) == 1:
        print(que[0])
        que.pop()
