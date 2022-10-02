#에라토스테네스 체

N = int(input())


#N = 20

lst = list(range(2, N+1))
sosu = []

while True:
    a = lst.pop(0)
    sosu.append(a)
    iter_num = N//a
    for i in range(2,iter_num+1):
        if a*i in lst:
            lst.remove(a*i)
    if len(lst) == 0:
        break

print(len(sosu))
