#카드 역배치
A = list(range(1,21))

def reverse(x):
    lst = []
    while len(x) != 0:
        k = x.pop()
        lst.append(k)
    return lst

for _ in range(10):
    a, b= map(int,input().split())
    res = A[a-1:b]
    res2 = reverse(res)
    A[a-1:b] = res2


for i in A:
    print(i, end = ' ')
