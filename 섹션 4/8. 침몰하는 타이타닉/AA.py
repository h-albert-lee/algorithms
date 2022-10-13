#침몰하는 타이타닉
#success

n, m = map(int, input().split())
A = list(map(int, input().split()))
'''
n = 5
m = 140
A = [90,50,70,100,60]
'''
A.sort(reverse = True)
cnt = 0

while len(A) > 0:
    if len(A) == 1:
        cnt += 1
        break
    else:
        a = A.pop(0)
        b = A.pop()
        if (a+b) <= m:
            pass
        else:
            A.append(b)
        cnt += 1

print(cnt)
