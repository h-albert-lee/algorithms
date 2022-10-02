#왜 안되는거지..?

n = int(input())
max = 0
ans = 0

for _ in range(n):
    tmp = input.split()
    tmp.sort()
    a,b,c = map(int, tmp)
    if (a==b) and (b==c):
        ans = 10000 + (1000*a)
    elif (a==b) or (a==c):
        ans = 1000 + (a*100)
    elif b==c:
        ans = 1000 + (b*100)
    else:
        ans = (c*100)
    if ans>max:
        max = ans

print(max)
