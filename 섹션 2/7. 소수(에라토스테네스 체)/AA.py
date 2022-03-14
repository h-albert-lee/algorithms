n= int(input())

def sosu(n):
    sos = 0
    for i in range(1, n+1):
        divid = []
        for j in range(1,n+1):
            check = divmod(i,j)
            if check[1] == 0:
                divid.append(j)
        if len(divid) == 2:
            sos += 1
    return sos

print(sosu(n))
