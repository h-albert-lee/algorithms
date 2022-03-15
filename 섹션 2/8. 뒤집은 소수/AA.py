#뒤집은 소수
#solved

n= int(input())
K = list(map(int, input().split()))


def reverse(x):
    number = str(x)
    length = len(number) -1
    new_number = ""
    for each in range(length,-1,-1):
        if number[each] == 0:
            pass
        else:
            new_number += number[each]
    return int(new_number)

def isPrime(x):
    yaksu = []
    for i in range(1,x+1):
        divid = divmod(x,i)
        if divid[1] == 0:
            yaksu.append(i)
        else:
            pass
    if len(yaksu) == 2:
        ans = True
    else:
        ans = False
    return ans

for each in K:
     check = isPrime(reverse(each))
     if check == True:
         print(reverse(each), end = ' ')
     elif check == False:
         pass
