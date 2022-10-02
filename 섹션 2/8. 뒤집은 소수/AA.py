#뒤집은 소수
#success
n = int(input())
numbers = map(int, input().split())
'''
n = 5
numbers = [32,55,62,3700,250]
'''

def isPrime(x):
    x = int(x)
    if (x != 1) or (x != 2):
        for i in range(2, x):
            if x%i == 0:
                result = False
                break
            else:
                result = True
    if x == 1:
        result = False
    if x == 2:
        result = True
    return result

def reverse(x):
    y = str(x)
    result = str()
    for i in y:
        result = i + result
    return int(result)


for each in numbers:
    a = reverse(each)
    if isPrime(a):
        print(a, end = ' ')
