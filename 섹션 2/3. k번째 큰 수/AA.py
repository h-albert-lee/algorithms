#import sys
#sys.stdin=open("input.txt", "r")

n, k= map(int, input().split())
N = list(map(int, input().split()))
#n = 10
#k = 3
#N = [13,15,34,23,45,65,33,11,26,42]

N.sort(reverse=True)
list = []
for i in range(n):
    for j in range(1,n-1):
        for k in range(1,n-2):
            each = N[i] + N[i+j] + N[i+j+k]
            list.append(each)
            if len(list) > int(k):
                break
        if len(list) > int(k):
            break
    if len(list) > int(k):
        break

ans = list[k-1]
print(ans)
