n = input()
N = list(map(int, input().split()))
#n = 10
#N = [45,73,66,87,92,67,75,79,75,80]

index = list(range(1,n+1))
dict = dict(zip(N, index))

mean = float(sum(N) / n)
mean = round(mean)
print(mean)

for i in range(10):
    m1 = int(mean + i)
    m2 = int(mean - i)
    if m1 in N:
        indice = N.index(m1)
        value = N[indice]
        break
    elif m2 in N:
        indice = N.index(m2)
        value = N[indice]
        break
    else:
        continue

number = indice +1
print(number, value)
